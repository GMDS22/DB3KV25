# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-22 02:09:54
- Entries: 3007
- Roles: {'assistant': 9, 'system': 2498, 'operator': 500}
- Event types: {'assistant_prompt': 4, 'assistant_analysis': 1, 'voice_status': 2498, 'spoken_confirmation': 1, 'voice_transcript_partial': 370, 'voice_transcript_final': 127, 'voice_command': 3, 'spoken_reply': 3}
- Channels: {'text': 5, 'voice': 3002}
- Latest operator request: that s
- Latest assistant message: My current scope is normal conversation, Smart Sentry help, diagnostics on request, and supported command handling.

## Timeline

- [2026-08-22 01:17:27] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-22 01:17:27] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-22 01:17:29] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787332649.45167 | source=vosk
- [2026-08-22 01:17:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332652.0333989 | source=vosk | rms=232 | updated_at=1787332652.0323997
- [2026-08-22 01:17:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332652.7168565 | source=vosk | rms=232 | updated_at=1787332652.0323997
- [2026-08-22 01:17:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332656.0162659 | source=vosk | rms=232 | updated_at=1787332652.0323997
- [2026-08-22 01:17:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332656.71648 | source=vosk | rms=232 | updated_at=1787332652.0323997
- [2026-08-22 01:17:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332657.2165387 | source=vosk | rms=232 | updated_at=1787332652.0323997
- [2026-08-22 01:17:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332657.7178652 | source=vosk | rms=232 | updated_at=1787332652.0323997
- [2026-08-22 01:17:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332660.2177613 | source=vosk | rms=157 | updated_at=1787332660.2177613
- [2026-08-22 01:17:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332661.4667647 | source=vosk | rms=306 | updated_at=1787332660.9660125
- [2026-08-22 01:18:05] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-22 01:18:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332688.818039 | source=vosk | rms=930 | updated_at=1787332688.818039
- [2026-08-22 01:18:10] operator / voice_transcript_partial / voice: smite
  meta: kind=partial | timestamp=1787332690.3948388 | source=vosk | rms=136 | updated_at=1787332690.1886718
- [2026-08-22 01:18:10] operator / voice_transcript_partial / voice: smiley
  meta: kind=partial | timestamp=1787332690.4869576 | source=vosk | rms=136 | updated_at=1787332690.1886718
- [2026-08-22 01:18:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332690.6877568 | source=vosk | rms=136 | updated_at=1787332690.1886718
- [2026-08-22 01:18:10] operator / voice_transcript_partial / voice: smiley are
  meta: kind=partial | timestamp=1787332690.7375216 | source=vosk | rms=136 | updated_at=1787332690.1886718
- [2026-08-22 01:18:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332691.1878757 | source=vosk | rms=136 | updated_at=1787332690.1886718
- [2026-08-22 01:18:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332691.6870587 | source=vosk | rms=138 | updated_at=1787332691.6870587
- [2026-08-22 01:18:11] operator / voice_transcript_partial / voice: smiley are you
  meta: kind=partial | timestamp=1787332691.7357674 | source=vosk | rms=138 | updated_at=1787332691.6870587
- [2026-08-22 01:18:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332692.1864746 | source=vosk | rms=138 | updated_at=1787332691.6870587
- [2026-08-22 01:18:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332692.4393504 | source=vosk | rms=251 | updated_at=1787332692.4393504
- [2026-08-22 01:18:12] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1787332692.6730275 | source=final | rms=251 | updated_at=1787332692.4393504
- [2026-08-22 01:18:12] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787332692.7120738 | source=state | rms=251 | updated_at=1787332692.4393504
- [2026-08-22 01:18:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332692.7120738 | source=state | rms=251 | updated_at=1787332692.4393504
- [2026-08-22 01:18:12] operator / voice_command / voice: who are you
  meta: normalized=True
- [2026-08-22 01:18:12] assistant / assistant_prompt / text: I am Elion Mesk, or Elion for short, the AI assistant voice for Smart Sentry. I can talk with you normally, help with Smart Sentry questions, and switch into diagnostics when you ask.
  meta: task_kind=prompt | speak_requested=True
- [2026-08-22 01:18:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332692.7130756 | source=vosk | rms=166 | updated_at=1787332692.7130756
- [2026-08-22 01:18:13] assistant / spoken_reply / voice: I am Elion Mesk, or Elion for short, the AI assistant voice for Smart Sentry. I can talk with you normally, help with Smart Sentry questions, and switch into diagnostics when you ask.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-08-22 01:18:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332693.4365003 | source=vosk | rms=259 | updated_at=1787332692.937856
- [2026-08-22 01:18:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332693.6874633 | source=vosk | rms=180 | updated_at=1787332693.6874633
- [2026-08-22 01:18:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332694.438266 | source=vosk | rms=152 | updated_at=1787332693.9368646
- [2026-08-22 01:18:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332695.186533 | source=vosk | rms=1055 | updated_at=1787332695.186533
- [2026-08-22 01:18:17] operator / voice_transcript_partial / voice: click got
  meta: kind=partial | timestamp=1787332697.2894306 | source=vosk | rms=1205 | updated_at=1787332697.2136626
- [2026-08-22 01:18:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332697.4469304 | source=vosk | rms=1205 | updated_at=1787332697.4469304
- [2026-08-22 01:18:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332697.6973183 | source=vosk | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332698.1967535 | source=vosk | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:19] operator / voice_transcript_final / voice: click got
  meta: kind=final | timestamp=1787332699.2070312 | source=final | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332699.2481673 | source=vosk | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:19] operator / voice_transcript_final / voice: click got
  meta: kind=final | timestamp=1787332699.5731227 | source=final | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332699.6094968 | source=vosk | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332700.199319 | source=vosk | rms=1167 | updated_at=1787332697.6973183
- [2026-08-22 01:18:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332700.6964798 | source=vosk | rms=1202 | updated_at=1787332700.6964798
- [2026-08-22 01:18:21] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1787332701.9878666 | source=vosk | rms=176 | updated_at=1787332701.946606
- [2026-08-22 01:18:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332702.1970768 | source=vosk | rms=1193 | updated_at=1787332702.1970768
- [2026-08-22 01:18:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332702.4469326 | source=vosk | rms=1205 | updated_at=1787332702.4469326
- [2026-08-22 01:18:23] operator / voice_transcript_final / voice: of good
  meta: kind=final | timestamp=1787332703.5885105 | source=final | rms=1205 | updated_at=1787332702.4469326
- [2026-08-22 01:18:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332703.6321669 | source=vosk | rms=1205 | updated_at=1787332702.4469326
- [2026-08-22 01:18:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332704.230545 | source=vosk | rms=962 | updated_at=1787332704.230545
- [2026-08-22 01:18:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332704.9480195 | source=vosk | rms=1202 | updated_at=1787332704.4470246
- [2026-08-22 01:18:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332705.1981354 | source=vosk | rms=1172 | updated_at=1787332705.196632
- [2026-08-22 01:18:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332705.9469242 | source=vosk | rms=1200 | updated_at=1787332705.4473011
- [2026-08-22 01:18:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332708.0195532 | source=vosk | rms=1112 | updated_at=1787332708.0195532 | frequency_hz=224.0
- [2026-08-22 01:18:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332709.1979277 | source=vosk | rms=862 | updated_at=1787332708.6968958 | frequency_hz=224.0
- [2026-08-22 01:18:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332711.8263516 | source=vosk | rms=775 | updated_at=1787332711.8263516 | frequency_hz=224.0
- [2026-08-22 01:18:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332712.9095156 | source=vosk | rms=864 | updated_at=1787332712.256872 | frequency_hz=224.0
- [2026-08-22 01:18:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332713.7593944 | source=vosk | rms=1116 | updated_at=1787332713.7593944 | frequency_hz=224.0
- [2026-08-22 01:18:34] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1787332714.8450165 | source=vosk | rms=1206 | updated_at=1787332714.7570431 | frequency_hz=224.0
- [2026-08-22 01:18:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332715.0071797 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:35] operator / voice_transcript_partial / voice: this much
  meta: kind=partial | timestamp=1787332715.0533385 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332715.2600694 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:35] operator / voice_transcript_partial / voice: this much so that
  meta: kind=partial | timestamp=1787332715.3717706 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332715.506735 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:35] operator / voice_transcript_partial / voice: this much so that it would
  meta: kind=partial | timestamp=1787332715.6930218 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332716.2564387 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:36] operator / voice_transcript_partial / voice: this much so that able to
  meta: kind=partial | timestamp=1787332716.3197517 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332716.7649395 | source=vosk | rms=1091 | updated_at=1787332715.0071797 | frequency_hz=224.0
- [2026-08-22 01:18:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332717.0069962 | source=vosk | rms=1200 | updated_at=1787332717.0069962 | frequency_hz=224.0
- [2026-08-22 01:18:37] operator / voice_transcript_partial / voice: this much so that able to dublin
  meta: kind=partial | timestamp=1787332717.128013 | source=vosk | rms=1200 | updated_at=1787332717.0069962 | frequency_hz=224.0
- [2026-08-22 01:18:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332717.2580433 | source=vosk | rms=1201 | updated_at=1787332717.2580433 | frequency_hz=224.0
- [2026-08-22 01:18:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332717.5294647 | source=vosk | rms=1201 | updated_at=1787332717.5294647 | frequency_hz=224.0
- [2026-08-22 01:18:37] operator / voice_transcript_final / voice: this much so that able to dublin
  meta: kind=final | timestamp=1787332717.861395 | source=final | rms=1201 | updated_at=1787332717.5294647 | frequency_hz=224.0
- [2026-08-22 01:18:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332718.0079598 | source=vosk | rms=1201 | updated_at=1787332717.5294647 | frequency_hz=224.0
- [2026-08-22 01:18:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332718.0079598 | source=vosk | rms=1200 | updated_at=1787332718.0079598 | frequency_hz=224.0
- [2026-08-22 01:18:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332718.5079007 | source=vosk | rms=1200 | updated_at=1787332718.0079598 | frequency_hz=224.0
- [2026-08-22 01:18:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332720.0083456 | source=vosk | rms=1202 | updated_at=1787332720.0083456 | frequency_hz=224.0
- [2026-08-22 01:18:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332720.5070174 | source=vosk | rms=1202 | updated_at=1787332720.0083456 | frequency_hz=224.0
- [2026-08-22 01:18:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332724.2572172 | source=vosk | rms=1203 | updated_at=1787332724.2572172 | frequency_hz=224.0
- [2026-08-22 01:18:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332725.0066903 | source=vosk | rms=1206 | updated_at=1787332724.508192 | frequency_hz=224.0
- [2026-08-22 01:18:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332725.5115614 | source=vosk | rms=1109 | updated_at=1787332725.5115614 | frequency_hz=275.8
- [2026-08-22 01:18:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332729.2996848 | source=vosk | rms=1204 | updated_at=1787332728.758222 | frequency_hz=232.5
- [2026-08-22 01:18:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332733.7599077 | source=vosk | rms=957 | updated_at=1787332733.7599077 | frequency_hz=324.0
- [2026-08-22 01:18:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332735.2579308 | source=vosk | rms=775 | updated_at=1787332734.7649927 | frequency_hz=324.0
- [2026-08-22 01:18:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332736.7572975 | source=vosk | rms=1206 | updated_at=1787332736.7572975 | frequency_hz=324.0
- [2026-08-22 01:18:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332737.5066607 | source=vosk | rms=1204 | updated_at=1787332737.0070539 | frequency_hz=324.0
- [2026-08-22 01:18:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332738.0082388 | source=vosk | rms=1204 | updated_at=1787332738.0082388 | frequency_hz=324.0
- [2026-08-22 01:18:58] operator / voice_transcript_partial / voice: school
  meta: kind=partial | timestamp=1787332738.050797 | source=vosk | rms=1204 | updated_at=1787332738.0082388 | frequency_hz=324.0
- [2026-08-22 01:18:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332738.3100524 | source=vosk | rms=1202 | updated_at=1787332738.3100524 | frequency_hz=324.0
- [2026-08-22 01:18:58] operator / voice_transcript_final / voice: school
  meta: kind=final | timestamp=1787332738.7532651 | source=final | rms=1202 | updated_at=1787332738.3100524 | frequency_hz=324.0
- [2026-08-22 01:18:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332738.7953124 | source=vosk | rms=1202 | updated_at=1787332738.3100524 | frequency_hz=324.0
- [2026-08-22 01:18:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332738.7953124 | source=vosk | rms=1201 | updated_at=1787332738.7953124 | frequency_hz=324.0
- [2026-08-22 01:18:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332739.5075324 | source=vosk | rms=1201 | updated_at=1787332738.7953124 | frequency_hz=324.0
- [2026-08-22 01:19:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332740.0080416 | source=vosk | rms=1201 | updated_at=1787332738.7953124 | frequency_hz=324.0
- [2026-08-22 01:19:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332741.758194 | source=vosk | rms=1204 | updated_at=1787332741.257526 | frequency_hz=304.0
- [2026-08-22 01:19:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332742.2609568 | source=vosk | rms=1201 | updated_at=1787332742.2609568 | frequency_hz=304.0
- [2026-08-22 01:19:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332743.50663 | source=vosk | rms=420 | updated_at=1787332743.0070636 | frequency_hz=304.0
- [2026-08-22 01:19:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332745.5227575 | source=vosk | rms=420 | updated_at=1787332743.0070636 | frequency_hz=304.0
- [2026-08-22 01:19:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332746.0074325 | source=vosk | rms=420 | updated_at=1787332743.0070636 | frequency_hz=304.0
- [2026-08-22 01:19:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332750.0131474 | source=vosk | rms=490 | updated_at=1787332750.0131474 | frequency_hz=176.0
- [2026-08-22 01:19:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332751.0072653 | source=vosk | rms=1122 | updated_at=1787332750.5084007 | frequency_hz=176.0
- [2026-08-22 01:19:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332753.4317064 | source=vosk | rms=1200 | updated_at=1787332753.4317064 | frequency_hz=176.0
- [2026-08-22 01:19:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332754.0075092 | source=vosk | rms=1200 | updated_at=1787332753.4317064 | frequency_hz=176.0
- [2026-08-22 01:19:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332754.511462 | source=vosk | rms=1206 | updated_at=1787332754.511462 | frequency_hz=176.0
- [2026-08-22 01:19:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332756.0073686 | source=vosk | rms=882 | updated_at=1787332755.507449 | frequency_hz=249.5
- [2026-08-22 01:19:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332756.5111024 | source=vosk | rms=883 | updated_at=1787332756.5111024 | frequency_hz=254.6
- [2026-08-22 01:19:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332758.0075088 | source=vosk | rms=1202 | updated_at=1787332757.5069358 | frequency_hz=254.6
- [2026-08-22 01:19:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332761.287623 | source=vosk | rms=1204 | updated_at=1787332761.287623 | frequency_hz=254.6
- [2026-08-22 01:19:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332762.007327 | source=vosk | rms=1202 | updated_at=1787332761.5075738 | frequency_hz=254.6
- [2026-08-22 01:19:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332762.258115 | source=vosk | rms=1206 | updated_at=1787332762.258115 | frequency_hz=254.6
- [2026-08-22 01:19:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332763.0077453 | source=vosk | rms=1204 | updated_at=1787332762.5086439 | frequency_hz=254.6
- [2026-08-22 01:19:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332764.2575505 | source=vosk | rms=1204 | updated_at=1787332762.5086439 | frequency_hz=254.6
- [2026-08-22 01:19:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332766.7570434 | source=vosk | rms=1205 | updated_at=1787332765.831753 | frequency_hz=254.6
- [2026-08-22 01:19:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332767.0067642 | source=vosk | rms=1204 | updated_at=1787332767.0067642 | frequency_hz=254.6
- [2026-08-22 01:19:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332770.2574058 | source=vosk | rms=420 | updated_at=1787332769.2574804 | frequency_hz=254.6
- [2026-08-22 01:19:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332771.2569098 | source=vosk | rms=1202 | updated_at=1787332771.2569098 | frequency_hz=254.6
- [2026-08-22 01:19:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332772.008847 | source=vosk | rms=1205 | updated_at=1787332771.5074072 | frequency_hz=254.6
- [2026-08-22 01:19:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332773.0073192 | source=vosk | rms=1201 | updated_at=1787332773.0073192 | frequency_hz=254.6
- [2026-08-22 01:19:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332773.5071886 | source=vosk | rms=1201 | updated_at=1787332773.0073192 | frequency_hz=254.6
- [2026-08-22 01:19:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332773.7586064 | source=vosk | rms=1309 | updated_at=1787332773.7586064 | frequency_hz=254.6
- [2026-08-22 01:19:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332774.5074942 | source=vosk | rms=639 | updated_at=1787332774.0100567 | frequency_hz=254.6
- [2026-08-22 01:19:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332775.0077147 | source=vosk | rms=891 | updated_at=1787332775.0077147 | frequency_hz=254.6
- [2026-08-22 01:19:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332776.5072806 | source=vosk | rms=1202 | updated_at=1787332776.0092793 | frequency_hz=254.6
- [2026-08-22 01:19:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332777.5073495 | source=vosk | rms=851 | updated_at=1787332777.5073495 | frequency_hz=254.6
- [2026-08-22 01:19:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332778.507404 | source=vosk | rms=960 | updated_at=1787332778.0069957 | frequency_hz=254.6
- [2026-08-22 01:19:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332779.2884915 | source=vosk | rms=960 | updated_at=1787332778.0069957 | frequency_hz=254.6
- [2026-08-22 01:19:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332779.7583516 | source=vosk | rms=960 | updated_at=1787332778.0069957 | frequency_hz=254.6
- [2026-08-22 01:19:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332780.0077834 | source=vosk | rms=960 | updated_at=1787332778.0069957 | frequency_hz=254.6
- [2026-08-22 01:19:40] operator / voice_transcript_partial / voice: jewish
  meta: kind=partial | timestamp=1787332780.2882955 | source=vosk | rms=1202 | updated_at=1787332780.257739 | frequency_hz=254.6
- [2026-08-22 01:19:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332780.5074425 | source=vosk | rms=1206 | updated_at=1787332780.5074425 | frequency_hz=254.6
- [2026-08-22 01:19:41] operator / voice_transcript_final / voice: jewish
  meta: kind=final | timestamp=1787332781.102645 | source=final | rms=1206 | updated_at=1787332780.5074425 | frequency_hz=254.6
- [2026-08-22 01:19:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332781.1377215 | source=vosk | rms=1206 | updated_at=1787332780.5074425 | frequency_hz=254.6
- [2026-08-22 01:19:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332782.0069497 | source=vosk | rms=1206 | updated_at=1787332780.5074425 | frequency_hz=254.6
- [2026-08-22 01:19:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332782.5072417 | source=vosk | rms=1206 | updated_at=1787332780.5074425 | frequency_hz=254.6
- [2026-08-22 01:19:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332783.0076594 | source=vosk | rms=1206 | updated_at=1787332780.5074425 | frequency_hz=254.6
- [2026-08-22 01:19:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332785.2677379 | source=vosk | rms=1203 | updated_at=1787332784.7572846 | frequency_hz=254.6
- [2026-08-22 01:19:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332785.5162058 | source=vosk | rms=818 | updated_at=1787332785.5162058 | frequency_hz=254.6
- [2026-08-22 01:19:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332786.0117707 | source=vosk | rms=818 | updated_at=1787332785.5162058 | frequency_hz=254.6
- [2026-08-22 01:19:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332786.507187 | source=vosk | rms=994 | updated_at=1787332786.507187 | frequency_hz=254.6
- [2026-08-22 01:19:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332787.5068612 | source=vosk | rms=885 | updated_at=1787332787.0110633 | frequency_hz=254.6
- [2026-08-22 01:19:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332788.1171515 | source=vosk | rms=885 | updated_at=1787332787.0110633 | frequency_hz=254.6
- [2026-08-22 01:19:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332788.6172757 | source=vosk | rms=885 | updated_at=1787332787.0110633 | frequency_hz=254.6
- [2026-08-22 01:19:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332791.11951 | source=vosk | rms=1204 | updated_at=1787332791.11951 | frequency_hz=254.6
- [2026-08-22 01:19:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332791.8671 | source=vosk | rms=1203 | updated_at=1787332791.3686416 | frequency_hz=254.6
- [2026-08-22 01:19:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332793.866922 | source=vosk | rms=1203 | updated_at=1787332791.3686416 | frequency_hz=254.6
- [2026-08-22 01:19:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332794.367812 | source=vosk | rms=1203 | updated_at=1787332791.3686416 | frequency_hz=254.6
- [2026-08-22 01:19:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332795.117311 | source=vosk | rms=1065 | updated_at=1787332795.117311 | frequency_hz=254.6
- [2026-08-22 01:19:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332796.1173275 | source=vosk | rms=898 | updated_at=1787332795.617226 | frequency_hz=254.6
- [2026-08-22 01:19:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332797.3677719 | source=vosk | rms=898 | updated_at=1787332795.617226 | frequency_hz=254.6
- [2026-08-22 01:19:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332797.8689249 | source=vosk | rms=898 | updated_at=1787332795.617226 | frequency_hz=254.6
- [2026-08-22 01:19:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332798.117811 | source=vosk | rms=1202 | updated_at=1787332798.117811 | frequency_hz=254.6
- [2026-08-22 01:19:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332798.8673606 | source=vosk | rms=1025 | updated_at=1787332798.3732345 | frequency_hz=254.6
- [2026-08-22 01:19:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332799.8677583 | source=vosk | rms=1025 | updated_at=1787332798.3732345 | frequency_hz=254.6
- [2026-08-22 01:20:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332801.61726 | source=vosk | rms=1200 | updated_at=1787332801.117328 | frequency_hz=254.6
- [2026-08-22 01:20:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332802.1177015 | source=vosk | rms=1200 | updated_at=1787332801.117328 | frequency_hz=254.6
- [2026-08-22 01:20:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332802.6176484 | source=vosk | rms=1200 | updated_at=1787332801.117328 | frequency_hz=254.6
- [2026-08-22 01:20:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332802.867873 | source=vosk | rms=1200 | updated_at=1787332801.117328 | frequency_hz=254.6
- [2026-08-22 01:20:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332803.3764353 | source=vosk | rms=1200 | updated_at=1787332801.117328 | frequency_hz=254.6
- [2026-08-22 01:20:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332805.6833727 | source=vosk | rms=1200 | updated_at=1787332805.6823728 | frequency_hz=254.6
- [2026-08-22 01:20:05] operator / voice_transcript_partial / voice: please respond
  meta: kind=partial | timestamp=1787332805.7496064 | source=vosk | rms=1200 | updated_at=1787332805.6823728 | frequency_hz=254.6
- [2026-08-22 01:20:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332805.8809278 | source=vosk | rms=1202 | updated_at=1787332805.8809278 | frequency_hz=254.6
- [2026-08-22 01:20:05] operator / voice_transcript_partial / voice: as far as
  meta: kind=partial | timestamp=1787332805.9095814 | source=vosk | rms=1202 | updated_at=1787332805.8809278 | frequency_hz=254.6
- [2026-08-22 01:20:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332806.1172302 | source=vosk | rms=570 | updated_at=1787332806.1172302 | frequency_hz=254.6
- [2026-08-22 01:20:06] operator / voice_transcript_partial / voice: as far
  meta: kind=partial | timestamp=1787332806.1309135 | source=vosk | rms=570 | updated_at=1787332806.1172302 | frequency_hz=254.6
- [2026-08-22 01:20:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332806.6177905 | source=vosk | rms=570 | updated_at=1787332806.1172302 | frequency_hz=254.6
- [2026-08-22 01:20:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332809.1177526 | source=vosk | rms=1086 | updated_at=1787332809.1177526 | frequency_hz=254.6
- [2026-08-22 01:20:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332809.4016094 | source=vosk | rms=1200 | updated_at=1787332809.4016094 | frequency_hz=254.6
- [2026-08-22 01:20:09] operator / voice_transcript_final / voice: to go far
  meta: kind=final | timestamp=1787332809.6955013 | source=final | rms=1200 | updated_at=1787332809.4016094 | frequency_hz=254.6
- [2026-08-22 01:20:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332809.9916894 | source=vosk | rms=1200 | updated_at=1787332809.4016094 | frequency_hz=254.6
- [2026-08-22 01:20:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332809.9916894 | source=vosk | rms=862 | updated_at=1787332809.9916894 | frequency_hz=254.6
- [2026-08-22 01:20:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332811.1173038 | source=vosk | rms=862 | updated_at=1787332809.9916894 | frequency_hz=254.6
- [2026-08-22 01:20:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332811.7413173 | source=vosk | rms=597 | updated_at=1787332811.7413173 | frequency_hz=254.6
- [2026-08-22 01:20:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332812.6172373 | source=vosk | rms=975 | updated_at=1787332812.1488547 | frequency_hz=254.6
- [2026-08-22 01:20:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332812.9656312 | source=vosk | rms=1202 | updated_at=1787332812.9656312 | frequency_hz=254.6
- [2026-08-22 01:20:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332813.6171505 | source=vosk | rms=1202 | updated_at=1787332812.9656312 | frequency_hz=254.6
- [2026-08-22 01:20:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332813.8672354 | source=vosk | rms=1202 | updated_at=1787332813.8672354 | frequency_hz=254.6
- [2026-08-22 01:20:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332815.3680527 | source=vosk | rms=1202 | updated_at=1787332814.8673406 | frequency_hz=254.6
- [2026-08-22 01:20:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332817.117716 | source=vosk | rms=862 | updated_at=1787332817.117716 | frequency_hz=302.0
- [2026-08-22 01:20:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332818.1502438 | source=vosk | rms=859 | updated_at=1787332817.6174836 | frequency_hz=302.0
- [2026-08-22 01:20:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332820.129876 | source=vosk | rms=859 | updated_at=1787332817.6174836 | frequency_hz=302.0
- [2026-08-22 01:20:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332821.3672378 | source=vosk | rms=1021 | updated_at=1787332820.8688776 | frequency_hz=302.0
- [2026-08-22 01:20:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332822.118078 | source=vosk | rms=459 | updated_at=1787332822.118078 | frequency_hz=302.0
- [2026-08-22 01:20:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332822.61793 | source=vosk | rms=459 | updated_at=1787332822.118078 | frequency_hz=302.0
- [2026-08-22 01:20:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332824.8684442 | source=vosk | rms=459 | updated_at=1787332822.118078 | frequency_hz=302.0
- [2026-08-22 01:20:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332825.3694053 | source=vosk | rms=459 | updated_at=1787332822.118078 | frequency_hz=302.0
- [2026-08-22 01:20:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332828.8677144 | source=vosk | rms=282 | updated_at=1787332828.8677144 | frequency_hz=126.0
- [2026-08-22 01:20:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332829.8682346 | source=vosk | rms=930 | updated_at=1787332829.3676286 | frequency_hz=126.0
- [2026-08-22 01:20:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332830.1196995 | source=vosk | rms=413 | updated_at=1787332830.1196995 | frequency_hz=182.7
- [2026-08-22 01:20:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332831.1175196 | source=vosk | rms=896 | updated_at=1787332830.6180532 | frequency_hz=182.7
- [2026-08-22 01:20:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332833.617493 | source=vosk | rms=447 | updated_at=1787332833.617493 | frequency_hz=160.0
- [2026-08-22 01:20:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332834.618853 | source=vosk | rms=924 | updated_at=1787332834.1178956 | frequency_hz=160.0
- [2026-08-22 01:20:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332835.1175482 | source=vosk | rms=924 | updated_at=1787332834.1178956 | frequency_hz=160.0
- [2026-08-22 01:20:35] operator / voice_transcript_partial / voice: we've
  meta: kind=partial | timestamp=1787332835.427894 | source=vosk | rms=639 | updated_at=1787332835.3675072 | frequency_hz=160.0
- [2026-08-22 01:20:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332835.6173835 | source=vosk | rms=685 | updated_at=1787332835.6173835 | frequency_hz=160.0
- [2026-08-22 01:20:35] operator / voice_transcript_partial / voice: if this were
  meta: kind=partial | timestamp=1787332835.6464422 | source=vosk | rms=685 | updated_at=1787332835.6173835 | frequency_hz=160.0
- [2026-08-22 01:20:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332835.869551 | source=vosk | rms=685 | updated_at=1787332835.6173835 | frequency_hz=160.0
- [2026-08-22 01:20:35] operator / voice_transcript_partial / voice: if this what's
  meta: kind=partial | timestamp=1787332835.9458575 | source=vosk | rms=685 | updated_at=1787332835.6173835 | frequency_hz=160.0
- [2026-08-22 01:20:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332836.1214838 | source=vosk | rms=849 | updated_at=1787332836.1214838 | frequency_hz=160.0
- [2026-08-22 01:20:36] operator / voice_transcript_partial / voice: if this wasn't really
  meta: kind=partial | timestamp=1787332836.21146 | source=vosk | rms=849 | updated_at=1787332836.1214838 | frequency_hz=160.0
- [2026-08-22 01:20:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332836.367599 | source=vosk | rms=1203 | updated_at=1787332836.367599 | frequency_hz=160.0
- [2026-08-22 01:20:36] operator / voice_transcript_partial / voice: if the sorts and
  meta: kind=partial | timestamp=1787332836.4575849 | source=vosk | rms=1203 | updated_at=1787332836.367599 | frequency_hz=160.0
- [2026-08-22 01:20:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332836.6175535 | source=vosk | rms=1062 | updated_at=1787332836.6175535 | frequency_hz=160.0
- [2026-08-22 01:20:36] operator / voice_transcript_partial / voice: if this wasn't really
  meta: kind=partial | timestamp=1787332836.6701314 | source=vosk | rms=1062 | updated_at=1787332836.6175535 | frequency_hz=160.0
- [2026-08-22 01:20:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332837.1175308 | source=vosk | rms=1062 | updated_at=1787332836.6175535 | frequency_hz=160.0
- [2026-08-22 01:20:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332838.6173418 | source=vosk | rms=1203 | updated_at=1787332838.6173418 | frequency_hz=160.0
- [2026-08-22 01:20:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332839.1217556 | source=vosk | rms=1203 | updated_at=1787332838.6173418 | frequency_hz=160.0
- [2026-08-22 01:20:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332840.117835 | source=vosk | rms=531 | updated_at=1787332840.117835 | frequency_hz=164.0
- [2026-08-22 01:20:40] operator / voice_transcript_final / voice: if the sorts in three
  meta: kind=final | timestamp=1787332840.430431 | source=final | rms=531 | updated_at=1787332840.117835 | frequency_hz=164.0
- [2026-08-22 01:20:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332840.546826 | source=vosk | rms=531 | updated_at=1787332840.117835 | frequency_hz=164.0
- [2026-08-22 01:20:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332840.546826 | source=vosk | rms=1201 | updated_at=1787332840.546826 | frequency_hz=164.0
- [2026-08-22 01:20:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332841.3682303 | source=vosk | rms=1205 | updated_at=1787332840.780924 | frequency_hz=164.0
- [2026-08-22 01:20:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332841.6528616 | source=vosk | rms=1200 | updated_at=1787332841.6528616 | frequency_hz=253.6
- [2026-08-22 01:20:44] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1787332844.4162936 | source=vosk | rms=1343 | updated_at=1787332844.3860674 | frequency_hz=292.8
- [2026-08-22 01:20:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332844.6639857 | source=vosk | rms=1832 | updated_at=1787332844.6639857 | frequency_hz=292.8
- [2026-08-22 01:20:44] operator / voice_transcript_partial / voice: connect the
  meta: kind=partial | timestamp=1787332844.6835423 | source=vosk | rms=1832 | updated_at=1787332844.6639857 | frequency_hz=292.8
- [2026-08-22 01:20:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332844.868164 | source=vosk | rms=1200 | updated_at=1787332844.868164 | frequency_hz=292.8
- [2026-08-22 01:20:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332845.1177802 | source=vosk | rms=1201 | updated_at=1787332845.1177802 | frequency_hz=292.8
- [2026-08-22 01:20:45] operator / voice_transcript_partial / voice: connect the smarts and
  meta: kind=partial | timestamp=1787332845.1247938 | source=vosk | rms=1201 | updated_at=1787332845.1177802 | frequency_hz=292.8
- [2026-08-22 01:20:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332845.3719974 | source=vosk | rms=325 | updated_at=1787332845.3719974 | frequency_hz=292.8
- [2026-08-22 01:20:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332845.8674395 | source=vosk | rms=325 | updated_at=1787332845.3719974 | frequency_hz=292.8
- [2026-08-22 01:20:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332846.6177652 | source=vosk | rms=937 | updated_at=1787332846.6177652 | frequency_hz=268.7
- [2026-08-22 01:20:46] operator / voice_transcript_partial / voice: connect the smarts and three
  meta: kind=partial | timestamp=1787332846.6269968 | source=vosk | rms=937 | updated_at=1787332846.6177652 | frequency_hz=268.7
- [2026-08-22 01:20:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332847.1179368 | source=vosk | rms=505 | updated_at=1787332847.1179368 | frequency_hz=268.7
- [2026-08-22 01:20:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332847.3723829 | source=vosk | rms=641 | updated_at=1787332847.3723829 | frequency_hz=268.7
- [2026-08-22 01:20:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332847.6181157 | source=vosk | rms=264 | updated_at=1787332847.6181157 | frequency_hz=268.7
- [2026-08-22 01:20:47] operator / voice_transcript_final / voice: connect smart sentry
  meta: kind=final | timestamp=1787332847.8973312 | source=final | rms=264 | updated_at=1787332847.6181157 | frequency_hz=268.7
- [2026-08-22 01:20:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332848.099422 | source=vosk | rms=264 | updated_at=1787332847.6181157 | frequency_hz=268.7
- [2026-08-22 01:20:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332848.6182353 | source=vosk | rms=810 | updated_at=1787332848.6182353 | frequency_hz=268.7
- [2026-08-22 01:20:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332849.3677146 | source=vosk | rms=857 | updated_at=1787332848.8681302 | frequency_hz=268.7
- [2026-08-22 01:20:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332849.6179318 | source=vosk | rms=623 | updated_at=1787332849.6179318 | frequency_hz=268.7
- [2026-08-22 01:20:49] operator / voice_transcript_partial / voice: to the
  meta: kind=partial | timestamp=1787332849.6656032 | source=vosk | rms=623 | updated_at=1787332849.6179318 | frequency_hz=268.7
- [2026-08-22 01:20:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332849.8681579 | source=vosk | rms=612 | updated_at=1787332849.8681579 | frequency_hz=268.7
- [2026-08-22 01:20:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332850.1367946 | source=vosk | rms=636 | updated_at=1787332850.1367946 | frequency_hz=268.7
- [2026-08-22 01:20:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332850.6182237 | source=vosk | rms=717 | updated_at=1787332850.6182237 | frequency_hz=268.7
- [2026-08-22 01:20:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332851.1174974 | source=vosk | rms=717 | updated_at=1787332850.6182237 | frequency_hz=268.7
- [2026-08-22 01:20:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332853.8892221 | source=vosk | rms=451 | updated_at=1787332853.8892221 | frequency_hz=342.0
- [2026-08-22 01:20:54] operator / voice_transcript_final / voice: to the
  meta: kind=final | timestamp=1787332854.1820245 | source=final | rms=451 | updated_at=1787332853.8892221 | frequency_hz=342.0
- [2026-08-22 01:20:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332854.2223535 | source=vosk | rms=710 | updated_at=1787332854.2223535 | frequency_hz=342.0
- [2026-08-22 01:20:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332855.37199 | source=vosk | rms=551 | updated_at=1787332854.8678534 | frequency_hz=342.0
- [2026-08-22 01:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332856.3799996 | source=vosk | rms=551 | updated_at=1787332854.8678534 | frequency_hz=342.0
- [2026-08-22 01:20:56] operator / voice_transcript_partial / voice: the answer
  meta: kind=partial | timestamp=1787332856.4460192 | source=vosk | rms=551 | updated_at=1787332854.8678534 | frequency_hz=342.0
- [2026-08-22 01:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332856.627157 | source=vosk | rms=678 | updated_at=1787332856.627157 | frequency_hz=342.0
- [2026-08-22 01:20:56] operator / voice_transcript_partial / voice: the answer in
  meta: kind=partial | timestamp=1787332856.664963 | source=vosk | rms=678 | updated_at=1787332856.627157 | frequency_hz=342.0
- [2026-08-22 01:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332856.8681812 | source=vosk | rms=1204 | updated_at=1787332856.8681812 | frequency_hz=314.0
- [2026-08-22 01:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332857.3697543 | source=vosk | rms=1204 | updated_at=1787332856.8681812 | frequency_hz=314.0
- [2026-08-22 01:20:57] operator / voice_transcript_final / voice: the answer
  meta: kind=final | timestamp=1787332857.5691884 | source=final | rms=1204 | updated_at=1787332856.8681812 | frequency_hz=314.0
- [2026-08-22 01:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332857.6191308 | source=vosk | rms=1201 | updated_at=1787332857.6191308 | frequency_hz=335.0
- [2026-08-22 01:20:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332859.8682141 | source=vosk | rms=1202 | updated_at=1787332859.3677897 | frequency_hz=345.1
- [2026-08-22 01:21:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332861.6182432 | source=vosk | rms=1205 | updated_at=1787332861.6182432 | frequency_hz=345.1
- [2026-08-22 01:21:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332862.4051402 | source=vosk | rms=1200 | updated_at=1787332861.868174 | frequency_hz=345.1
- [2026-08-22 01:21:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332863.8683245 | source=vosk | rms=1201 | updated_at=1787332863.8683245 | frequency_hz=345.1
- [2026-08-22 01:21:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332864.617931 | source=vosk | rms=1205 | updated_at=1787332864.1176937 | frequency_hz=345.1
- [2026-08-22 01:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332867.3483193 | source=vosk | rms=1121 | updated_at=1787332867.3483193 | frequency_hz=268.0
- [2026-08-22 01:21:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332868.0984201 | source=vosk | rms=1174 | updated_at=1787332867.5992024 | frequency_hz=268.0
- [2026-08-22 01:21:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332869.3700426 | source=vosk | rms=1202 | updated_at=1787332869.3700426 | frequency_hz=268.0
- [2026-08-22 01:21:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332870.0973027 | source=vosk | rms=1203 | updated_at=1787332869.605275 | frequency_hz=268.0
- [2026-08-22 01:21:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332870.849232 | source=vosk | rms=990 | updated_at=1787332870.849232 | frequency_hz=268.0
- [2026-08-22 01:21:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332871.9681287 | source=vosk | rms=1204 | updated_at=1787332871.097586 | frequency_hz=268.0
- [2026-08-22 01:21:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332872.6141999 | source=vosk | rms=1202 | updated_at=1787332872.6141999 | frequency_hz=268.0
- [2026-08-22 01:21:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332873.3480012 | source=vosk | rms=1202 | updated_at=1787332872.848495 | frequency_hz=268.0
- [2026-08-22 01:21:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332873.8495338 | source=vosk | rms=1204 | updated_at=1787332873.8495338 | frequency_hz=268.0
- [2026-08-22 01:21:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332874.5983875 | source=vosk | rms=1203 | updated_at=1787332874.1391563 | frequency_hz=268.0
- [2026-08-22 01:21:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332875.3601174 | source=vosk | rms=774 | updated_at=1787332875.3601174 | frequency_hz=268.0
- [2026-08-22 01:21:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332876.0981493 | source=vosk | rms=1070 | updated_at=1787332875.5978637 | frequency_hz=268.0
- [2026-08-22 01:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332880.6127107 | source=vosk | rms=1205 | updated_at=1787332880.6127107 | frequency_hz=384.0
- [2026-08-22 01:21:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332881.607951 | source=vosk | rms=994 | updated_at=1787332881.1081674 | frequency_hz=384.0
- [2026-08-22 01:21:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332883.8611224 | source=vosk | rms=1204 | updated_at=1787332883.8611224 | frequency_hz=384.0
- [2026-08-22 01:21:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332884.8577616 | source=vosk | rms=1126 | updated_at=1787332884.3577967 | frequency_hz=384.0
- [2026-08-22 01:21:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332885.3611624 | source=vosk | rms=1201 | updated_at=1787332885.3611624 | frequency_hz=384.0
- [2026-08-22 01:21:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332886.6074564 | source=vosk | rms=631 | updated_at=1787332886.1085277 | frequency_hz=384.0
- [2026-08-22 01:21:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332890.8694177 | source=vosk | rms=1201 | updated_at=1787332890.8694177 | frequency_hz=384.0
- [2026-08-22 01:21:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332891.9794455 | source=vosk | rms=1202 | updated_at=1787332891.107781 | frequency_hz=384.0
- [2026-08-22 01:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332893.108512 | source=vosk | rms=1200 | updated_at=1787332893.108512 | frequency_hz=384.0
- [2026-08-22 01:21:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332894.8588595 | source=vosk | rms=531 | updated_at=1787332894.3880615 | frequency_hz=384.0
- [2026-08-22 01:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332896.6102467 | source=vosk | rms=1202 | updated_at=1787332896.6102467 | frequency_hz=384.0
- [2026-08-22 01:21:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332899.108727 | source=vosk | rms=1204 | updated_at=1787332898.1082737 | frequency_hz=384.0
- [2026-08-22 01:21:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332899.8602307 | source=vosk | rms=331 | updated_at=1787332899.8602307 | frequency_hz=384.0
- [2026-08-22 01:21:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332901.1090486 | source=vosk | rms=1202 | updated_at=1787332900.3912349 | frequency_hz=384.0
- [2026-08-22 01:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332902.8849845 | source=vosk | rms=1203 | updated_at=1787332902.8849845 | frequency_hz=384.0
- [2026-08-22 01:21:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332903.609463 | source=vosk | rms=1203 | updated_at=1787332903.1084948 | frequency_hz=384.0
- [2026-08-22 01:21:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332905.3579757 | source=vosk | rms=1201 | updated_at=1787332905.3579757 | frequency_hz=384.0
- [2026-08-22 01:21:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332906.3578012 | source=vosk | rms=1083 | updated_at=1787332905.8619316 | frequency_hz=384.0
- [2026-08-22 01:21:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332908.3577766 | source=vosk | rms=834 | updated_at=1787332908.3577766 | frequency_hz=384.0
- [2026-08-22 01:21:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332909.1085098 | source=vosk | rms=1203 | updated_at=1787332908.6076164 | frequency_hz=384.0
- [2026-08-22 01:21:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332911.1086957 | source=vosk | rms=1201 | updated_at=1787332911.1086957 | frequency_hz=384.0
- [2026-08-22 01:21:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332911.8586552 | source=vosk | rms=1203 | updated_at=1787332911.3582232 | frequency_hz=384.0
- [2026-08-22 01:21:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332915.1079714 | source=vosk | rms=1163 | updated_at=1787332915.1079714 | frequency_hz=266.0
- [2026-08-22 01:21:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332916.107824 | source=vosk | rms=1206 | updated_at=1787332915.614455 | frequency_hz=266.0
- [2026-08-22 01:22:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332921.8622935 | source=vosk | rms=1201 | updated_at=1787332921.8622935 | frequency_hz=266.0
- [2026-08-22 01:22:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332922.6095955 | source=vosk | rms=1202 | updated_at=1787332922.108438 | frequency_hz=266.0
- [2026-08-22 01:22:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332924.8587115 | source=vosk | rms=931 | updated_at=1787332924.8587115 | frequency_hz=266.0
- [2026-08-22 01:22:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332925.608824 | source=vosk | rms=1017 | updated_at=1787332925.1078827 | frequency_hz=266.0
- [2026-08-22 01:22:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332927.1118147 | source=vosk | rms=1203 | updated_at=1787332927.1118147 | frequency_hz=266.0
- [2026-08-22 01:22:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332927.8578925 | source=vosk | rms=1200 | updated_at=1787332927.3616157 | frequency_hz=266.0
- [2026-08-22 01:22:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332934.3585253 | source=vosk | rms=659 | updated_at=1787332934.3585253 | frequency_hz=160.0
- [2026-08-22 01:22:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332935.358746 | source=vosk | rms=1205 | updated_at=1787332934.8588488 | frequency_hz=160.0
- [2026-08-22 01:22:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332939.8597553 | source=vosk | rms=1205 | updated_at=1787332934.8588488 | frequency_hz=160.0
- [2026-08-22 01:22:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332940.3587108 | source=vosk | rms=1205 | updated_at=1787332934.8588488 | frequency_hz=160.0
- [2026-08-22 01:22:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332942.1807792 | source=vosk | rms=231 | updated_at=1787332942.1807792 | frequency_hz=160.0
- [2026-08-22 01:22:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332943.1087356 | source=vosk | rms=231 | updated_at=1787332942.1807792 | frequency_hz=160.0
- [2026-08-22 01:22:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332943.6088052 | source=vosk | rms=168 | updated_at=1787332943.6088052 | frequency_hz=160.0
- [2026-08-22 01:22:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332944.8588796 | source=vosk | rms=1202 | updated_at=1787332944.1082902 | frequency_hz=160.0
- [2026-08-22 01:22:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332947.6082082 | source=vosk | rms=374 | updated_at=1787332947.6082082 | frequency_hz=160.0
- [2026-08-22 01:22:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332948.1082642 | source=vosk | rms=374 | updated_at=1787332947.6082082 | frequency_hz=160.0
- [2026-08-22 01:22:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332949.1088383 | source=vosk | rms=1204 | updated_at=1787332949.1088383 | frequency_hz=160.0
- [2026-08-22 01:22:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332949.8582232 | source=vosk | rms=1202 | updated_at=1787332949.35873 | frequency_hz=160.0
- [2026-08-22 01:22:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332951.1147351 | source=vosk | rms=1203 | updated_at=1787332951.1147351 | frequency_hz=160.0
- [2026-08-22 01:22:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332951.8597293 | source=vosk | rms=164 | updated_at=1787332951.358466 | frequency_hz=174.0
- [2026-08-22 01:22:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332955.0114298 | source=vosk | rms=1203 | updated_at=1787332955.0114298 | frequency_hz=174.0
- [2026-08-22 01:22:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332955.6081293 | source=vosk | rms=1200 | updated_at=1787332955.108785 | frequency_hz=174.0
- [2026-08-22 01:22:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332958.8584166 | source=vosk | rms=204 | updated_at=1787332958.8584166 | frequency_hz=174.0
- [2026-08-22 01:22:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332959.3587072 | source=vosk | rms=204 | updated_at=1787332958.8584166 | frequency_hz=174.0
- [2026-08-22 01:22:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332959.858927 | source=vosk | rms=253 | updated_at=1787332959.858927 | frequency_hz=174.0
- [2026-08-22 01:22:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332961.8710735 | source=vosk | rms=254 | updated_at=1787332961.3696465 | frequency_hz=174.0
- [2026-08-22 01:22:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332962.1082268 | source=vosk | rms=254 | updated_at=1787332961.3696465 | frequency_hz=174.0
- [2026-08-22 01:22:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332966.209105 | source=vosk | rms=212 | updated_at=1787332965.358889 | frequency_hz=174.0
- [2026-08-22 01:22:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332967.358489 | source=vosk | rms=1128 | updated_at=1787332967.358489 | frequency_hz=174.0
- [2026-08-22 01:22:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332968.8581524 | source=vosk | rms=1205 | updated_at=1787332968.108672 | frequency_hz=174.0
- [2026-08-22 01:22:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332972.9562583 | source=vosk | rms=294 | updated_at=1787332972.9562583 | frequency_hz=174.0
- [2026-08-22 01:22:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332974.8583639 | source=vosk | rms=814 | updated_at=1787332974.2355065 | frequency_hz=174.0
- [2026-08-22 01:22:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332975.1096337 | source=vosk | rms=369 | updated_at=1787332975.1096337 | frequency_hz=174.0
- [2026-08-22 01:22:55] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1787332975.9041042 | source=vosk | rms=220 | updated_at=1787332975.6090467 | frequency_hz=174.0
- [2026-08-22 01:22:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332976.1101556 | source=vosk | rms=220 | updated_at=1787332975.6090467 | frequency_hz=174.0
- [2026-08-22 01:22:56] operator / voice_transcript_partial / voice: to go
  meta: kind=partial | timestamp=1787332976.1842752 | source=vosk | rms=220 | updated_at=1787332975.6090467 | frequency_hz=174.0
- [2026-08-22 01:22:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332976.3582315 | source=vosk | rms=220 | updated_at=1787332975.6090467 | frequency_hz=174.0
- [2026-08-22 01:22:56] operator / voice_transcript_partial / voice: to go to
  meta: kind=partial | timestamp=1787332976.4024339 | source=vosk | rms=220 | updated_at=1787332975.6090467 | frequency_hz=174.0
- [2026-08-22 01:22:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332976.8583689 | source=vosk | rms=220 | updated_at=1787332975.6090467 | frequency_hz=174.0
- [2026-08-22 01:22:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332977.3608434 | source=vosk | rms=1168 | updated_at=1787332977.3608434 | frequency_hz=174.0
- [2026-08-22 01:22:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332977.6089733 | source=vosk | rms=1078 | updated_at=1787332977.6089733 | frequency_hz=174.0
- [2026-08-22 01:22:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332977.8664997 | source=vosk | rms=388 | updated_at=1787332977.8664997 | frequency_hz=174.0
- [2026-08-22 01:22:58] operator / voice_transcript_final / voice: to go to
  meta: kind=final | timestamp=1787332978.155915 | source=final | rms=388 | updated_at=1787332977.8664997 | frequency_hz=174.0
- [2026-08-22 01:22:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332978.3999114 | source=vosk | rms=388 | updated_at=1787332977.8664997 | frequency_hz=174.0
- [2026-08-22 01:22:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332978.3999114 | source=vosk | rms=388 | updated_at=1787332977.8664997 | frequency_hz=174.0
- [2026-08-22 01:22:58] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1787332978.4301107 | source=vosk | rms=388 | updated_at=1787332977.8664997 | frequency_hz=174.0
- [2026-08-22 01:22:58] operator / voice_transcript_partial / voice: it got
  meta: kind=partial | timestamp=1787332978.446802 | source=vosk | rms=388 | updated_at=1787332977.8664997 | frequency_hz=174.0
- [2026-08-22 01:22:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332978.6084206 | source=vosk | rms=263 | updated_at=1787332978.6084206 | frequency_hz=174.0
- [2026-08-22 01:22:58] operator / voice_transcript_partial / voice: it got to
  meta: kind=partial | timestamp=1787332978.624441 | source=vosk | rms=263 | updated_at=1787332978.6084206 | frequency_hz=174.0
- [2026-08-22 01:22:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332978.858878 | source=vosk | rms=263 | updated_at=1787332978.6084206 | frequency_hz=174.0
- [2026-08-22 01:22:58] operator / voice_transcript_partial / voice: it got to pick
  meta: kind=partial | timestamp=1787332978.8918815 | source=vosk | rms=263 | updated_at=1787332978.6084206 | frequency_hz=174.0
- [2026-08-22 01:22:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332979.3587623 | source=vosk | rms=263 | updated_at=1787332978.6084206 | frequency_hz=174.0
- [2026-08-22 01:22:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332979.608293 | source=vosk | rms=1204 | updated_at=1787332979.608293 | frequency_hz=174.0
- [2026-08-22 01:22:59] operator / voice_transcript_partial / voice: it got
  meta: kind=partial | timestamp=1787332979.6928148 | source=vosk | rms=1204 | updated_at=1787332979.608293 | frequency_hz=174.0
- [2026-08-22 01:22:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332979.8591042 | source=vosk | rms=1204 | updated_at=1787332979.8591042 | frequency_hz=174.0
- [2026-08-22 01:23:00] operator / voice_transcript_final / voice: it got to pick out
  meta: kind=final | timestamp=1787332980.221198 | source=final | rms=1204 | updated_at=1787332979.8591042 | frequency_hz=174.0
- [2026-08-22 01:23:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332980.331512 | source=vosk | rms=1204 | updated_at=1787332979.8591042 | frequency_hz=174.0
- [2026-08-22 01:23:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332980.3325143 | source=vosk | rms=1172 | updated_at=1787332980.331512 | frequency_hz=174.0
- [2026-08-22 01:23:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332981.8698997 | source=vosk | rms=326 | updated_at=1787332980.6086085 | frequency_hz=174.0
- [2026-08-22 01:23:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332983.3589766 | source=vosk | rms=326 | updated_at=1787332980.6086085 | frequency_hz=174.0
- [2026-08-22 01:23:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332983.85903 | source=vosk | rms=326 | updated_at=1787332980.6086085 | frequency_hz=174.0
- [2026-08-22 01:23:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332984.3590229 | source=vosk | rms=1200 | updated_at=1787332984.3590229 | frequency_hz=174.0
- [2026-08-22 01:23:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332985.3591595 | source=vosk | rms=787 | updated_at=1787332984.8587968 | frequency_hz=174.0
- [2026-08-22 01:23:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332985.6088567 | source=vosk | rms=384 | updated_at=1787332985.6088567 | frequency_hz=174.0
- [2026-08-22 01:23:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332986.6088045 | source=vosk | rms=1202 | updated_at=1787332986.108572 | frequency_hz=174.0
- [2026-08-22 01:23:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332986.8588507 | source=vosk | rms=1032 | updated_at=1787332986.8588507 | frequency_hz=174.0
- [2026-08-22 01:23:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332988.1103477 | source=vosk | rms=885 | updated_at=1787332987.1160452 | frequency_hz=174.0
- [2026-08-22 01:23:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332990.1091166 | source=vosk | rms=885 | updated_at=1787332987.1160452 | frequency_hz=174.0
- [2026-08-22 01:23:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332990.6083102 | source=vosk | rms=885 | updated_at=1787332987.1160452 | frequency_hz=174.0
- [2026-08-22 01:23:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332992.6091585 | source=vosk | rms=752 | updated_at=1787332992.6091585 | frequency_hz=174.0
- [2026-08-22 01:23:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332993.3587413 | source=vosk | rms=1203 | updated_at=1787332992.8582938 | frequency_hz=174.0
- [2026-08-22 01:23:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332995.1091356 | source=vosk | rms=1203 | updated_at=1787332992.8582938 | frequency_hz=174.0
- [2026-08-22 01:23:15] operator / voice_transcript_final / voice: or
  meta: kind=final | timestamp=1787332995.323408 | source=final | rms=1203 | updated_at=1787332992.8582938 | frequency_hz=174.0
- [2026-08-22 01:23:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787332995.811277 | source=vosk | rms=1203 | updated_at=1787332992.8582938 | frequency_hz=174.0
- [2026-08-22 01:23:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787332999.3590372 | source=vosk | rms=1203 | updated_at=1787332999.3590372 | frequency_hz=338.0
- [2026-08-22 01:23:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333000.3588066 | source=vosk | rms=1204 | updated_at=1787332999.86715 | frequency_hz=338.0
- [2026-08-22 01:23:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333000.6087852 | source=vosk | rms=1204 | updated_at=1787332999.86715 | frequency_hz=338.0
- [2026-08-22 01:23:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333001.16334 | source=vosk | rms=1204 | updated_at=1787332999.86715 | frequency_hz=338.0
- [2026-08-22 01:23:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333001.3607004 | source=vosk | rms=606 | updated_at=1787333001.3607004 | frequency_hz=338.0
- [2026-08-22 01:23:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333002.1108828 | source=vosk | rms=606 | updated_at=1787333001.3607004 | frequency_hz=338.0
- [2026-08-22 01:23:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333002.608612 | source=vosk | rms=766 | updated_at=1787333002.608612 | frequency_hz=338.0
- [2026-08-22 01:23:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333003.6089244 | source=vosk | rms=1206 | updated_at=1787333003.1154807 | frequency_hz=338.0
- [2026-08-22 01:23:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333004.6091542 | source=vosk | rms=754 | updated_at=1787333004.6091542 | frequency_hz=338.0
- [2026-08-22 01:23:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333005.8587382 | source=vosk | rms=1191 | updated_at=1787333005.3647301 | frequency_hz=338.0
- [2026-08-22 01:23:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333007.6084034 | source=vosk | rms=367 | updated_at=1787333007.6084034 | frequency_hz=338.0
- [2026-08-22 01:23:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333008.6086097 | source=vosk | rms=1202 | updated_at=1787333008.1097572 | frequency_hz=338.0
- [2026-08-22 01:23:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333015.9889717 | source=vosk | rms=1204 | updated_at=1787333015.9889717 | frequency_hz=338.0
- [2026-08-22 01:23:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333016.73926 | source=vosk | rms=1205 | updated_at=1787333016.2387345 | frequency_hz=338.0
- [2026-08-22 01:23:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333021.4897878 | source=vosk | rms=301 | updated_at=1787333021.4882374 | frequency_hz=338.0
- [2026-08-22 01:23:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333021.9892287 | source=vosk | rms=301 | updated_at=1787333021.4882374 | frequency_hz=338.0
- [2026-08-22 01:23:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333022.2392316 | source=vosk | rms=286 | updated_at=1787333022.2392316 | frequency_hz=338.0
- [2026-08-22 01:23:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333023.596985 | source=vosk | rms=327 | updated_at=1787333022.739242 | frequency_hz=338.0
- [2026-08-22 01:23:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333023.8389916 | source=vosk | rms=649 | updated_at=1787333023.8389916 | frequency_hz=338.0
- [2026-08-22 01:23:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333026.6492171 | source=vosk | rms=1204 | updated_at=1787333026.1503775 | frequency_hz=338.0
- [2026-08-22 01:23:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333027.3993623 | source=vosk | rms=743 | updated_at=1787333027.3993623 | frequency_hz=338.0
- [2026-08-22 01:23:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333028.3994071 | source=vosk | rms=1176 | updated_at=1787333027.649552 | frequency_hz=338.0
- [2026-08-22 01:23:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333030.6490257 | source=vosk | rms=259 | updated_at=1787333030.6490257 | frequency_hz=338.0
- [2026-08-22 01:23:51] operator / voice_transcript_partial / voice: it's made explicit
  meta: kind=partial | timestamp=1787333031.2081192 | source=vosk | rms=566 | updated_at=1787333031.1490436 | frequency_hz=338.0
- [2026-08-22 01:23:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333031.399112 | source=vosk | rms=566 | updated_at=1787333031.1490436 | frequency_hz=338.0
- [2026-08-22 01:23:51] operator / voice_transcript_partial / voice: sweet expressed
  meta: kind=partial | timestamp=1787333031.4257407 | source=vosk | rms=566 | updated_at=1787333031.1490436 | frequency_hz=338.0
- [2026-08-22 01:23:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333031.6488338 | source=vosk | rms=467 | updated_at=1787333031.6488338 | frequency_hz=338.0
- [2026-08-22 01:23:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333031.898849 | source=vosk | rms=273 | updated_at=1787333031.898849 | frequency_hz=338.0
- [2026-08-22 01:23:51] operator / voice_transcript_partial / voice: sweet expressed skepticism
  meta: kind=partial | timestamp=1787333031.915935 | source=vosk | rms=273 | updated_at=1787333031.898849 | frequency_hz=338.0
- [2026-08-22 01:23:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333032.3987925 | source=vosk | rms=273 | updated_at=1787333031.898849 | frequency_hz=338.0
- [2026-08-22 01:23:52] operator / voice_transcript_final / voice: sweet expressed
  meta: kind=final | timestamp=1787333032.6183262 | source=final | rms=273 | updated_at=1787333031.898849 | frequency_hz=338.0
- [2026-08-22 01:23:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333033.597134 | source=vosk | rms=273 | updated_at=1787333031.898849 | frequency_hz=338.0
- [2026-08-22 01:23:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333033.597134 | source=vosk | rms=273 | updated_at=1787333031.898849 | frequency_hz=338.0
- [2026-08-22 01:23:53] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1787333033.8686259 | source=vosk | rms=1204 | updated_at=1787333033.8395443 | frequency_hz=338.0
- [2026-08-22 01:23:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333034.1520038 | source=vosk | rms=1201 | updated_at=1787333034.1520038 | frequency_hz=338.0
- [2026-08-22 01:23:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333034.340245 | source=vosk | rms=1004 | updated_at=1787333034.340245 | frequency_hz=338.0
- [2026-08-22 01:23:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333034.5888565 | source=vosk | rms=237 | updated_at=1787333034.5888565 | frequency_hz=338.0
- [2026-08-22 01:23:54] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1787333034.7692273 | source=final | rms=237 | updated_at=1787333034.5888565 | frequency_hz=338.0
- [2026-08-22 01:23:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333035.0891612 | source=vosk | rms=237 | updated_at=1787333034.5888565 | frequency_hz=338.0
- [2026-08-22 01:23:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333035.58918 | source=vosk | rms=237 | updated_at=1787333034.5888565 | frequency_hz=338.0
- [2026-08-22 01:23:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333036.088892 | source=vosk | rms=255 | updated_at=1787333036.088892 | frequency_hz=338.0
- [2026-08-22 01:23:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333037.339133 | source=vosk | rms=472 | updated_at=1787333036.590556 | frequency_hz=338.0
- [2026-08-22 01:23:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333037.838962 | source=vosk | rms=1204 | updated_at=1787333037.838962 | frequency_hz=338.0
- [2026-08-22 01:23:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333038.8386505 | source=vosk | rms=793 | updated_at=1787333038.3494415 | frequency_hz=338.0
- [2026-08-22 01:23:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333039.093395 | source=vosk | rms=793 | updated_at=1787333038.3494415 | frequency_hz=338.0
- [2026-08-22 01:23:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333039.5924718 | source=vosk | rms=793 | updated_at=1787333038.3494415 | frequency_hz=338.0
- [2026-08-22 01:23:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333039.8386793 | source=vosk | rms=1206 | updated_at=1787333039.8386793 | frequency_hz=338.0
- [2026-08-22 01:24:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333040.8468826 | source=vosk | rms=1150 | updated_at=1787333040.3652394 | frequency_hz=338.0
- [2026-08-22 01:24:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333041.5886648 | source=vosk | rms=1150 | updated_at=1787333040.3652394 | frequency_hz=338.0
- [2026-08-22 01:24:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333042.6378257 | source=vosk | rms=1150 | updated_at=1787333040.3652394 | frequency_hz=338.0
- [2026-08-22 01:24:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333042.8791013 | source=vosk | rms=315 | updated_at=1787333042.8791013 | frequency_hz=338.0
- [2026-08-22 01:24:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333044.6302893 | source=vosk | rms=231 | updated_at=1787333043.8792195 | frequency_hz=338.0
- [2026-08-22 01:24:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333044.87904 | source=vosk | rms=1202 | updated_at=1787333044.87904 | frequency_hz=338.0
- [2026-08-22 01:24:05] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1787333045.3476508 | source=final | rms=1202 | updated_at=1787333044.87904 | frequency_hz=338.0
- [2026-08-22 01:24:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333045.382795 | source=vosk | rms=1202 | updated_at=1787333044.87904 | frequency_hz=338.0
- [2026-08-22 01:24:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333045.382795 | source=vosk | rms=1200 | updated_at=1787333045.382795 | frequency_hz=338.0
- [2026-08-22 01:24:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333046.642976 | source=vosk | rms=646 | updated_at=1787333046.1291835 | frequency_hz=338.0
- [2026-08-22 01:24:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333046.8790898 | source=vosk | rms=1203 | updated_at=1787333046.8790898 | frequency_hz=338.0
- [2026-08-22 01:24:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333047.882373 | source=vosk | rms=537 | updated_at=1787333047.3786628 | frequency_hz=338.0
- [2026-08-22 01:24:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333048.1293788 | source=vosk | rms=784 | updated_at=1787333048.1293788 | frequency_hz=338.0
- [2026-08-22 01:24:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333048.629396 | source=vosk | rms=784 | updated_at=1787333048.1293788 | frequency_hz=338.0
- [2026-08-22 01:24:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333049.6288762 | source=vosk | rms=1204 | updated_at=1787333049.6288762 | frequency_hz=338.0
- [2026-08-22 01:24:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333050.8793452 | source=vosk | rms=1206 | updated_at=1787333050.3857243 | frequency_hz=338.0
- [2026-08-22 01:24:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333054.12925 | source=vosk | rms=1206 | updated_at=1787333050.3857243 | frequency_hz=338.0
- [2026-08-22 01:24:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333054.630343 | source=vosk | rms=1206 | updated_at=1787333050.3857243 | frequency_hz=338.0
- [2026-08-22 01:24:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333055.1294103 | source=vosk | rms=1201 | updated_at=1787333055.1294103 | frequency_hz=364.0
- [2026-08-22 01:24:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333056.6304784 | source=vosk | rms=1205 | updated_at=1787333055.8792 | frequency_hz=364.0
- [2026-08-22 01:24:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333064.8796036 | source=vosk | rms=1204 | updated_at=1787333064.8796036 | frequency_hz=364.0
- [2026-08-22 01:24:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333065.6672468 | source=vosk | rms=1203 | updated_at=1787333065.129538 | frequency_hz=364.0
- [2026-08-22 01:24:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333066.8792593 | source=vosk | rms=1203 | updated_at=1787333066.8792593 | frequency_hz=364.0
- [2026-08-22 01:24:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333067.8796797 | source=vosk | rms=739 | updated_at=1787333067.3791595 | frequency_hz=364.0
- [2026-08-22 01:24:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333071.6303935 | source=vosk | rms=888 | updated_at=1787333071.6303935 | frequency_hz=364.0
- [2026-08-22 01:24:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333073.1289415 | source=vosk | rms=661 | updated_at=1787333072.1296806 | frequency_hz=364.0
- [2026-08-22 01:24:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333073.379633 | source=vosk | rms=661 | updated_at=1787333072.1296806 | frequency_hz=364.0
- [2026-08-22 01:24:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333074.8800988 | source=vosk | rms=322 | updated_at=1787333074.384989 | frequency_hz=364.0
- [2026-08-22 01:24:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333077.87987 | source=vosk | rms=1201 | updated_at=1787333077.87987 | frequency_hz=364.0
- [2026-08-22 01:24:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333078.9606614 | source=vosk | rms=582 | updated_at=1787333078.3794882 | frequency_hz=364.0
- [2026-08-22 01:24:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333081.8991928 | source=vosk | rms=1206 | updated_at=1787333081.8991928 | frequency_hz=364.0
- [2026-08-22 01:24:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333084.4004993 | source=vosk | rms=1203 | updated_at=1787333083.9291258 | frequency_hz=364.0
- [2026-08-22 01:24:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333084.6495717 | source=vosk | rms=211 | updated_at=1787333084.6495717 | frequency_hz=364.0
- [2026-08-22 01:24:45] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1787333085.3638103 | source=final | rms=255 | updated_at=1787333084.8992822 | frequency_hz=364.0
- [2026-08-22 01:24:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333085.5738735 | source=vosk | rms=255 | updated_at=1787333084.8992822 | frequency_hz=364.0
- [2026-08-22 01:24:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333087.3992891 | source=vosk | rms=255 | updated_at=1787333084.8992822 | frequency_hz=364.0
- [2026-08-22 01:24:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333087.8989918 | source=vosk | rms=255 | updated_at=1787333084.8992822 | frequency_hz=364.0
- [2026-08-22 01:24:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333090.398987 | source=vosk | rms=1202 | updated_at=1787333090.398987 | frequency_hz=364.0
- [2026-08-22 01:24:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333091.1975925 | source=vosk | rms=1201 | updated_at=1787333090.6497087 | frequency_hz=364.0
- [2026-08-22 01:24:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333092.6488807 | source=vosk | rms=581 | updated_at=1787333092.6488807 | frequency_hz=398.0
- [2026-08-22 01:24:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333093.9062376 | source=vosk | rms=1202 | updated_at=1787333093.399481 | frequency_hz=398.0
- [2026-08-22 01:24:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333097.098492 | source=vosk | rms=1203 | updated_at=1787333097.098492 | frequency_hz=398.0
- [2026-08-22 01:24:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333097.649592 | source=vosk | rms=1200 | updated_at=1787333097.1491957 | frequency_hz=398.0
- [2026-08-22 01:24:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333098.6493838 | source=vosk | rms=1201 | updated_at=1787333098.6493838 | frequency_hz=398.0
- [2026-08-22 01:25:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333100.1496172 | source=vosk | rms=812 | updated_at=1787333099.5692503 | frequency_hz=398.0
- [2026-08-22 01:25:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333100.6493623 | source=vosk | rms=1195 | updated_at=1787333100.6493623 | frequency_hz=398.0
- [2026-08-22 01:25:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333101.9019084 | source=vosk | rms=1205 | updated_at=1787333101.151257 | frequency_hz=398.0
- [2026-08-22 01:25:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333103.3997266 | source=vosk | rms=1200 | updated_at=1787333103.3997266 | frequency_hz=398.0
- [2026-08-22 01:25:05] operator / voice_transcript_partial / voice: please
  meta: kind=partial | timestamp=1787333105.9231503 | source=vosk | rms=1203 | updated_at=1787333105.901218 | frequency_hz=398.0
- [2026-08-22 01:25:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333106.1735356 | source=vosk | rms=1200 | updated_at=1787333106.1735356 | frequency_hz=398.0
- [2026-08-22 01:25:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333106.39913 | source=vosk | rms=816 | updated_at=1787333106.39913 | frequency_hz=398.0
- [2026-08-22 01:25:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333106.89913 | source=vosk | rms=816 | updated_at=1787333106.39913 | frequency_hz=398.0
- [2026-08-22 01:25:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333108.64923 | source=vosk | rms=701 | updated_at=1787333108.64923 | frequency_hz=398.0
- [2026-08-22 01:25:08] operator / voice_transcript_final / voice: please
  meta: kind=final | timestamp=1787333108.8586996 | source=final | rms=701 | updated_at=1787333108.64923 | frequency_hz=398.0
- [2026-08-22 01:25:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333108.8992486 | source=vosk | rms=1127 | updated_at=1787333108.8992486 | frequency_hz=398.0
- [2026-08-22 01:25:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333109.9000432 | source=vosk | rms=1127 | updated_at=1787333108.8992486 | frequency_hz=398.0
- [2026-08-22 01:25:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333110.649929 | source=vosk | rms=1201 | updated_at=1787333110.649929 | frequency_hz=398.0
- [2026-08-22 01:25:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333111.4080539 | source=vosk | rms=1201 | updated_at=1787333110.8992076 | frequency_hz=398.0
- [2026-08-22 01:25:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333117.8998249 | source=vosk | rms=1201 | updated_at=1787333117.8998249 | frequency_hz=398.0
- [2026-08-22 01:25:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333118.6498125 | source=vosk | rms=1200 | updated_at=1787333118.1496038 | frequency_hz=398.0
- [2026-08-22 01:25:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333119.1508348 | source=vosk | rms=759 | updated_at=1787333119.1508348 | frequency_hz=398.0
- [2026-08-22 01:25:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333119.9095948 | source=vosk | rms=1207 | updated_at=1787333119.4654417 | frequency_hz=398.0
- [2026-08-22 01:25:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333124.7996805 | source=vosk | rms=344 | updated_at=1787333124.7996805 | frequency_hz=398.0
- [2026-08-22 01:25:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333126.2998247 | source=vosk | rms=1204 | updated_at=1787333125.8148384 | frequency_hz=398.0
- [2026-08-22 01:25:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333128.7995834 | source=vosk | rms=986 | updated_at=1787333128.7995834 | frequency_hz=212.0
- [2026-08-22 01:25:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333129.8239007 | source=vosk | rms=1201 | updated_at=1787333129.374093 | frequency_hz=212.0
- [2026-08-22 01:25:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333131.049586 | source=vosk | rms=1201 | updated_at=1787333129.374093 | frequency_hz=212.0
- [2026-08-22 01:25:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333131.549786 | source=vosk | rms=1201 | updated_at=1787333129.374093 | frequency_hz=212.0
- [2026-08-22 01:25:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333132.0626264 | source=vosk | rms=1134 | updated_at=1787333132.0626264 | frequency_hz=212.0
- [2026-08-22 01:25:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333132.799216 | source=vosk | rms=487 | updated_at=1787333132.3044717 | frequency_hz=212.0
- [2026-08-22 01:25:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333134.0497468 | source=vosk | rms=801 | updated_at=1787333134.0497468 | frequency_hz=212.0
- [2026-08-22 01:25:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333135.2995794 | source=vosk | rms=347 | updated_at=1787333134.7994573 | frequency_hz=212.0
- [2026-08-22 01:25:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333137.3000925 | source=vosk | rms=1203 | updated_at=1787333137.3000925 | frequency_hz=212.0
- [2026-08-22 01:25:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333138.0502298 | source=vosk | rms=1204 | updated_at=1787333137.5500712 | frequency_hz=212.0
- [2026-08-22 01:25:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333145.1999366 | source=vosk | rms=1205 | updated_at=1787333145.1999366 | frequency_hz=212.0
- [2026-08-22 01:25:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333148.4496884 | source=vosk | rms=1204 | updated_at=1787333147.9508681 | frequency_hz=212.0
- [2026-08-22 01:25:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333151.950055 | source=vosk | rms=1204 | updated_at=1787333147.9508681 | frequency_hz=212.0
- [2026-08-22 01:25:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333152.4647462 | source=vosk | rms=1204 | updated_at=1787333147.9508681 | frequency_hz=212.0
- [2026-08-22 01:25:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333152.94958 | source=vosk | rms=1204 | updated_at=1787333147.9508681 | frequency_hz=212.0
- [2026-08-22 01:25:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333154.452288 | source=vosk | rms=1204 | updated_at=1787333147.9508681 | frequency_hz=212.0
- [2026-08-22 01:25:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333155.199404 | source=vosk | rms=1202 | updated_at=1787333155.199404 | frequency_hz=212.0
- [2026-08-22 01:25:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333155.9496777 | source=vosk | rms=1201 | updated_at=1787333155.450033 | frequency_hz=212.0
- [2026-08-22 01:25:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333156.200482 | source=vosk | rms=1204 | updated_at=1787333156.200482 | frequency_hz=212.0
- [2026-08-22 01:25:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333158.950207 | source=vosk | rms=1202 | updated_at=1787333158.4502046 | frequency_hz=212.0
- [2026-08-22 01:25:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333159.2020226 | source=vosk | rms=213 | updated_at=1787333159.2020226 | frequency_hz=212.0
- [2026-08-22 01:25:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333159.9538698 | source=vosk | rms=213 | updated_at=1787333159.2020226 | frequency_hz=212.0
- [2026-08-22 01:26:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333160.2011714 | source=vosk | rms=281 | updated_at=1787333160.2011714 | frequency_hz=212.0
- [2026-08-22 01:26:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333161.7002854 | source=vosk | rms=286 | updated_at=1787333161.1996858 | frequency_hz=212.0
- [2026-08-22 01:26:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333164.7017748 | source=vosk | rms=341 | updated_at=1787333164.7017748 | frequency_hz=212.0
- [2026-08-22 01:26:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333165.6328843 | source=vosk | rms=344 | updated_at=1787333165.2002091 | frequency_hz=212.0
- [2026-08-22 01:26:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333167.9549649 | source=vosk | rms=344 | updated_at=1787333165.2002091 | frequency_hz=212.0
- [2026-08-22 01:26:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333169.702581 | source=vosk | rms=1012 | updated_at=1787333169.156411 | frequency_hz=212.0
- [2026-08-22 01:26:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333170.205072 | source=vosk | rms=1012 | updated_at=1787333169.156411 | frequency_hz=212.0
- [2026-08-22 01:26:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333170.7003863 | source=vosk | rms=1012 | updated_at=1787333169.156411 | frequency_hz=212.0
- [2026-08-22 01:26:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333170.9503827 | source=vosk | rms=1203 | updated_at=1787333170.9503827 | frequency_hz=212.0
- [2026-08-22 01:26:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333171.6999702 | source=vosk | rms=1201 | updated_at=1787333171.199827 | frequency_hz=212.0
- [2026-08-22 01:26:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333172.1998026 | source=vosk | rms=1201 | updated_at=1787333171.199827 | frequency_hz=212.0
- [2026-08-22 01:26:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333172.700382 | source=vosk | rms=1201 | updated_at=1787333171.199827 | frequency_hz=212.0
- [2026-08-22 01:26:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333173.4503758 | source=vosk | rms=1087 | updated_at=1787333173.4503758 | frequency_hz=212.0
- [2026-08-22 01:26:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333174.4503796 | source=vosk | rms=1201 | updated_at=1787333173.9495418 | frequency_hz=212.0
- [2026-08-22 01:26:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333175.9502134 | source=vosk | rms=1203 | updated_at=1787333175.9502134 | frequency_hz=212.0
- [2026-08-22 01:26:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333176.6997046 | source=vosk | rms=1202 | updated_at=1787333176.1996675 | frequency_hz=212.0
- [2026-08-22 01:26:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333177.700145 | source=vosk | rms=319 | updated_at=1787333177.700145 | frequency_hz=212.0
- [2026-08-22 01:26:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333178.2000985 | source=vosk | rms=319 | updated_at=1787333177.700145 | frequency_hz=212.0
- [2026-08-22 01:26:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333178.9497075 | source=vosk | rms=1202 | updated_at=1787333178.9497075 | frequency_hz=212.0
- [2026-08-22 01:26:19] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1787333179.2203767 | source=vosk | rms=1202 | updated_at=1787333179.2012246 | frequency_hz=212.0
- [2026-08-22 01:26:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333179.700083 | source=vosk | rms=1202 | updated_at=1787333179.2012246 | frequency_hz=212.0
- [2026-08-22 01:26:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333180.700474 | source=vosk | rms=1204 | updated_at=1787333180.700474 | frequency_hz=212.0
- [2026-08-22 01:26:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333180.9825366 | source=vosk | rms=1203 | updated_at=1787333180.9825366 | frequency_hz=212.0
- [2026-08-22 01:26:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333181.2015624 | source=vosk | rms=1125 | updated_at=1787333181.2015624 | frequency_hz=212.0
- [2026-08-22 01:26:21] operator / voice_transcript_final / voice: two
  meta: kind=final | timestamp=1787333181.3939993 | source=final | rms=1125 | updated_at=1787333181.2015624 | frequency_hz=212.0
- [2026-08-22 01:26:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333181.700543 | source=vosk | rms=1125 | updated_at=1787333181.2015624 | frequency_hz=212.0
- [2026-08-22 01:26:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333183.7004707 | source=vosk | rms=448 | updated_at=1787333183.7004707 | frequency_hz=212.0
- [2026-08-22 01:26:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333184.1999683 | source=vosk | rms=448 | updated_at=1787333183.7004707 | frequency_hz=212.0
- [2026-08-22 01:26:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333190.62316 | source=vosk | rms=448 | updated_at=1787333183.7004707 | frequency_hz=212.0
- [2026-08-22 01:26:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333191.3735244 | source=vosk | rms=448 | updated_at=1787333183.7004707 | frequency_hz=212.0
- [2026-08-22 01:26:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333191.627231 | source=vosk | rms=448 | updated_at=1787333183.7004707 | frequency_hz=212.0
- [2026-08-22 01:26:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333192.8737457 | source=vosk | rms=1020 | updated_at=1787333192.4115841 | frequency_hz=212.0
- [2026-08-22 01:26:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333195.3733077 | source=vosk | rms=1020 | updated_at=1787333192.4115841 | frequency_hz=212.0
- [2026-08-22 01:26:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333196.6230922 | source=vosk | rms=1020 | updated_at=1787333192.4115841 | frequency_hz=212.0
- [2026-08-22 01:26:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333199.6238067 | source=vosk | rms=1204 | updated_at=1787333199.622807 | frequency_hz=212.0
- [2026-08-22 01:26:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333200.8729186 | source=vosk | rms=1200 | updated_at=1787333200.108986 | frequency_hz=212.0
- [2026-08-22 01:26:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333202.912025 | source=vosk | rms=602 | updated_at=1787333202.912025 | frequency_hz=212.0
- [2026-08-22 01:26:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333204.4220037 | source=vosk | rms=1201 | updated_at=1787333203.1621075 | frequency_hz=212.0
- [2026-08-22 01:26:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333211.4334888 | source=vosk | rms=599 | updated_at=1787333211.4334888 | frequency_hz=212.0
- [2026-08-22 01:26:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333215.18206 | source=vosk | rms=296 | updated_at=1787333214.6824183 | frequency_hz=212.0
- [2026-08-22 01:26:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333218.9233441 | source=vosk | rms=1204 | updated_at=1787333218.9233441 | frequency_hz=212.0
- [2026-08-22 01:26:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333219.9231222 | source=vosk | rms=543 | updated_at=1787333219.4234886 | frequency_hz=212.0
- [2026-08-22 01:27:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333221.923732 | source=vosk | rms=791 | updated_at=1787333221.923732 | frequency_hz=212.0
- [2026-08-22 01:27:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333224.934675 | source=vosk | rms=795 | updated_at=1787333224.183444 | frequency_hz=212.0
- [2026-08-22 01:27:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333225.1829507 | source=vosk | rms=795 | updated_at=1787333224.183444 | frequency_hz=212.0
- [2026-08-22 01:27:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333225.6844065 | source=vosk | rms=795 | updated_at=1787333224.183444 | frequency_hz=212.0
- [2026-08-22 01:27:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333232.184828 | source=vosk | rms=1200 | updated_at=1787333232.184828 | frequency_hz=212.0
- [2026-08-22 01:27:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333232.9336247 | source=vosk | rms=1200 | updated_at=1787333232.4329016 | frequency_hz=212.0
- [2026-08-22 01:27:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333233.9334142 | source=vosk | rms=1200 | updated_at=1787333233.9334142 | frequency_hz=212.0
- [2026-08-22 01:27:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333234.6829934 | source=vosk | rms=1204 | updated_at=1787333234.1829715 | frequency_hz=212.0
- [2026-08-22 01:27:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333244.184581 | source=vosk | rms=1204 | updated_at=1787333234.1829715 | frequency_hz=212.0
- [2026-08-22 01:27:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333244.6831262 | source=vosk | rms=1204 | updated_at=1787333234.1829715 | frequency_hz=212.0
- [2026-08-22 01:27:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333245.1838148 | source=vosk | rms=1204 | updated_at=1787333234.1829715 | frequency_hz=212.0
- [2026-08-22 01:27:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333247.377064 | source=vosk | rms=1202 | updated_at=1787333246.473606 | frequency_hz=212.0
- [2026-08-22 01:27:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333247.6271603 | source=vosk | rms=1202 | updated_at=1787333246.473606 | frequency_hz=212.0
- [2026-08-22 01:27:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333248.1288176 | source=vosk | rms=1202 | updated_at=1787333246.473606 | frequency_hz=212.0
- [2026-08-22 01:27:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333248.3775795 | source=vosk | rms=259 | updated_at=1787333248.3775795 | frequency_hz=212.0
- [2026-08-22 01:27:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333248.8778827 | source=vosk | rms=259 | updated_at=1787333248.3775795 | frequency_hz=212.0
- [2026-08-22 01:27:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333249.8773055 | source=vosk | rms=1169 | updated_at=1787333249.8773055 | frequency_hz=212.0
- [2026-08-22 01:27:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333251.1270742 | source=vosk | rms=1203 | updated_at=1787333250.6279883 | frequency_hz=212.0
- [2026-08-22 01:27:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333251.8771298 | source=vosk | rms=398 | updated_at=1787333251.8771298 | frequency_hz=212.0
- [2026-08-22 01:27:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333252.6277022 | source=vosk | rms=166 | updated_at=1787333252.1278949 | frequency_hz=212.0
- [2026-08-22 01:27:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333252.8778565 | source=vosk | rms=166 | updated_at=1787333252.1278949 | frequency_hz=212.0
- [2026-08-22 01:27:33] operator / voice_transcript_final / voice: but
  meta: kind=final | timestamp=1787333253.1203587 | source=final | rms=166 | updated_at=1787333252.1278949 | frequency_hz=212.0
- [2026-08-22 01:27:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333253.160108 | source=vosk | rms=166 | updated_at=1787333252.1278949 | frequency_hz=212.0
- [2026-08-22 01:27:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333253.627826 | source=vosk | rms=166 | updated_at=1787333252.1278949 | frequency_hz=212.0
- [2026-08-22 01:27:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333254.1489015 | source=vosk | rms=517 | updated_at=1787333254.1489015 | frequency_hz=212.0
- [2026-08-22 01:27:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333254.6273735 | source=vosk | rms=517 | updated_at=1787333254.1489015 | frequency_hz=212.0
- [2026-08-22 01:27:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333259.889412 | source=vosk | rms=1200 | updated_at=1787333259.8884094 | frequency_hz=212.0
- [2026-08-22 01:27:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333260.6291077 | source=vosk | rms=1200 | updated_at=1787333260.128202 | frequency_hz=212.0
- [2026-08-22 01:27:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333261.6274993 | source=vosk | rms=1202 | updated_at=1787333261.6274993 | frequency_hz=212.0
- [2026-08-22 01:27:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333262.7090933 | source=vosk | rms=1203 | updated_at=1787333262.1878633 | frequency_hz=212.0
- [2026-08-22 01:27:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333263.7068558 | source=vosk | rms=837 | updated_at=1787333263.7068558 | frequency_hz=212.0
- [2026-08-22 01:27:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333264.7057822 | source=vosk | rms=1200 | updated_at=1787333264.2056687 | frequency_hz=212.0
- [2026-08-22 01:27:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333272.4698834 | source=vosk | rms=1200 | updated_at=1787333264.2056687 | frequency_hz=212.0
- [2026-08-22 01:27:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333275.4555452 | source=vosk | rms=259 | updated_at=1787333274.95607 | frequency_hz=212.0
- [2026-08-22 01:27:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333276.4957306 | source=vosk | rms=424 | updated_at=1787333276.4957306 | frequency_hz=212.0
- [2026-08-22 01:27:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333277.955617 | source=vosk | rms=213 | updated_at=1787333277.4556875 | frequency_hz=212.0
- [2026-08-22 01:27:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333278.705521 | source=vosk | rms=213 | updated_at=1787333277.4556875 | frequency_hz=212.0
- [2026-08-22 01:28:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333281.2059095 | source=vosk | rms=908 | updated_at=1787333280.7060056 | frequency_hz=212.0
- [2026-08-22 01:28:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333283.4561503 | source=vosk | rms=359 | updated_at=1787333283.4561503 | frequency_hz=212.0
- [2026-08-22 01:28:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333284.2071366 | source=vosk | rms=238 | updated_at=1787333283.7058182 | frequency_hz=212.0
- [2026-08-22 01:28:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333285.7057922 | source=vosk | rms=286 | updated_at=1787333285.7057922 | frequency_hz=212.0
- [2026-08-22 01:28:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333286.212834 | source=vosk | rms=286 | updated_at=1787333285.7057922 | frequency_hz=212.0
- [2026-08-22 01:28:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333288.4640691 | source=vosk | rms=286 | updated_at=1787333285.7057922 | frequency_hz=212.0
- [2026-08-22 01:28:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333288.9880164 | source=vosk | rms=286 | updated_at=1787333285.7057922 | frequency_hz=212.0
- [2026-08-22 01:28:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333289.9561822 | source=vosk | rms=132 | updated_at=1787333289.9561822 | frequency_hz=212.0
- [2026-08-22 01:28:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333290.455698 | source=vosk | rms=132 | updated_at=1787333289.9561822 | frequency_hz=212.0
- [2026-08-22 01:28:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333291.2054243 | source=vosk | rms=1205 | updated_at=1787333291.2054243 | frequency_hz=212.0
- [2026-08-22 01:28:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333292.207228 | source=vosk | rms=1132 | updated_at=1787333291.7281702 | frequency_hz=212.0
- [2026-08-22 01:28:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333296.955439 | source=vosk | rms=175 | updated_at=1787333296.955439 | frequency_hz=212.0
- [2026-08-22 01:28:17] operator / voice_transcript_final / voice: specimens
  meta: kind=final | timestamp=1787333297.473399 | source=final | rms=175 | updated_at=1787333296.955439 | frequency_hz=212.0
- [2026-08-22 01:28:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333297.5070305 | source=vosk | rms=175 | updated_at=1787333296.955439 | frequency_hz=212.0
- [2026-08-22 01:28:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333303.864325 | source=vosk | rms=1202 | updated_at=1787333302.7118616 | frequency_hz=212.0
- [2026-08-22 01:28:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333308.4742155 | source=vosk | rms=204 | updated_at=1787333308.4742155 | frequency_hz=212.0
- [2026-08-22 01:28:28] operator / voice_transcript_final / voice: dogs
  meta: kind=final | timestamp=1787333308.9658267 | source=final | rms=204 | updated_at=1787333308.4742155 | frequency_hz=212.0
- [2026-08-22 01:28:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333308.9999118 | source=vosk | rms=204 | updated_at=1787333308.4742155 | frequency_hz=212.0
- [2026-08-22 01:28:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333309.223698 | source=vosk | rms=243 | updated_at=1787333309.223698 | frequency_hz=212.0
- [2026-08-22 01:28:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333309.7249765 | source=vosk | rms=243 | updated_at=1787333309.223698 | frequency_hz=212.0
- [2026-08-22 01:28:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333310.4739056 | source=vosk | rms=372 | updated_at=1787333310.4739056 | frequency_hz=212.0
- [2026-08-22 01:28:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333310.9742858 | source=vosk | rms=372 | updated_at=1787333310.4739056 | frequency_hz=212.0
- [2026-08-22 01:28:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333311.72142 | source=vosk | rms=372 | updated_at=1787333310.4739056 | frequency_hz=212.0
- [2026-08-22 01:28:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333312.7179844 | source=vosk | rms=372 | updated_at=1787333310.4739056 | frequency_hz=212.0
- [2026-08-22 01:28:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333315.2553296 | source=vosk | rms=372 | updated_at=1787333310.4739056 | frequency_hz=212.0
- [2026-08-22 01:28:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333318.695537 | source=vosk | rms=173 | updated_at=1787333317.2240005 | frequency_hz=212.0
- [2026-08-22 01:28:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333319.6954114 | source=vosk | rms=159 | updated_at=1787333319.6954114 | frequency_hz=212.0
- [2026-08-22 01:28:40] operator / voice_transcript_partial / voice: little by little
  meta: kind=partial | timestamp=1787333320.0017662 | source=vosk | rms=143 | updated_at=1787333319.9563591 | frequency_hz=212.0
- [2026-08-22 01:28:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333320.193708 | source=vosk | rms=175 | updated_at=1787333320.193708 | frequency_hz=212.0
- [2026-08-22 01:28:40] operator / voice_transcript_partial / voice: the to be able
  meta: kind=partial | timestamp=1787333320.237591 | source=vosk | rms=175 | updated_at=1787333320.193708 | frequency_hz=212.0
- [2026-08-22 01:28:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333320.8225152 | source=vosk | rms=259 | updated_at=1787333320.8225152 | frequency_hz=212.0
- [2026-08-22 01:28:40] operator / voice_transcript_partial / voice: little by little people
  meta: kind=partial | timestamp=1787333320.9171648 | source=vosk | rms=259 | updated_at=1787333320.8225152 | frequency_hz=212.0
- [2026-08-22 01:28:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333322.1220763 | source=vosk | rms=259 | updated_at=1787333320.8225152 | frequency_hz=212.0
- [2026-08-22 01:28:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333322.5744247 | source=vosk | rms=127 | updated_at=1787333322.5744247 | frequency_hz=212.0
- [2026-08-22 01:28:42] operator / voice_transcript_partial / voice: little by little paper was
  meta: kind=partial | timestamp=1787333322.6348715 | source=vosk | rms=127 | updated_at=1787333322.5744247 | frequency_hz=212.0
- [2026-08-22 01:28:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333322.8250458 | source=vosk | rms=174 | updated_at=1787333322.8250458 | frequency_hz=212.0
- [2026-08-22 01:28:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333323.074702 | source=vosk | rms=216 | updated_at=1787333323.074702 | frequency_hz=212.0
- [2026-08-22 01:28:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333323.679467 | source=vosk | rms=411 | updated_at=1787333323.679467 | frequency_hz=212.0
- [2026-08-22 01:28:44] operator / voice_transcript_final / voice: little by little paper was
  meta: kind=final | timestamp=1787333324.0024164 | source=final | rms=411 | updated_at=1787333323.679467 | frequency_hz=212.0
- [2026-08-22 01:28:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333324.145521 | source=vosk | rms=411 | updated_at=1787333323.679467 | frequency_hz=212.0
- [2026-08-22 01:28:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333324.1465206 | source=vosk | rms=158 | updated_at=1787333324.1465206 | frequency_hz=212.0
- [2026-08-22 01:28:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333325.0048769 | source=vosk | rms=125 | updated_at=1787333324.4373424 | frequency_hz=212.0
- [2026-08-22 01:28:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333326.456365 | source=vosk | rms=153 | updated_at=1787333326.456365 | frequency_hz=212.0
- [2026-08-22 01:28:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333326.9858646 | source=vosk | rms=153 | updated_at=1787333326.456365 | frequency_hz=212.0
- [2026-08-22 01:28:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333328.3746324 | source=vosk | rms=160 | updated_at=1787333328.3746324 | frequency_hz=212.0
- [2026-08-22 01:28:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333329.2825096 | source=vosk | rms=160 | updated_at=1787333328.3746324 | frequency_hz=212.0
- [2026-08-22 01:28:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333334.4778612 | source=vosk | rms=149 | updated_at=1787333334.4778612 | frequency_hz=212.0
- [2026-08-22 01:28:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333337.2162242 | source=vosk | rms=134 | updated_at=1787333335.0043159 | frequency_hz=212.0
- [2026-08-22 01:28:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333338.0595121 | source=vosk | rms=134 | updated_at=1787333335.0043159 | frequency_hz=212.0
- [2026-08-22 01:28:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333338.5551174 | source=vosk | rms=134 | updated_at=1787333335.0043159 | frequency_hz=212.0
- [2026-08-22 01:28:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333339.8046799 | source=vosk | rms=1202 | updated_at=1787333339.8046799 | frequency_hz=212.0
- [2026-08-22 01:29:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333340.945207 | source=vosk | rms=1204 | updated_at=1787333340.4136593 | frequency_hz=212.0
- [2026-08-22 01:29:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333345.9458246 | source=vosk | rms=1200 | updated_at=1787333345.9446552 | frequency_hz=212.0
- [2026-08-22 01:29:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333346.9454231 | source=vosk | rms=650 | updated_at=1787333346.4453232 | frequency_hz=212.0
- [2026-08-22 01:29:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333350.695162 | source=vosk | rms=1203 | updated_at=1787333350.695162 | frequency_hz=212.0
- [2026-08-22 01:29:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333351.695377 | source=vosk | rms=819 | updated_at=1787333351.1956654 | frequency_hz=212.0
- [2026-08-22 01:29:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333354.0392804 | source=vosk | rms=1188 | updated_at=1787333354.0392804 | frequency_hz=212.0
- [2026-08-22 01:29:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333355.039523 | source=vosk | rms=1204 | updated_at=1787333354.5392978 | frequency_hz=212.0
- [2026-08-22 01:29:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333366.042992 | source=vosk | rms=1205 | updated_at=1787333366.042992 | frequency_hz=212.0
- [2026-08-22 01:29:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333367.0521336 | source=vosk | rms=663 | updated_at=1787333366.543486 | frequency_hz=212.0
- [2026-08-22 01:29:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333368.5438273 | source=vosk | rms=1136 | updated_at=1787333368.5438273 | frequency_hz=212.0
- [2026-08-22 01:29:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333369.5430784 | source=vosk | rms=1201 | updated_at=1787333369.043115 | frequency_hz=212.0
- [2026-08-22 01:29:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333385.1337862 | source=vosk | rms=1204 | updated_at=1787333385.1337862 | frequency_hz=212.0
- [2026-08-22 01:29:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333385.8838425 | source=vosk | rms=1201 | updated_at=1787333385.3837645 | frequency_hz=212.0
- [2026-08-22 01:29:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333387.1333992 | source=vosk | rms=1205 | updated_at=1787333387.1333992 | frequency_hz=212.0
- [2026-08-22 01:29:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333388.1335862 | source=vosk | rms=769 | updated_at=1787333387.6445367 | frequency_hz=212.0
- [2026-08-22 01:29:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333390.8830743 | source=vosk | rms=769 | updated_at=1787333387.6445367 | frequency_hz=212.0
- [2026-08-22 01:29:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333391.3832157 | source=vosk | rms=769 | updated_at=1787333387.6445367 | frequency_hz=212.0
- [2026-08-22 01:29:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333394.1056676 | source=vosk | rms=1204 | updated_at=1787333394.1056676 | frequency_hz=212.0
- [2026-08-22 01:29:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333395.1055741 | source=vosk | rms=1201 | updated_at=1787333394.5816379 | frequency_hz=212.0
- [2026-08-22 01:30:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333400.6319604 | source=vosk | rms=1202 | updated_at=1787333400.6319604 | frequency_hz=212.0
- [2026-08-22 01:30:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333401.6317604 | source=vosk | rms=1202 | updated_at=1787333401.0996876 | frequency_hz=212.0
- [2026-08-22 01:30:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333403.6318958 | source=vosk | rms=1203 | updated_at=1787333403.6318958 | frequency_hz=212.0
- [2026-08-22 01:30:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333404.882428 | source=vosk | rms=1202 | updated_at=1787333403.882493 | frequency_hz=212.0
- [2026-08-22 01:30:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333406.131816 | source=vosk | rms=1203 | updated_at=1787333406.131816 | frequency_hz=212.0
- [2026-08-22 01:30:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333407.1559045 | source=vosk | rms=1201 | updated_at=1787333406.6409636 | frequency_hz=212.0
- [2026-08-22 01:30:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333407.912431 | source=vosk | rms=1201 | updated_at=1787333406.6409636 | frequency_hz=212.0
- [2026-08-22 01:30:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333408.405526 | source=vosk | rms=1201 | updated_at=1787333406.6409636 | frequency_hz=212.0
- [2026-08-22 01:30:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333409.9053984 | source=vosk | rms=1204 | updated_at=1787333409.9053984 | frequency_hz=212.0
- [2026-08-22 01:30:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333411.0527391 | source=vosk | rms=1202 | updated_at=1787333410.5539207 | frequency_hz=212.0
- [2026-08-22 01:30:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333427.684595 | source=vosk | rms=1203 | updated_at=1787333427.684595 | frequency_hz=212.0
- [2026-08-22 01:30:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333428.7891665 | source=vosk | rms=1202 | updated_at=1787333428.2823415 | frequency_hz=212.0
- [2026-08-22 01:30:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333434.1534026 | source=vosk | rms=1206 | updated_at=1787333434.1534026 | frequency_hz=212.0
- [2026-08-22 01:30:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333435.1580684 | source=vosk | rms=1002 | updated_at=1787333434.6541092 | frequency_hz=212.0
- [2026-08-22 01:30:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333437.6541054 | source=vosk | rms=1203 | updated_at=1787333437.6541054 | frequency_hz=212.0
- [2026-08-22 01:30:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333438.759985 | source=vosk | rms=1203 | updated_at=1787333438.1910543 | frequency_hz=212.0
- [2026-08-22 01:30:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333441.2598062 | source=vosk | rms=1200 | updated_at=1787333441.2598062 | frequency_hz=304.0
- [2026-08-22 01:30:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333441.9374528 | source=vosk | rms=1200 | updated_at=1787333441.51692 | frequency_hz=304.0
- [2026-08-22 01:30:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333442.0457933 | source=vosk | rms=1160 | updated_at=1787333442.0457933 | frequency_hz=304.0
- [2026-08-22 01:30:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333443.0397298 | source=vosk | rms=1160 | updated_at=1787333442.0457933 | frequency_hz=304.0
- [2026-08-22 01:30:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333445.5438623 | source=vosk | rms=1160 | updated_at=1787333442.0457933 | frequency_hz=304.0
- [2026-08-22 01:30:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333446.0523994 | source=vosk | rms=1160 | updated_at=1787333442.0457933 | frequency_hz=304.0
- [2026-08-22 01:30:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333454.099006 | source=vosk | rms=1202 | updated_at=1787333454.099006 | frequency_hz=304.0
- [2026-08-22 01:30:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333455.1772943 | source=vosk | rms=1203 | updated_at=1787333454.7126029 | frequency_hz=304.0
- [2026-08-22 01:30:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333457.9273267 | source=vosk | rms=1203 | updated_at=1787333457.9273267 | frequency_hz=304.0
- [2026-08-22 01:30:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333458.6769881 | source=vosk | rms=1201 | updated_at=1787333458.1868837 | frequency_hz=304.0
- [2026-08-22 01:31:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333460.4271703 | source=vosk | rms=1203 | updated_at=1787333460.4271703 | frequency_hz=304.0
- [2026-08-22 01:31:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333461.4275615 | source=vosk | rms=690 | updated_at=1787333460.926819 | frequency_hz=304.0
- [2026-08-22 01:31:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333494.7391222 | source=vosk | rms=143 | updated_at=1787333494.7391222 | frequency_hz=304.0
- [2026-08-22 01:31:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333495.240374 | source=vosk | rms=143 | updated_at=1787333494.7391222 | frequency_hz=304.0
- [2026-08-22 01:31:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333495.7393856 | source=vosk | rms=143 | updated_at=1787333494.7391222 | frequency_hz=304.0
- [2026-08-22 01:31:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333496.7723815 | source=vosk | rms=143 | updated_at=1787333494.7391222 | frequency_hz=304.0
- [2026-08-22 01:31:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333497.8215642 | source=vosk | rms=175 | updated_at=1787333497.8215642 | frequency_hz=304.0
- [2026-08-22 01:31:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333498.3234458 | source=vosk | rms=175 | updated_at=1787333497.8215642 | frequency_hz=304.0
- [2026-08-22 01:31:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333499.101111 | source=vosk | rms=182 | updated_at=1787333499.101111 | frequency_hz=304.0
- [2026-08-22 01:31:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333499.7111003 | source=vosk | rms=182 | updated_at=1787333499.101111 | frequency_hz=304.0
- [2026-08-22 01:31:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333499.9750268 | source=vosk | rms=183 | updated_at=1787333499.9750268 | frequency_hz=304.0
- [2026-08-22 01:31:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333504.0405934 | source=vosk | rms=253 | updated_at=1787333502.3788378 | frequency_hz=304.0
- [2026-08-22 01:31:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333506.595849 | source=vosk | rms=227 | updated_at=1787333506.595849 | frequency_hz=304.0
- [2026-08-22 01:31:49] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787333509.1382663 | source=vosk | rms=308 | updated_at=1787333508.8836298 | frequency_hz=304.0
- [2026-08-22 01:31:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333509.3451133 | source=vosk | rms=150 | updated_at=1787333509.3451133 | frequency_hz=304.0
- [2026-08-22 01:31:49] operator / voice_transcript_partial / voice: the bottom
  meta: kind=partial | timestamp=1787333509.3822377 | source=vosk | rms=150 | updated_at=1787333509.3451133 | frequency_hz=304.0
- [2026-08-22 01:31:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333509.8636866 | source=vosk | rms=126 | updated_at=1787333509.8636866 | frequency_hz=304.0
- [2026-08-22 01:31:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333510.0946002 | source=vosk | rms=246 | updated_at=1787333510.0946002 | frequency_hz=304.0
- [2026-08-22 01:31:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333510.3458502 | source=vosk | rms=250 | updated_at=1787333510.3458502 | frequency_hz=304.0
- [2026-08-22 01:31:50] operator / voice_transcript_final / voice: the bottom
  meta: kind=final | timestamp=1787333510.5539913 | source=final | rms=250 | updated_at=1787333510.3458502 | frequency_hz=304.0
- [2026-08-22 01:31:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333510.5956218 | source=vosk | rms=164 | updated_at=1787333510.5956218 | frequency_hz=304.0
- [2026-08-22 01:31:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333512.345616 | source=vosk | rms=162 | updated_at=1787333510.845458 | frequency_hz=304.0
- [2026-08-22 01:31:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333515.0989592 | source=vosk | rms=162 | updated_at=1787333510.845458 | frequency_hz=304.0
- [2026-08-22 01:31:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333517.6578913 | source=vosk | rms=223 | updated_at=1787333517.0967088 | frequency_hz=304.0
- [2026-08-22 01:31:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333517.6598923 | source=vosk | rms=223 | updated_at=1787333517.0967088 | frequency_hz=304.0
- [2026-08-22 01:31:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333518.6807778 | source=vosk | rms=237 | updated_at=1787333518.167669 | frequency_hz=304.0
- [2026-08-22 01:32:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333520.4178474 | source=vosk | rms=237 | updated_at=1787333518.167669 | frequency_hz=304.0
- [2026-08-22 01:32:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333522.6722093 | source=vosk | rms=193 | updated_at=1787333521.167965 | frequency_hz=304.0
- [2026-08-22 01:32:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333524.1672125 | source=vosk | rms=193 | updated_at=1787333521.167965 | frequency_hz=304.0
- [2026-08-22 01:32:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333526.8712351 | source=vosk | rms=190 | updated_at=1787333525.534546 | frequency_hz=304.0
- [2026-08-22 01:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333527.371343 | source=vosk | rms=673 | updated_at=1787333527.371343 | frequency_hz=304.0
- [2026-08-22 01:32:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333529.8713174 | source=vosk | rms=968 | updated_at=1787333529.372607 | frequency_hz=304.0
- [2026-08-22 01:32:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333530.621131 | source=vosk | rms=387 | updated_at=1787333530.621131 | frequency_hz=304.0
- [2026-08-22 01:32:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333532.7379093 | source=vosk | rms=512 | updated_at=1787333531.8710158 | frequency_hz=304.0
- [2026-08-22 01:32:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333533.5001915 | source=vosk | rms=433 | updated_at=1787333533.5001915 | frequency_hz=304.0
- [2026-08-22 01:32:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333539.2513127 | source=vosk | rms=131 | updated_at=1787333538.7526853 | frequency_hz=304.0
- [2026-08-22 01:32:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333539.5013282 | source=vosk | rms=336 | updated_at=1787333539.5013282 | frequency_hz=304.0
- [2026-08-22 01:32:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333540.3034446 | source=vosk | rms=336 | updated_at=1787333539.5013282 | frequency_hz=304.0
- [2026-08-22 01:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333540.5801597 | source=vosk | rms=165 | updated_at=1787333540.5801597 | frequency_hz=304.0
- [2026-08-22 01:32:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333542.8469942 | source=vosk | rms=490 | updated_at=1787333542.329503 | frequency_hz=304.0
- [2026-08-22 01:32:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333544.329103 | source=vosk | rms=344 | updated_at=1787333544.329103 | frequency_hz=304.0
- [2026-08-22 01:32:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333544.8307717 | source=vosk | rms=344 | updated_at=1787333544.329103 | frequency_hz=304.0
- [2026-08-22 01:32:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333546.3358579 | source=vosk | rms=344 | updated_at=1787333544.329103 | frequency_hz=304.0
- [2026-08-22 01:32:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333547.0797071 | source=vosk | rms=771 | updated_at=1787333546.5794141 | frequency_hz=304.0
- [2026-08-22 01:32:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333547.3299358 | source=vosk | rms=771 | updated_at=1787333546.5794141 | frequency_hz=304.0
- [2026-08-22 01:32:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333550.636121 | source=vosk | rms=1203 | updated_at=1787333550.1576018 | frequency_hz=304.0
- [2026-08-22 01:32:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333550.8857927 | source=vosk | rms=204 | updated_at=1787333550.8857927 | frequency_hz=269.7
- [2026-08-22 01:32:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333551.3855596 | source=vosk | rms=204 | updated_at=1787333550.8857927 | frequency_hz=269.7
- [2026-08-22 01:32:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333552.3861294 | source=vosk | rms=204 | updated_at=1787333550.8857927 | frequency_hz=269.7
- [2026-08-22 01:32:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333555.4245918 | source=vosk | rms=214 | updated_at=1787333554.6533692 | frequency_hz=269.7
- [2026-08-22 01:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333557.1346107 | source=vosk | rms=214 | updated_at=1787333554.6533692 | frequency_hz=269.7
- [2026-08-22 01:32:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333559.9344132 | source=vosk | rms=280 | updated_at=1787333558.6815147 | frequency_hz=269.7
- [2026-08-22 01:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333560.1769419 | source=vosk | rms=269 | updated_at=1787333560.1769419 | frequency_hz=269.7
- [2026-08-22 01:32:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333561.1186488 | source=vosk | rms=269 | updated_at=1787333560.1769419 | frequency_hz=269.7
- [2026-08-22 01:32:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333562.1271625 | source=vosk | rms=339 | updated_at=1787333562.1271625 | frequency_hz=269.7
- [2026-08-22 01:32:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333562.627839 | source=vosk | rms=339 | updated_at=1787333562.1271625 | frequency_hz=269.7
- [2026-08-22 01:32:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333562.8763208 | source=vosk | rms=325 | updated_at=1787333562.8763208 | frequency_hz=269.7
- [2026-08-22 01:32:43] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787333563.6099844 | source=vosk | rms=325 | updated_at=1787333562.8763208 | frequency_hz=269.7
- [2026-08-22 01:32:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333564.0322733 | source=vosk | rms=325 | updated_at=1787333562.8763208 | frequency_hz=269.7
- [2026-08-22 01:32:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333565.964176 | source=vosk | rms=325 | updated_at=1787333562.8763208 | frequency_hz=269.7
- [2026-08-22 01:32:45] operator / voice_transcript_partial / voice: i don't
  meta: kind=partial | timestamp=1787333565.99493 | source=vosk | rms=325 | updated_at=1787333562.8763208 | frequency_hz=269.7
- [2026-08-22 01:32:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333566.462789 | source=vosk | rms=325 | updated_at=1787333562.8763208 | frequency_hz=269.7
- [2026-08-22 01:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333568.777745 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333569.0263486 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:49] operator / voice_transcript_partial / voice: i don't understand
  meta: kind=partial | timestamp=1787333569.0991125 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333569.2771544 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:49] operator / voice_transcript_final / voice: the gold it and domingo
  meta: kind=final | timestamp=1787333569.6334639 | source=final | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333569.769061 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333569.769061 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333570.277937 | source=vosk | rms=326 | updated_at=1787333568.777745 | frequency_hz=269.7
- [2026-08-22 01:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333570.897543 | source=vosk | rms=522 | updated_at=1787333570.897543 | frequency_hz=269.7
- [2026-08-22 01:32:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333571.478934 | source=vosk | rms=522 | updated_at=1787333570.897543 | frequency_hz=269.7
- [2026-08-22 01:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333571.978173 | source=vosk | rms=1203 | updated_at=1787333571.978173 | frequency_hz=269.7
- [2026-08-22 01:32:53] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1787333573.5189395 | source=vosk | rms=527 | updated_at=1787333573.4780388 | frequency_hz=269.7
- [2026-08-22 01:32:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333573.7281764 | source=vosk | rms=306 | updated_at=1787333573.7281764 | frequency_hz=269.7
- [2026-08-22 01:32:53] operator / voice_transcript_partial / voice: what is
  meta: kind=partial | timestamp=1787333573.7436972 | source=vosk | rms=306 | updated_at=1787333573.7281764 | frequency_hz=269.7
- [2026-08-22 01:32:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333573.9770346 | source=vosk | rms=246 | updated_at=1787333573.9770346 | frequency_hz=269.7
- [2026-08-22 01:32:53] operator / voice_transcript_partial / voice: what is a
  meta: kind=partial | timestamp=1787333573.9915543 | source=vosk | rms=246 | updated_at=1787333573.9770346 | frequency_hz=269.7
- [2026-08-22 01:32:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333574.478079 | source=vosk | rms=246 | updated_at=1787333573.9770346 | frequency_hz=269.7
- [2026-08-22 01:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333575.2272143 | source=vosk | rms=626 | updated_at=1787333575.2272143 | frequency_hz=269.7
- [2026-08-22 01:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333575.4788904 | source=vosk | rms=626 | updated_at=1787333575.2272143 | frequency_hz=269.7
- [2026-08-22 01:32:55] operator / voice_transcript_partial / voice: what is a particular
  meta: kind=partial | timestamp=1787333575.5460434 | source=vosk | rms=626 | updated_at=1787333575.2272143 | frequency_hz=269.7
- [2026-08-22 01:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333575.7276876 | source=vosk | rms=241 | updated_at=1787333575.7276876 | frequency_hz=269.7
- [2026-08-22 01:32:55] operator / voice_transcript_partial / voice: what is a perfect but
  meta: kind=partial | timestamp=1787333575.7843456 | source=vosk | rms=241 | updated_at=1787333575.7276876 | frequency_hz=269.7
- [2026-08-22 01:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333575.9774323 | source=vosk | rms=249 | updated_at=1787333575.9774323 | frequency_hz=269.7
- [2026-08-22 01:32:56] operator / voice_transcript_partial / voice: what is a perfect opponent
  meta: kind=partial | timestamp=1787333576.016712 | source=vosk | rms=249 | updated_at=1787333575.9774323 | frequency_hz=269.7
- [2026-08-22 01:32:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333577.0208592 | source=vosk | rms=249 | updated_at=1787333575.9774323 | frequency_hz=269.7
- [2026-08-22 01:32:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333577.3918383 | source=vosk | rms=249 | updated_at=1787333575.9774323 | frequency_hz=269.7
- [2026-08-22 01:32:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333577.8912692 | source=vosk | rms=257 | updated_at=1787333577.8912692 | frequency_hz=269.7
- [2026-08-22 01:32:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333578.1412816 | source=vosk | rms=303 | updated_at=1787333578.1412816 | frequency_hz=269.7
- [2026-08-22 01:32:58] operator / voice_transcript_final / voice: what is a perfect opponent
  meta: kind=final | timestamp=1787333578.5955386 | source=final | rms=303 | updated_at=1787333578.1412816 | frequency_hz=269.7
- [2026-08-22 01:32:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333578.752634 | source=vosk | rms=303 | updated_at=1787333578.1412816 | frequency_hz=269.7
- [2026-08-22 01:32:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333578.752634 | source=vosk | rms=276 | updated_at=1787333578.752634 | frequency_hz=269.7
- [2026-08-22 01:32:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333579.4254515 | source=vosk | rms=276 | updated_at=1787333578.752634 | frequency_hz=269.7
- [2026-08-22 01:33:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333580.1185338 | source=vosk | rms=380 | updated_at=1787333580.1185338 | frequency_hz=269.7
- [2026-08-22 01:33:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333581.153377 | source=vosk | rms=380 | updated_at=1787333580.1185338 | frequency_hz=269.7
- [2026-08-22 01:33:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333581.6514015 | source=vosk | rms=380 | updated_at=1787333580.1185338 | frequency_hz=269.7
- [2026-08-22 01:33:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333582.1537397 | source=vosk | rms=380 | updated_at=1787333580.1185338 | frequency_hz=269.7
- [2026-08-22 01:33:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333583.2689164 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:03] operator / voice_transcript_partial / voice: don't
  meta: kind=partial | timestamp=1787333583.301881 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333583.6226194 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:03] operator / voice_transcript_partial / voice: don't think
  meta: kind=partial | timestamp=1787333583.639146 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333584.1411984 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:04] operator / voice_transcript_partial / voice: don't
  meta: kind=partial | timestamp=1787333584.1792624 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333584.6217551 | source=vosk | rms=668 | updated_at=1787333583.2679157 | frequency_hz=269.7
- [2026-08-22 01:33:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333585.1229987 | source=vosk | rms=311 | updated_at=1787333585.1229987 | frequency_hz=269.7
- [2026-08-22 01:33:05] operator / voice_transcript_final / voice: don t do that
  meta: kind=final | timestamp=1787333585.5448985 | source=final | rms=311 | updated_at=1787333585.1229987 | frequency_hz=269.7
- [2026-08-22 01:33:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333585.7453988 | source=vosk | rms=311 | updated_at=1787333585.1229987 | frequency_hz=269.7
- [2026-08-22 01:33:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333585.7453988 | source=vosk | rms=273 | updated_at=1787333585.7453988 | frequency_hz=269.7
- [2026-08-22 01:33:05] operator / voice_transcript_partial / voice: like that
  meta: kind=partial | timestamp=1787333585.7955523 | source=vosk | rms=375 | updated_at=1787333585.7578828 | frequency_hz=269.7
- [2026-08-22 01:33:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333586.1212103 | source=vosk | rms=375 | updated_at=1787333585.7578828 | frequency_hz=269.7
- [2026-08-22 01:33:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333587.1249394 | source=vosk | rms=213 | updated_at=1787333586.37136 | frequency_hz=269.7
- [2026-08-22 01:33:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333589.121398 | source=vosk | rms=213 | updated_at=1787333586.37136 | frequency_hz=269.7
- [2026-08-22 01:33:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333591.7595956 | source=vosk | rms=285 | updated_at=1787333590.6217272 | frequency_hz=269.7
- [2026-08-22 01:33:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333594.52847 | source=vosk | rms=417 | updated_at=1787333594.52847 | frequency_hz=269.7
- [2026-08-22 01:33:15] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1787333595.5693026 | source=vosk | rms=202 | updated_at=1787333595.5269508 | frequency_hz=269.7
- [2026-08-22 01:33:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333596.0284667 | source=vosk | rms=202 | updated_at=1787333595.5269508 | frequency_hz=269.7
- [2026-08-22 01:33:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333596.278006 | source=vosk | rms=222 | updated_at=1787333596.278006 | frequency_hz=269.7
- [2026-08-22 01:33:16] operator / voice_transcript_partial / voice: a strong
  meta: kind=partial | timestamp=1787333596.3250284 | source=vosk | rms=222 | updated_at=1787333596.278006 | frequency_hz=269.7
- [2026-08-22 01:33:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333596.5283976 | source=vosk | rms=222 | updated_at=1787333596.278006 | frequency_hz=269.7
- [2026-08-22 01:33:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333596.7770932 | source=vosk | rms=222 | updated_at=1787333596.278006 | frequency_hz=269.7
- [2026-08-22 01:33:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333597.3112903 | source=vosk | rms=172 | updated_at=1787333597.3112903 | frequency_hz=269.7
- [2026-08-22 01:33:17] operator / voice_transcript_final / voice: like that a strong
  meta: kind=final | timestamp=1787333597.7589593 | source=final | rms=172 | updated_at=1787333597.3112903 | frequency_hz=269.7
- [2026-08-22 01:33:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333598.0328972 | source=vosk | rms=172 | updated_at=1787333597.3112903 | frequency_hz=269.7
- [2026-08-22 01:33:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333598.0328972 | source=vosk | rms=388 | updated_at=1787333598.0328972 | frequency_hz=269.7
- [2026-08-22 01:33:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333598.5279412 | source=vosk | rms=243 | updated_at=1787333598.0840185 | frequency_hz=269.7
- [2026-08-22 01:33:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333606.5289607 | source=vosk | rms=243 | updated_at=1787333598.0840185 | frequency_hz=269.7
- [2026-08-22 01:33:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333607.0292618 | source=vosk | rms=243 | updated_at=1787333598.0840185 | frequency_hz=269.7
- [2026-08-22 01:33:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333610.0466974 | source=vosk | rms=243 | updated_at=1787333598.0840185 | frequency_hz=269.7
- [2026-08-22 01:33:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333610.528136 | source=vosk | rms=243 | updated_at=1787333598.0840185 | frequency_hz=269.7
- [2026-08-22 01:33:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333616.5090032 | source=vosk | rms=1201 | updated_at=1787333616.5090032 | frequency_hz=269.7
- [2026-08-22 01:33:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333617.2589202 | source=vosk | rms=1205 | updated_at=1787333616.759395 | frequency_hz=269.7
- [2026-08-22 01:33:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333618.2592895 | source=vosk | rms=136 | updated_at=1787333618.2592895 | frequency_hz=269.7
- [2026-08-22 01:33:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333621.9194145 | source=vosk | rms=257 | updated_at=1787333621.2147882 | frequency_hz=269.7
- [2026-08-22 01:33:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333622.9205518 | source=vosk | rms=257 | updated_at=1787333621.2147882 | frequency_hz=269.7
- [2026-08-22 01:33:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333623.8188841 | source=vosk | rms=257 | updated_at=1787333621.2147882 | frequency_hz=269.7
- [2026-08-22 01:33:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333624.9960742 | source=vosk | rms=209 | updated_at=1787333624.9960742 | frequency_hz=84.0
- [2026-08-22 01:33:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333625.5021412 | source=vosk | rms=209 | updated_at=1787333624.9960742 | frequency_hz=84.0
- [2026-08-22 01:33:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333627.5965366 | source=vosk | rms=163 | updated_at=1787333627.5965366 | frequency_hz=84.0
- [2026-08-22 01:33:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333629.4550436 | source=vosk | rms=172 | updated_at=1787333628.5963356 | frequency_hz=84.0
- [2026-08-22 01:33:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333631.8207855 | source=vosk | rms=172 | updated_at=1787333628.5963356 | frequency_hz=84.0
- [2026-08-22 01:33:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333633.4238636 | source=vosk | rms=270 | updated_at=1787333632.8210802 | frequency_hz=84.0
- [2026-08-22 01:33:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333633.931739 | source=vosk | rms=270 | updated_at=1787333632.8210802 | frequency_hz=84.0
- [2026-08-22 01:33:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333634.4347262 | source=vosk | rms=270 | updated_at=1787333632.8210802 | frequency_hz=84.0
- [2026-08-22 01:33:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333635.1815062 | source=vosk | rms=422 | updated_at=1787333635.1815062 | frequency_hz=84.0
- [2026-08-22 01:33:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333635.7878904 | source=vosk | rms=422 | updated_at=1787333635.1815062 | frequency_hz=84.0
- [2026-08-22 01:33:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333637.547817 | source=vosk | rms=140 | updated_at=1787333637.547817 | frequency_hz=84.0
- [2026-08-22 01:33:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333638.9822786 | source=vosk | rms=140 | updated_at=1787333637.547817 | frequency_hz=84.0
- [2026-08-22 01:33:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333639.2327795 | source=vosk | rms=140 | updated_at=1787333639.2327795 | frequency_hz=84.0
- [2026-08-22 01:33:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333639.9823987 | source=vosk | rms=142 | updated_at=1787333639.4826367 | frequency_hz=84.0
- [2026-08-22 01:34:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333648.5707128 | source=vosk | rms=142 | updated_at=1787333639.4826367 | frequency_hz=84.0
- [2026-08-22 01:34:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333649.954751 | source=vosk | rms=277 | updated_at=1787333648.819318 | frequency_hz=84.0
- [2026-08-22 01:34:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333652.2047744 | source=vosk | rms=277 | updated_at=1787333648.819318 | frequency_hz=84.0
- [2026-08-22 01:34:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333652.704106 | source=vosk | rms=277 | updated_at=1787333648.819318 | frequency_hz=84.0
- [2026-08-22 01:34:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333653.7769687 | source=vosk | rms=277 | updated_at=1787333648.819318 | frequency_hz=84.0
- [2026-08-22 01:34:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333654.2823439 | source=vosk | rms=277 | updated_at=1787333648.819318 | frequency_hz=84.0
- [2026-08-22 01:34:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333655.2822125 | source=vosk | rms=148 | updated_at=1787333655.2822125 | frequency_hz=84.0
- [2026-08-22 01:34:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333656.032665 | source=vosk | rms=148 | updated_at=1787333655.5323477 | frequency_hz=84.0
- [2026-08-22 01:34:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333658.1206462 | source=vosk | rms=203 | updated_at=1787333658.1206462 | frequency_hz=84.0
- [2026-08-22 01:34:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333658.6684203 | source=vosk | rms=203 | updated_at=1787333658.1206462 | frequency_hz=84.0
- [2026-08-22 01:34:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333668.1366458 | source=vosk | rms=226 | updated_at=1787333668.1366458 | frequency_hz=84.0
- [2026-08-22 01:34:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333669.0376108 | source=vosk | rms=226 | updated_at=1787333668.1366458 | frequency_hz=84.0
- [2026-08-22 01:34:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333669.533542 | source=vosk | rms=136 | updated_at=1787333669.533542 | frequency_hz=84.0
- [2026-08-22 01:34:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333671.0678334 | source=vosk | rms=136 | updated_at=1787333669.533542 | frequency_hz=84.0
- [2026-08-22 01:34:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333671.568297 | source=vosk | rms=136 | updated_at=1787333669.533542 | frequency_hz=84.0
- [2026-08-22 01:34:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333673.638338 | source=vosk | rms=151 | updated_at=1787333673.1704586 | frequency_hz=84.0
- [2026-08-22 01:34:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333673.88671 | source=vosk | rms=172 | updated_at=1787333673.88671 | frequency_hz=84.0
- [2026-08-22 01:34:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333675.1373582 | source=vosk | rms=127 | updated_at=1787333674.6375349 | frequency_hz=84.0
- [2026-08-22 01:34:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333678.097152 | source=vosk | rms=127 | updated_at=1787333674.6375349 | frequency_hz=84.0
- [2026-08-22 01:34:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333679.5166657 | source=vosk | rms=127 | updated_at=1787333674.6375349 | frequency_hz=84.0
- [2026-08-22 01:34:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333683.9400983 | source=vosk | rms=146 | updated_at=1787333683.9400983 | frequency_hz=84.0
- [2026-08-22 01:34:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333684.5578096 | source=vosk | rms=146 | updated_at=1787333683.9400983 | frequency_hz=84.0
- [2026-08-22 01:34:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333685.0571423 | source=vosk | rms=146 | updated_at=1787333683.9400983 | frequency_hz=84.0
- [2026-08-22 01:34:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333685.5577943 | source=vosk | rms=146 | updated_at=1787333683.9400983 | frequency_hz=84.0
- [2026-08-22 01:34:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333686.30712 | source=vosk | rms=146 | updated_at=1787333683.9400983 | frequency_hz=84.0
- [2026-08-22 01:34:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333688.1389685 | source=vosk | rms=124 | updated_at=1787333687.281992 | frequency_hz=84.0
- [2026-08-22 01:34:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333688.3929539 | source=vosk | rms=190 | updated_at=1787333688.3929539 | frequency_hz=84.0
- [2026-08-22 01:34:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333689.8096123 | source=vosk | rms=210 | updated_at=1787333688.6390584 | frequency_hz=84.0
- [2026-08-22 01:34:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333690.6237535 | source=vosk | rms=208 | updated_at=1787333690.6237535 | frequency_hz=84.0
- [2026-08-22 01:34:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333694.1249075 | source=vosk | rms=151 | updated_at=1787333693.1239254 | frequency_hz=244.9
- [2026-08-22 01:34:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333696.184192 | source=vosk | rms=155 | updated_at=1787333696.184192 | frequency_hz=244.9
- [2026-08-22 01:34:57] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1787333697.178346 | source=final | rms=214 | updated_at=1787333696.9336221 | frequency_hz=244.9
- [2026-08-22 01:34:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333697.2129686 | source=vosk | rms=201 | updated_at=1787333697.2129686 | frequency_hz=244.9
- [2026-08-22 01:34:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333699.9339547 | source=vosk | rms=155 | updated_at=1787333699.4334662 | frequency_hz=342.3
- [2026-08-22 01:35:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333700.932987 | source=vosk | rms=125 | updated_at=1787333700.932987 | frequency_hz=342.3
- [2026-08-22 01:35:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333701.4508195 | source=vosk | rms=125 | updated_at=1787333700.932987 | frequency_hz=342.3
- [2026-08-22 01:35:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333702.1839876 | source=vosk | rms=125 | updated_at=1787333700.932987 | frequency_hz=342.3
- [2026-08-22 01:35:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333703.3160176 | source=vosk | rms=129 | updated_at=1787333702.8077302 | frequency_hz=342.3
- [2026-08-22 01:35:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333704.0656242 | source=vosk | rms=165 | updated_at=1787333704.0656242 | frequency_hz=342.3
- [2026-08-22 01:35:06] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1787333706.268246 | source=final | rms=179 | updated_at=1787333706.0652587 | frequency_hz=342.3
- [2026-08-22 01:35:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333706.3161435 | source=vosk | rms=203 | updated_at=1787333706.3161435 | frequency_hz=342.3
- [2026-08-22 01:35:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333710.0672164 | source=vosk | rms=179 | updated_at=1787333709.5659022 | frequency_hz=342.3
- [2026-08-22 01:35:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333711.2674847 | source=vosk | rms=155 | updated_at=1787333711.2674847 | frequency_hz=342.3
- [2026-08-22 01:35:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333711.8599885 | source=vosk | rms=155 | updated_at=1787333711.2674847 | frequency_hz=342.3
- [2026-08-22 01:35:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333712.1099799 | source=vosk | rms=201 | updated_at=1787333712.1099799 | frequency_hz=342.3
- [2026-08-22 01:35:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333713.110123 | source=vosk | rms=236 | updated_at=1787333712.6093154 | frequency_hz=342.3
- [2026-08-22 01:35:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333713.8590932 | source=vosk | rms=124 | updated_at=1787333713.8590932 | frequency_hz=342.3
- [2026-08-22 01:35:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333714.609593 | source=vosk | rms=124 | updated_at=1787333713.8590932 | frequency_hz=342.3
- [2026-08-22 01:35:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333721.8159502 | source=vosk | rms=124 | updated_at=1787333713.8590932 | frequency_hz=342.3
- [2026-08-22 01:35:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333722.5811346 | source=vosk | rms=215 | updated_at=1787333722.0658631 | frequency_hz=342.3
- [2026-08-22 01:35:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333723.817272 | source=vosk | rms=167 | updated_at=1787333723.817272 | frequency_hz=342.3
- [2026-08-22 01:35:24] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1787333724.0858881 | source=vosk | rms=279 | updated_at=1787333724.079374 | frequency_hz=342.3
- [2026-08-22 01:35:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333724.5658305 | source=vosk | rms=279 | updated_at=1787333724.079374 | frequency_hz=342.3
- [2026-08-22 01:35:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333725.0657446 | source=vosk | rms=140 | updated_at=1787333725.0657446 | frequency_hz=342.3
- [2026-08-22 01:35:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333725.3162334 | source=vosk | rms=304 | updated_at=1787333725.3162334 | frequency_hz=342.3
- [2026-08-22 01:35:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333725.5738873 | source=vosk | rms=304 | updated_at=1787333725.3162334 | frequency_hz=342.3
- [2026-08-22 01:35:25] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1787333725.8573322 | source=final | rms=304 | updated_at=1787333725.3162334 | frequency_hz=342.3
- [2026-08-22 01:35:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333726.0690107 | source=vosk | rms=304 | updated_at=1787333725.3162334 | frequency_hz=342.3
- [2026-08-22 01:35:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333730.3336349 | source=vosk | rms=301 | updated_at=1787333730.3336349 | frequency_hz=342.3
- [2026-08-22 01:35:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333731.5658455 | source=vosk | rms=184 | updated_at=1787333731.0661216 | frequency_hz=342.3
- [2026-08-22 01:35:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333732.3157823 | source=vosk | rms=184 | updated_at=1787333731.0661216 | frequency_hz=342.3
- [2026-08-22 01:35:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333733.565735 | source=vosk | rms=362 | updated_at=1787333733.0945156 | frequency_hz=342.3
- [2026-08-22 01:35:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333736.0424693 | source=vosk | rms=362 | updated_at=1787333733.0945156 | frequency_hz=342.3
- [2026-08-22 01:35:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333736.8686163 | source=vosk | rms=362 | updated_at=1787333733.0945156 | frequency_hz=342.3
- [2026-08-22 01:35:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333737.8628235 | source=vosk | rms=362 | updated_at=1787333733.0945156 | frequency_hz=342.3
- [2026-08-22 01:35:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333739.612463 | source=vosk | rms=298 | updated_at=1787333738.8639996 | frequency_hz=342.3
- [2026-08-22 01:35:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333740.113163 | source=vosk | rms=601 | updated_at=1787333740.113163 | frequency_hz=342.3
- [2026-08-22 01:35:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333741.364104 | source=vosk | rms=147 | updated_at=1787333740.8631587 | frequency_hz=342.3
- [2026-08-22 01:35:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333743.1494758 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333743.8624434 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333744.1185765 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333744.6130419 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333747.2085783 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333747.9223614 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333751.555197 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333752.051165 | source=vosk | rms=1201 | updated_at=1787333743.1494758 | frequency_hz=342.3
- [2026-08-22 01:35:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333757.2835329 | source=vosk | rms=180 | updated_at=1787333757.2835329 | frequency_hz=342.3
- [2026-08-22 01:35:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333757.782661 | source=vosk | rms=180 | updated_at=1787333757.2835329 | frequency_hz=342.3
- [2026-08-22 01:35:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333759.875441 | source=vosk | rms=134 | updated_at=1787333759.875441 | frequency_hz=342.3
- [2026-08-22 01:36:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333762.374556 | source=vosk | rms=186 | updated_at=1787333760.1276143 | frequency_hz=342.3
- [2026-08-22 01:36:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333763.3080976 | source=vosk | rms=186 | updated_at=1787333760.1276143 | frequency_hz=342.3
- [2026-08-22 01:36:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333763.9212322 | source=vosk | rms=186 | updated_at=1787333760.1276143 | frequency_hz=342.3
- [2026-08-22 01:36:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333764.4215846 | source=vosk | rms=186 | updated_at=1787333760.1276143 | frequency_hz=342.3
- [2026-08-22 01:36:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333768.4855435 | source=vosk | rms=585 | updated_at=1787333767.9436872 | frequency_hz=342.3
- [2026-08-22 01:36:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333769.6409285 | source=vosk | rms=585 | updated_at=1787333767.9436872 | frequency_hz=342.3
- [2026-08-22 01:36:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333770.8871841 | source=vosk | rms=157 | updated_at=1787333770.137318 | frequency_hz=342.3
- [2026-08-22 01:36:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333771.1374133 | source=vosk | rms=127 | updated_at=1787333771.1374133 | frequency_hz=342.3
- [2026-08-22 01:36:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333776.369729 | source=vosk | rms=189 | updated_at=1787333775.852441 | frequency_hz=342.3
- [2026-08-22 01:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333777.2686954 | source=vosk | rms=157 | updated_at=1787333777.2686954 | frequency_hz=342.3
- [2026-08-22 01:36:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333777.7711074 | source=vosk | rms=157 | updated_at=1787333777.2686954 | frequency_hz=342.3
- [2026-08-22 01:36:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333778.0754094 | source=vosk | rms=244 | updated_at=1787333778.0754094 | frequency_hz=342.3
- [2026-08-22 01:36:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333780.7713318 | source=vosk | rms=367 | updated_at=1787333780.2712874 | frequency_hz=342.3
- [2026-08-22 01:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333781.0353372 | source=vosk | rms=367 | updated_at=1787333780.2712874 | frequency_hz=342.3
- [2026-08-22 01:36:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333781.5225074 | source=vosk | rms=367 | updated_at=1787333780.2712874 | frequency_hz=342.3
- [2026-08-22 01:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333788.020964 | source=vosk | rms=345 | updated_at=1787333788.020964 | frequency_hz=342.3
- [2026-08-22 01:36:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333788.7735364 | source=vosk | rms=148 | updated_at=1787333788.2777972 | frequency_hz=342.3
- [2026-08-22 01:36:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333789.0210288 | source=vosk | rms=125 | updated_at=1787333789.0210288 | frequency_hz=342.3
- [2026-08-22 01:36:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333789.521651 | source=vosk | rms=125 | updated_at=1787333789.0210288 | frequency_hz=342.3
- [2026-08-22 01:36:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333790.2736096 | source=vosk | rms=125 | updated_at=1787333789.0210288 | frequency_hz=342.3
- [2026-08-22 01:36:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333791.2715251 | source=vosk | rms=125 | updated_at=1787333789.0210288 | frequency_hz=342.3
- [2026-08-22 01:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333792.271249 | source=vosk | rms=624 | updated_at=1787333792.271249 | frequency_hz=342.3
- [2026-08-22 01:36:35] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1787333795.0454514 | source=vosk | rms=255 | updated_at=1787333795.0213747 | frequency_hz=342.3
- [2026-08-22 01:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333795.270882 | source=vosk | rms=207 | updated_at=1787333795.270882 | frequency_hz=342.3
- [2026-08-22 01:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333795.544379 | source=vosk | rms=552 | updated_at=1787333795.544379 | frequency_hz=342.3
- [2026-08-22 01:36:35] operator / voice_transcript_partial / voice: but a lot of
  meta: kind=partial | timestamp=1787333795.5805728 | source=vosk | rms=552 | updated_at=1787333795.544379 | frequency_hz=342.3
- [2026-08-22 01:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333795.7899475 | source=vosk | rms=608 | updated_at=1787333795.7899475 | frequency_hz=342.3
- [2026-08-22 01:36:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333796.021222 | source=vosk | rms=276 | updated_at=1787333796.021222 | frequency_hz=342.3
- [2026-08-22 01:36:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333796.2728138 | source=vosk | rms=1003 | updated_at=1787333796.2728138 | frequency_hz=342.3
- [2026-08-22 01:36:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333797.0615923 | source=vosk | rms=236 | updated_at=1787333797.0605874 | frequency_hz=342.3
- [2026-08-22 01:36:37] operator / voice_transcript_final / voice: but a lot of
  meta: kind=final | timestamp=1787333797.5517423 | source=final | rms=236 | updated_at=1787333797.0605874 | frequency_hz=342.3
- [2026-08-22 01:36:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333798.4786477 | source=vosk | rms=236 | updated_at=1787333797.0605874 | frequency_hz=342.3
- [2026-08-22 01:36:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333799.4899578 | source=vosk | rms=164 | updated_at=1787333799.4899578 | frequency_hz=342.3
- [2026-08-22 01:36:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333800.4749124 | source=vosk | rms=256 | updated_at=1787333799.975306 | frequency_hz=342.3
- [2026-08-22 01:36:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333801.7253776 | source=vosk | rms=140 | updated_at=1787333801.7253776 | frequency_hz=342.3
- [2026-08-22 01:36:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333803.5341015 | source=vosk | rms=243 | updated_at=1787333802.7250469 | frequency_hz=342.3
- [2026-08-22 01:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333804.275119 | source=vosk | rms=243 | updated_at=1787333802.7250469 | frequency_hz=342.3
- [2026-08-22 01:36:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333804.7766786 | source=vosk | rms=243 | updated_at=1787333802.7250469 | frequency_hz=342.3
- [2026-08-22 01:36:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333807.2846646 | source=vosk | rms=243 | updated_at=1787333802.7250469 | frequency_hz=342.3
- [2026-08-22 01:36:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333807.7752745 | source=vosk | rms=243 | updated_at=1787333802.7250469 | frequency_hz=342.3
- [2026-08-22 01:36:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333808.2751484 | source=vosk | rms=530 | updated_at=1787333808.2751484 | frequency_hz=342.3
- [2026-08-22 01:36:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333809.2751389 | source=vosk | rms=530 | updated_at=1787333808.2751484 | frequency_hz=342.3
- [2026-08-22 01:36:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333810.0257647 | source=vosk | rms=131 | updated_at=1787333810.0257647 | frequency_hz=342.3
- [2026-08-22 01:36:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333810.779094 | source=vosk | rms=120 | updated_at=1787333810.2756567 | frequency_hz=342.3
- [2026-08-22 01:36:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333811.2755845 | source=vosk | rms=120 | updated_at=1787333810.2756567 | frequency_hz=342.3
- [2026-08-22 01:36:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333812.5252576 | source=vosk | rms=120 | updated_at=1787333810.2756567 | frequency_hz=342.3
- [2026-08-22 01:36:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333812.7766302 | source=vosk | rms=120 | updated_at=1787333810.2756567 | frequency_hz=342.3
- [2026-08-22 01:36:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333816.2759516 | source=vosk | rms=271 | updated_at=1787333815.27505 | frequency_hz=342.3
- [2026-08-22 01:36:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333816.5252469 | source=vosk | rms=136 | updated_at=1787333816.5252469 | frequency_hz=342.3
- [2026-08-22 01:36:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333817.0258803 | source=vosk | rms=136 | updated_at=1787333816.5252469 | frequency_hz=342.3
- [2026-08-22 01:36:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333817.275529 | source=vosk | rms=143 | updated_at=1787333817.275529 | frequency_hz=342.3
- [2026-08-22 01:36:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333818.2753549 | source=vosk | rms=414 | updated_at=1787333817.5254755 | frequency_hz=342.3
- [2026-08-22 01:36:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333818.525713 | source=vosk | rms=414 | updated_at=1787333817.5254755 | frequency_hz=342.3
- [2026-08-22 01:37:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333821.0319133 | source=vosk | rms=145 | updated_at=1787333820.2875547 | frequency_hz=342.3
- [2026-08-22 01:37:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333821.5251057 | source=vosk | rms=145 | updated_at=1787333820.2875547 | frequency_hz=342.3
- [2026-08-22 01:37:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333823.892119 | source=vosk | rms=201 | updated_at=1787333822.2757335 | frequency_hz=342.3
- [2026-08-22 01:37:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333824.8920846 | source=vosk | rms=201 | updated_at=1787333822.2757335 | frequency_hz=342.3
- [2026-08-22 01:37:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333825.3917804 | source=vosk | rms=201 | updated_at=1787333822.2757335 | frequency_hz=342.3
- [2026-08-22 01:37:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333829.5195167 | source=vosk | rms=201 | updated_at=1787333822.2757335 | frequency_hz=342.3
- [2026-08-22 01:37:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333830.019448 | source=vosk | rms=201 | updated_at=1787333822.2757335 | frequency_hz=342.3
- [2026-08-22 01:37:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333831.0195081 | source=vosk | rms=486 | updated_at=1787333831.0195081 | frequency_hz=342.3
- [2026-08-22 01:37:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333832.0245428 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333832.2693021 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333832.7693048 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333836.520113 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333837.0206845 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333837.2694986 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333837.7694473 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333839.5239594 | source=vosk | rms=223 | updated_at=1787333831.520997 | frequency_hz=342.3
- [2026-08-22 01:37:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333840.5217667 | source=vosk | rms=129 | updated_at=1787333840.019759 | frequency_hz=342.3
- [2026-08-22 01:37:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333840.7699435 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333841.2696517 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333841.529617 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333842.019573 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333842.8382344 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333843.779468 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333845.0521398 | source=vosk | rms=121 | updated_at=1787333840.7699435 | frequency_hz=342.3
- [2026-08-22 01:37:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333845.7789102 | source=vosk | rms=146 | updated_at=1787333845.2789383 | frequency_hz=342.3
- [2026-08-22 01:37:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333846.7784278 | source=vosk | rms=146 | updated_at=1787333845.2789383 | frequency_hz=342.3
- [2026-08-22 01:37:28] operator / voice_transcript_partial / voice: come on
  meta: kind=partial | timestamp=1787333848.5531905 | source=vosk | rms=147 | updated_at=1787333848.029982 | frequency_hz=342.3
- [2026-08-22 01:37:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333848.7785969 | source=vosk | rms=200 | updated_at=1787333848.7785969 | frequency_hz=342.3
- [2026-08-22 01:37:28] operator / voice_transcript_partial / voice: come on come
  meta: kind=partial | timestamp=1787333848.7968638 | source=vosk | rms=200 | updated_at=1787333848.7785969 | frequency_hz=342.3
- [2026-08-22 01:37:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333849.2786381 | source=vosk | rms=200 | updated_at=1787333848.7785969 | frequency_hz=342.3
- [2026-08-22 01:37:29] operator / voice_transcript_partial / voice: come on come on
  meta: kind=partial | timestamp=1787333849.2936664 | source=vosk | rms=200 | updated_at=1787333848.7785969 | frequency_hz=342.3
- [2026-08-22 01:37:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333849.7856152 | source=vosk | rms=124 | updated_at=1787333849.7856152 | frequency_hz=342.3
- [2026-08-22 01:37:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333850.523252 | source=vosk | rms=197 | updated_at=1787333850.523252 | frequency_hz=342.3
- [2026-08-22 01:37:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333851.1229637 | source=vosk | rms=197 | updated_at=1787333850.523252 | frequency_hz=342.3
- [2026-08-22 01:37:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333851.6271207 | source=vosk | rms=197 | updated_at=1787333850.523252 | frequency_hz=342.3
- [2026-08-22 01:37:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333856.9985445 | source=vosk | rms=197 | updated_at=1787333850.523252 | frequency_hz=342.3
- [2026-08-22 01:37:37] operator / voice_transcript_final / voice: come on come on
  meta: kind=final | timestamp=1787333857.2771995 | source=final | rms=197 | updated_at=1787333850.523252 | frequency_hz=342.3
- [2026-08-22 01:37:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333857.5001953 | source=vosk | rms=197 | updated_at=1787333850.523252 | frequency_hz=342.3
- [2026-08-22 01:37:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333859.7484334 | source=vosk | rms=282 | updated_at=1787333859.7484334 | frequency_hz=342.3
- [2026-08-22 01:37:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333860.5049167 | source=vosk | rms=175 | updated_at=1787333859.999105 | frequency_hz=342.3
- [2026-08-22 01:37:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333866.7319465 | source=vosk | rms=208 | updated_at=1787333866.7319465 | frequency_hz=342.3
- [2026-08-22 01:37:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333867.4829247 | source=vosk | rms=208 | updated_at=1787333866.7319465 | frequency_hz=342.3
- [2026-08-22 01:37:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333868.232142 | source=vosk | rms=214 | updated_at=1787333868.232142 | frequency_hz=342.3
- [2026-08-22 01:37:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333872.4821987 | source=vosk | rms=381 | updated_at=1787333871.7314036 | frequency_hz=342.3
- [2026-08-22 01:37:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333875.8825161 | source=vosk | rms=285 | updated_at=1787333875.8825161 | frequency_hz=342.3
- [2026-08-22 01:37:56] operator / voice_transcript_final / voice: mark
  meta: kind=final | timestamp=1787333876.0787518 | source=final | rms=285 | updated_at=1787333875.8825161 | frequency_hz=342.3
- [2026-08-22 01:37:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333876.3827803 | source=vosk | rms=285 | updated_at=1787333875.8825161 | frequency_hz=342.3
- [2026-08-22 01:37:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333878.1639893 | source=vosk | rms=285 | updated_at=1787333875.8825161 | frequency_hz=342.3
- [2026-08-22 01:37:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333879.9289322 | source=vosk | rms=285 | updated_at=1787333875.8825161 | frequency_hz=342.3
- [2026-08-22 01:38:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333881.044289 | source=vosk | rms=248 | updated_at=1787333881.044289 | frequency_hz=342.3
- [2026-08-22 01:38:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333881.545152 | source=vosk | rms=248 | updated_at=1787333881.044289 | frequency_hz=342.3
- [2026-08-22 01:38:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333882.045015 | source=vosk | rms=248 | updated_at=1787333881.044289 | frequency_hz=342.3
- [2026-08-22 01:38:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333884.7630749 | source=vosk | rms=195 | updated_at=1787333884.2385361 | frequency_hz=342.3
- [2026-08-22 01:38:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333885.0132437 | source=vosk | rms=195 | updated_at=1787333884.2385361 | frequency_hz=342.3
- [2026-08-22 01:38:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333885.5128288 | source=vosk | rms=195 | updated_at=1787333884.2385361 | frequency_hz=342.3
- [2026-08-22 01:38:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333886.5132797 | source=vosk | rms=128 | updated_at=1787333886.5132797 | frequency_hz=342.3
- [2026-08-22 01:38:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333888.7529595 | source=vosk | rms=174 | updated_at=1787333887.7624846 | frequency_hz=342.3
- [2026-08-22 01:38:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333889.014489 | source=vosk | rms=174 | updated_at=1787333887.7624846 | frequency_hz=342.3
- [2026-08-22 01:38:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333889.5122328 | source=vosk | rms=174 | updated_at=1787333887.7624846 | frequency_hz=342.3
- [2026-08-22 01:38:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333892.756093 | source=vosk | rms=127 | updated_at=1787333892.756093 | frequency_hz=342.3
- [2026-08-22 01:38:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333893.2710984 | source=vosk | rms=127 | updated_at=1787333892.756093 | frequency_hz=342.3
- [2026-08-22 01:38:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333900.25259 | source=vosk | rms=175 | updated_at=1787333900.25259 | frequency_hz=342.3
- [2026-08-22 01:38:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333901.005392 | source=vosk | rms=166 | updated_at=1787333900.5185854 | frequency_hz=342.3
- [2026-08-22 01:38:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333901.2531195 | source=vosk | rms=136 | updated_at=1787333901.2531195 | frequency_hz=342.3
- [2026-08-22 01:38:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333901.7528555 | source=vosk | rms=136 | updated_at=1787333901.2531195 | frequency_hz=342.3
- [2026-08-22 01:38:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333902.254264 | source=vosk | rms=215 | updated_at=1787333902.254264 | frequency_hz=342.3
- [2026-08-22 01:38:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333902.7533474 | source=vosk | rms=215 | updated_at=1787333902.254264 | frequency_hz=342.3
- [2026-08-22 01:38:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333907.7269032 | source=vosk | rms=338 | updated_at=1787333907.7269032 | frequency_hz=342.3
- [2026-08-22 01:38:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333912.7326417 | source=vosk | rms=126 | updated_at=1787333911.2084484 | frequency_hz=342.3
- [2026-08-22 01:38:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333914.6981866 | source=vosk | rms=126 | updated_at=1787333911.2084484 | frequency_hz=342.3
- [2026-08-22 01:38:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333915.2065668 | source=vosk | rms=126 | updated_at=1787333911.2084484 | frequency_hz=342.3
- [2026-08-22 01:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333915.9758658 | source=vosk | rms=126 | updated_at=1787333911.2084484 | frequency_hz=342.3
- [2026-08-22 01:38:36] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1787333916.3023238 | source=final | rms=126 | updated_at=1787333911.2084484 | frequency_hz=342.3
- [2026-08-22 01:38:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333916.4563062 | source=vosk | rms=121 | updated_at=1787333916.4563062 | frequency_hz=342.3
- [2026-08-22 01:38:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333916.9557395 | source=vosk | rms=121 | updated_at=1787333916.4563062 | frequency_hz=342.3
- [2026-08-22 01:38:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333920.4647768 | source=vosk | rms=182 | updated_at=1787333920.4647768 | frequency_hz=64.0
- [2026-08-22 01:38:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333920.9642382 | source=vosk | rms=182 | updated_at=1787333920.4647768 | frequency_hz=64.0
- [2026-08-22 01:38:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333921.7209282 | source=vosk | rms=182 | updated_at=1787333920.4647768 | frequency_hz=64.0
- [2026-08-22 01:38:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333924.7381485 | source=vosk | rms=547 | updated_at=1787333923.7154706 | frequency_hz=64.0
- [2026-08-22 01:38:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333925.2152786 | source=vosk | rms=547 | updated_at=1787333923.7154706 | frequency_hz=64.0
- [2026-08-22 01:38:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333926.71537 | source=vosk | rms=309 | updated_at=1787333926.215925 | frequency_hz=64.0
- [2026-08-22 01:39:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333942.3794012 | source=vosk | rms=212 | updated_at=1787333942.3794012 | frequency_hz=64.0
- [2026-08-22 01:39:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333942.940611 | source=vosk | rms=212 | updated_at=1787333942.3794012 | frequency_hz=64.0
- [2026-08-22 01:39:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333948.7300417 | source=vosk | rms=212 | updated_at=1787333942.3794012 | frequency_hz=64.0
- [2026-08-22 01:39:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333949.48147 | source=vosk | rms=212 | updated_at=1787333942.3794012 | frequency_hz=64.0
- [2026-08-22 01:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333964.6766903 | source=vosk | rms=212 | updated_at=1787333942.3794012 | frequency_hz=64.0
- [2026-08-22 01:39:25] operator / voice_transcript_final / voice: a pin
  meta: kind=final | timestamp=1787333965.9909446 | source=final | rms=279 | updated_at=1787333965.1757023 | frequency_hz=64.0
- [2026-08-22 01:39:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333966.035006 | source=vosk | rms=279 | updated_at=1787333965.1757023 | frequency_hz=64.0
- [2026-08-22 01:39:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333966.035006 | source=vosk | rms=131 | updated_at=1787333966.035006 | frequency_hz=64.0
- [2026-08-22 01:39:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333966.6756501 | source=vosk | rms=131 | updated_at=1787333966.035006 | frequency_hz=64.0
- [2026-08-22 01:39:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333974.6083066 | source=vosk | rms=131 | updated_at=1787333966.035006 | frequency_hz=64.0
- [2026-08-22 01:39:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333975.108724 | source=vosk | rms=131 | updated_at=1787333966.035006 | frequency_hz=64.0
- [2026-08-22 01:39:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333978.6083477 | source=vosk | rms=131 | updated_at=1787333966.035006 | frequency_hz=64.0
- [2026-08-22 01:39:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333981.3673697 | source=vosk | rms=127 | updated_at=1787333980.8584192 | frequency_hz=64.0
- [2026-08-22 01:39:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333982.1083786 | source=vosk | rms=143 | updated_at=1787333982.1083786 | frequency_hz=64.0
- [2026-08-22 01:39:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333982.6421862 | source=vosk | rms=143 | updated_at=1787333982.1083786 | frequency_hz=64.0
- [2026-08-22 01:39:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333985.0926569 | source=vosk | rms=297 | updated_at=1787333985.0926569 | frequency_hz=64.0
- [2026-08-22 01:39:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333985.5889661 | source=vosk | rms=297 | updated_at=1787333985.0926569 | frequency_hz=64.0
- [2026-08-22 01:39:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333992.790734 | source=vosk | rms=313 | updated_at=1787333992.790734 | frequency_hz=64.0
- [2026-08-22 01:39:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333993.552778 | source=vosk | rms=215 | updated_at=1787333993.0408506 | frequency_hz=64.0
- [2026-08-22 01:39:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333994.0392416 | source=vosk | rms=152 | updated_at=1787333994.0392416 | frequency_hz=64.0
- [2026-08-22 01:39:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333994.599502 | source=vosk | rms=152 | updated_at=1787333994.0392416 | frequency_hz=64.0
- [2026-08-22 01:39:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333995.0395484 | source=vosk | rms=152 | updated_at=1787333994.0392416 | frequency_hz=64.0
- [2026-08-22 01:39:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333995.5399597 | source=vosk | rms=152 | updated_at=1787333994.0392416 | frequency_hz=64.0
- [2026-08-22 01:39:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333995.8185349 | source=vosk | rms=152 | updated_at=1787333994.0392416 | frequency_hz=64.0
- [2026-08-22 01:39:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787333998.8951113 | source=vosk | rms=153 | updated_at=1787333996.0398157 | frequency_hz=64.0
- [2026-08-22 01:39:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787333999.1512094 | source=vosk | rms=153 | updated_at=1787333996.0398157 | frequency_hz=64.0
- [2026-08-22 01:40:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334000.1437702 | source=vosk | rms=153 | updated_at=1787333996.0398157 | frequency_hz=64.0
- [2026-08-22 01:40:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334003.6449728 | source=vosk | rms=153 | updated_at=1787333996.0398157 | frequency_hz=64.0
- [2026-08-22 01:40:03] operator / voice_transcript_partial / voice: people
  meta: kind=partial | timestamp=1787334003.6638377 | source=vosk | rms=153 | updated_at=1787333996.0398157 | frequency_hz=64.0
- [2026-08-22 01:40:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334004.1449084 | source=vosk | rms=153 | updated_at=1787333996.0398157 | frequency_hz=64.0
- [2026-08-22 01:40:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334007.804299 | source=vosk | rms=350 | updated_at=1787334007.804299 | frequency_hz=64.0
- [2026-08-22 01:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334008.0546124 | source=vosk | rms=184 | updated_at=1787334008.0546124 | frequency_hz=64.0
- [2026-08-22 01:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334008.3228347 | source=vosk | rms=334 | updated_at=1787334008.3228347 | frequency_hz=64.0
- [2026-08-22 01:40:08] operator / voice_transcript_partial / voice: people per annum
  meta: kind=partial | timestamp=1787334008.4167955 | source=vosk | rms=334 | updated_at=1787334008.3228347 | frequency_hz=64.0
- [2026-08-22 01:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334008.5562606 | source=vosk | rms=175 | updated_at=1787334008.5562606 | frequency_hz=64.0
- [2026-08-22 01:40:08] operator / voice_transcript_partial / voice: people but i'm sick
  meta: kind=partial | timestamp=1787334008.6145937 | source=vosk | rms=175 | updated_at=1787334008.5562606 | frequency_hz=64.0
- [2026-08-22 01:40:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334009.0549247 | source=vosk | rms=175 | updated_at=1787334008.5562606 | frequency_hz=64.0
- [2026-08-22 01:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334010.304868 | source=vosk | rms=188 | updated_at=1787334010.304868 | frequency_hz=64.0
- [2026-08-22 01:40:10] operator / voice_transcript_partial / voice: people but i'm sick of
  meta: kind=partial | timestamp=1787334010.337458 | source=vosk | rms=188 | updated_at=1787334010.304868 | frequency_hz=64.0
- [2026-08-22 01:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334010.55441 | source=vosk | rms=304 | updated_at=1787334010.55441 | frequency_hz=64.0
- [2026-08-22 01:40:10] operator / voice_transcript_partial / voice: people but i'm sick of people
  meta: kind=partial | timestamp=1787334010.565978 | source=vosk | rms=304 | updated_at=1787334010.55441 | frequency_hz=64.0
- [2026-08-22 01:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334010.8112338 | source=vosk | rms=338 | updated_at=1787334010.8112338 | frequency_hz=64.0
- [2026-08-22 01:40:10] operator / voice_transcript_partial / voice: people but i'm sick of people to go
  meta: kind=partial | timestamp=1787334010.8249528 | source=vosk | rms=338 | updated_at=1787334010.8112338 | frequency_hz=64.0
- [2026-08-22 01:40:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334011.5789335 | source=vosk | rms=338 | updated_at=1787334010.8112338 | frequency_hz=64.0
- [2026-08-22 01:40:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334011.5894446 | source=vosk | rms=1200 | updated_at=1787334011.5894446 | frequency_hz=64.0
- [2026-08-22 01:40:11] operator / voice_transcript_partial / voice: people but i'm sick of people to couple
  meta: kind=partial | timestamp=1787334011.640868 | source=vosk | rms=1200 | updated_at=1787334011.5894446 | frequency_hz=64.0
- [2026-08-22 01:40:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334011.943646 | source=vosk | rms=130 | updated_at=1787334011.943646 | frequency_hz=64.0
- [2026-08-22 01:40:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334012.4123635 | source=vosk | rms=127 | updated_at=1787334012.4108605 | frequency_hz=64.0
- [2026-08-22 01:40:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334012.6614609 | source=vosk | rms=127 | updated_at=1787334012.4108605 | frequency_hz=64.0
- [2026-08-22 01:40:12] operator / voice_transcript_final / voice: people but i m sick of people to couple that
  meta: kind=final | timestamp=1787334012.955325 | source=final | rms=127 | updated_at=1787334012.4108605 | frequency_hz=64.0
- [2026-08-22 01:40:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334013.986794 | source=vosk | rms=127 | updated_at=1787334012.4108605 | frequency_hz=64.0
- [2026-08-22 01:40:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334013.986794 | source=vosk | rms=127 | updated_at=1787334012.4108605 | frequency_hz=64.0
- [2026-08-22 01:40:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334014.4908092 | source=vosk | rms=127 | updated_at=1787334012.4108605 | frequency_hz=64.0
- [2026-08-22 01:40:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334015.4910352 | source=vosk | rms=216 | updated_at=1787334015.4910352 | frequency_hz=64.0
- [2026-08-22 01:40:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334016.5164561 | source=vosk | rms=216 | updated_at=1787334015.4910352 | frequency_hz=64.0
- [2026-08-22 01:40:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334017.2695665 | source=vosk | rms=216 | updated_at=1787334015.4910352 | frequency_hz=64.0
- [2026-08-22 01:40:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334018.270299 | source=vosk | rms=216 | updated_at=1787334015.4910352 | frequency_hz=64.0
- [2026-08-22 01:40:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334019.2693477 | source=vosk | rms=216 | updated_at=1787334015.4910352 | frequency_hz=64.0
- [2026-08-22 01:40:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334019.770096 | source=vosk | rms=216 | updated_at=1787334015.4910352 | frequency_hz=64.0
- [2026-08-22 01:40:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334028.7416594 | source=vosk | rms=173 | updated_at=1787334028.7416594 | frequency_hz=64.0
- [2026-08-22 01:40:28] operator / voice_transcript_partial / voice: i'm
  meta: kind=partial | timestamp=1787334028.7711043 | source=vosk | rms=173 | updated_at=1787334028.7416594 | frequency_hz=64.0
- [2026-08-22 01:40:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334028.9911745 | source=vosk | rms=146 | updated_at=1787334028.9911745 | frequency_hz=64.0
- [2026-08-22 01:40:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334029.491925 | source=vosk | rms=164 | updated_at=1787334029.491925 | frequency_hz=64.0
- [2026-08-22 01:40:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334029.7414317 | source=vosk | rms=164 | updated_at=1787334029.491925 | frequency_hz=64.0
- [2026-08-22 01:40:30] operator / voice_transcript_final / voice: i m an idiot
  meta: kind=final | timestamp=1787334030.0601945 | source=final | rms=164 | updated_at=1787334029.491925 | frequency_hz=64.0
- [2026-08-22 01:40:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334030.1757698 | source=vosk | rms=164 | updated_at=1787334029.491925 | frequency_hz=64.0
- [2026-08-22 01:40:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334030.1757698 | source=vosk | rms=595 | updated_at=1787334030.1757698 | frequency_hz=64.0
- [2026-08-22 01:40:30] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1787334030.201202 | source=vosk | rms=595 | updated_at=1787334030.1757698 | frequency_hz=64.0
- [2026-08-22 01:40:30] operator / voice_transcript_partial / voice: but basically
  meta: kind=partial | timestamp=1787334030.3016412 | source=vosk | rms=136 | updated_at=1787334030.2416046 | frequency_hz=64.0
- [2026-08-22 01:40:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334030.491312 | source=vosk | rms=136 | updated_at=1787334030.2416046 | frequency_hz=64.0
- [2026-08-22 01:40:30] operator / voice_transcript_partial / voice: my place in
  meta: kind=partial | timestamp=1787334030.528822 | source=vosk | rms=136 | updated_at=1787334030.2416046 | frequency_hz=64.0
- [2026-08-22 01:40:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334030.7415352 | source=vosk | rms=123 | updated_at=1787334030.7415352 | frequency_hz=64.0
- [2026-08-22 01:40:30] operator / voice_transcript_partial / voice: my place in don't
  meta: kind=partial | timestamp=1787334030.7746859 | source=vosk | rms=123 | updated_at=1787334030.7415352 | frequency_hz=64.0
- [2026-08-22 01:40:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334031.7611747 | source=vosk | rms=123 | updated_at=1787334030.7415352 | frequency_hz=64.0
- [2026-08-22 01:40:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334032.0108051 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334032.2515082 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:32] operator / voice_transcript_partial / voice: my place in no time
  meta: kind=partial | timestamp=1787334032.2744293 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334032.502934 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:32] operator / voice_transcript_partial / voice: my place in know guide them
  meta: kind=partial | timestamp=1787334032.54285 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334033.0051692 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334038.8084233 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:38] operator / voice_transcript_partial / voice: my place in don't try to me
  meta: kind=partial | timestamp=1787334038.8274932 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334039.0576303 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334039.579317 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334054.2260318 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:54] operator / voice_transcript_final / voice: my place in don t try to me
  meta: kind=final | timestamp=1787334054.5395744 | source=final | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:40:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334054.6593094 | source=vosk | rms=148 | updated_at=1787334032.0108051 | frequency_hz=64.0
- [2026-08-22 01:41:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334062.7747405 | source=vosk | rms=136 | updated_at=1787334062.7747405 | frequency_hz=64.0
- [2026-08-22 01:41:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334063.2736735 | source=vosk | rms=136 | updated_at=1787334062.7747405 | frequency_hz=64.0
- [2026-08-22 01:41:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334070.1707177 | source=vosk | rms=177 | updated_at=1787334070.1707177 | frequency_hz=64.0
- [2026-08-22 01:41:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334072.1716447 | source=vosk | rms=205 | updated_at=1787334071.6722243 | frequency_hz=64.0
- [2026-08-22 01:41:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334073.422561 | source=vosk | rms=161 | updated_at=1787334073.422561 | frequency_hz=64.0
- [2026-08-22 01:41:14] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1787334074.4025145 | source=vosk | rms=161 | updated_at=1787334073.422561 | frequency_hz=64.0
- [2026-08-22 01:41:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334074.615896 | source=vosk | rms=161 | updated_at=1787334073.422561 | frequency_hz=64.0
- [2026-08-22 01:41:14] operator / voice_transcript_partial / voice: no more
  meta: kind=partial | timestamp=1787334074.6624873 | source=vosk | rms=161 | updated_at=1787334073.422561 | frequency_hz=64.0
- [2026-08-22 01:41:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334075.083976 | source=vosk | rms=136 | updated_at=1787334075.083976 | frequency_hz=64.0
- [2026-08-22 01:41:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334076.3035777 | source=vosk | rms=136 | updated_at=1787334075.083976 | frequency_hz=64.0
- [2026-08-22 01:41:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334076.8128114 | source=vosk | rms=136 | updated_at=1787334075.083976 | frequency_hz=64.0
- [2026-08-22 01:41:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334077.3112164 | source=vosk | rms=136 | updated_at=1787334075.083976 | frequency_hz=64.0
- [2026-08-22 01:41:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334087.051667 | source=vosk | rms=187 | updated_at=1787334087.051667 | frequency_hz=64.0
- [2026-08-22 01:41:27] operator / voice_transcript_final / voice: no more
  meta: kind=final | timestamp=1787334087.2491486 | source=final | rms=187 | updated_at=1787334087.051667 | frequency_hz=64.0
- [2026-08-22 01:41:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334087.3341732 | source=vosk | rms=187 | updated_at=1787334087.051667 | frequency_hz=64.0
- [2026-08-22 01:41:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334089.3280845 | source=vosk | rms=237 | updated_at=1787334088.55406 | frequency_hz=64.0
- [2026-08-22 01:41:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334091.8939118 | source=vosk | rms=237 | updated_at=1787334088.55406 | frequency_hz=64.0
- [2026-08-22 01:41:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334095.196933 | source=vosk | rms=135 | updated_at=1787334094.0889664 | frequency_hz=64.0
- [2026-08-22 01:41:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334098.0227656 | source=vosk | rms=167 | updated_at=1787334098.0227656 | frequency_hz=64.0
- [2026-08-22 01:41:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334099.1104593 | source=vosk | rms=167 | updated_at=1787334098.0227656 | frequency_hz=64.0
- [2026-08-22 01:41:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334099.4344213 | source=vosk | rms=156 | updated_at=1787334099.4344213 | frequency_hz=64.0
- [2026-08-22 01:41:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334102.1221995 | source=vosk | rms=152 | updated_at=1787334101.6221168 | frequency_hz=73.8
- [2026-08-22 01:41:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334103.202539 | source=vosk | rms=286 | updated_at=1787334103.202539 | frequency_hz=73.8
- [2026-08-22 01:41:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334104.2026193 | source=vosk | rms=203 | updated_at=1787334103.7020786 | frequency_hz=71.8
- [2026-08-22 01:41:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334110.1388564 | source=vosk | rms=436 | updated_at=1787334110.1388564 | frequency_hz=71.8
- [2026-08-22 01:41:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334111.9468155 | source=vosk | rms=540 | updated_at=1787334111.4383562 | frequency_hz=71.8
- [2026-08-22 01:41:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334112.446059 | source=vosk | rms=540 | updated_at=1787334111.4383562 | frequency_hz=71.8
- [2026-08-22 01:41:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334114.082353 | source=vosk | rms=247 | updated_at=1787334113.5553684 | frequency_hz=71.8
- [2026-08-22 01:41:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334114.331888 | source=vosk | rms=157 | updated_at=1787334114.331888 | frequency_hz=71.8
- [2026-08-22 01:41:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334116.6085365 | source=vosk | rms=124 | updated_at=1787334115.7530253 | frequency_hz=71.8
- [2026-08-22 01:41:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334116.9317684 | source=vosk | rms=124 | updated_at=1787334115.7530253 | frequency_hz=71.8
- [2026-08-22 01:41:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334117.3582382 | source=vosk | rms=124 | updated_at=1787334115.7530253 | frequency_hz=71.8
- [2026-08-22 01:41:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334119.8272994 | source=vosk | rms=124 | updated_at=1787334115.7530253 | frequency_hz=71.8
- [2026-08-22 01:42:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334120.3537092 | source=vosk | rms=124 | updated_at=1787334115.7530253 | frequency_hz=71.8
- [2026-08-22 01:42:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334121.1617453 | source=vosk | rms=706 | updated_at=1787334121.1617453 | frequency_hz=71.8
- [2026-08-22 01:42:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334121.7217395 | source=vosk | rms=706 | updated_at=1787334121.1617453 | frequency_hz=71.8
- [2026-08-22 01:42:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334128.205233 | source=vosk | rms=706 | updated_at=1787334121.1617453 | frequency_hz=71.8
- [2026-08-22 01:42:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334128.8609014 | source=vosk | rms=706 | updated_at=1787334121.1617453 | frequency_hz=71.8
- [2026-08-22 01:42:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334129.6347044 | source=vosk | rms=706 | updated_at=1787334121.1617453 | frequency_hz=71.8
- [2026-08-22 01:42:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334130.3609476 | source=vosk | rms=706 | updated_at=1787334121.1617453 | frequency_hz=71.8
- [2026-08-22 01:42:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334131.3758147 | source=vosk | rms=217 | updated_at=1787334131.3758147 | frequency_hz=71.8
- [2026-08-22 01:42:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334131.8848588 | source=vosk | rms=217 | updated_at=1787334131.3758147 | frequency_hz=71.8
- [2026-08-22 01:42:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334132.13488 | source=vosk | rms=217 | updated_at=1787334131.3758147 | frequency_hz=71.8
- [2026-08-22 01:42:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334132.6359174 | source=vosk | rms=217 | updated_at=1787334131.3758147 | frequency_hz=71.8
- [2026-08-22 01:42:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334142.3834255 | source=vosk | rms=309 | updated_at=1787334142.3834255 | frequency_hz=71.8
- [2026-08-22 01:42:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334143.132548 | source=vosk | rms=433 | updated_at=1787334142.650454 | frequency_hz=71.8
- [2026-08-22 01:42:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334146.4104378 | source=vosk | rms=203 | updated_at=1787334146.4104378 | frequency_hz=71.8
- [2026-08-22 01:42:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334147.3951147 | source=vosk | rms=724 | updated_at=1787334146.6331003 | frequency_hz=71.8
- [2026-08-22 01:42:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334148.3822432 | source=vosk | rms=267 | updated_at=1787334148.3822432 | frequency_hz=71.8
- [2026-08-22 01:42:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334149.6395497 | source=vosk | rms=134 | updated_at=1787334149.1323466 | frequency_hz=71.8
- [2026-08-22 01:42:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334160.810114 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334161.5590866 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334165.3090124 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334165.8087704 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334167.3082163 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334168.0587344 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334172.6610541 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:42:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334173.1853092 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:43:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334181.5013745 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:43:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334182.0283556 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:43:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334183.001203 | source=vosk | rms=166 | updated_at=1787334160.810114 | frequency_hz=71.8
- [2026-08-22 01:43:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334184.2514102 | source=vosk | rms=179 | updated_at=1787334183.2682266 | frequency_hz=71.8
- [2026-08-22 01:43:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334186.251383 | source=vosk | rms=179 | updated_at=1787334183.2682266 | frequency_hz=71.8
- [2026-08-22 01:43:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334186.7512815 | source=vosk | rms=179 | updated_at=1787334183.2682266 | frequency_hz=71.8
- [2026-08-22 01:43:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334190.0015032 | source=vosk | rms=189 | updated_at=1787334190.0015032 | frequency_hz=71.8
- [2026-08-22 01:43:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334190.5012987 | source=vosk | rms=189 | updated_at=1787334190.0015032 | frequency_hz=71.8
- [2026-08-22 01:43:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334192.1499925 | source=vosk | rms=189 | updated_at=1787334190.0015032 | frequency_hz=71.8
- [2026-08-22 01:43:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334192.9470205 | source=vosk | rms=343 | updated_at=1787334192.3995779 | frequency_hz=71.8
- [2026-08-22 01:43:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334195.399672 | source=vosk | rms=343 | updated_at=1787334192.3995779 | frequency_hz=71.8
- [2026-08-22 01:43:15] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1787334195.672116 | source=final | rms=343 | updated_at=1787334192.3995779 | frequency_hz=71.8
- [2026-08-22 01:43:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334195.899681 | source=vosk | rms=343 | updated_at=1787334192.3995779 | frequency_hz=71.8
- [2026-08-22 01:43:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334196.6511586 | source=vosk | rms=343 | updated_at=1787334192.3995779 | frequency_hz=71.8
- [2026-08-22 01:43:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334200.1511202 | source=vosk | rms=343 | updated_at=1787334192.3995779 | frequency_hz=71.8
- [2026-08-22 01:43:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334203.6147752 | source=vosk | rms=135 | updated_at=1787334201.9004447 | frequency_hz=193.7
- [2026-08-22 01:43:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334203.902645 | source=vosk | rms=135 | updated_at=1787334201.9004447 | frequency_hz=193.7
- [2026-08-22 01:43:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334204.3735147 | source=vosk | rms=135 | updated_at=1787334201.9004447 | frequency_hz=193.7
- [2026-08-22 01:43:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334204.8758674 | source=vosk | rms=135 | updated_at=1787334201.9004447 | frequency_hz=193.7
- [2026-08-22 01:43:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334206.639436 | source=vosk | rms=1202 | updated_at=1787334206.1313477 | frequency_hz=193.7
- [2026-08-22 01:43:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334207.6341457 | source=vosk | rms=1200 | updated_at=1787334207.6341457 | frequency_hz=193.7
- [2026-08-22 01:43:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334208.7277186 | source=vosk | rms=667 | updated_at=1787334208.133472 | frequency_hz=248.4
- [2026-08-22 01:43:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334209.373302 | source=vosk | rms=813 | updated_at=1787334209.373302 | frequency_hz=248.4
- [2026-08-22 01:43:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334211.374504 | source=vosk | rms=151 | updated_at=1787334210.8912501 | frequency_hz=248.4
- [2026-08-22 01:43:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334211.8943782 | source=vosk | rms=399 | updated_at=1787334211.8943782 | frequency_hz=248.4
- [2026-08-22 01:43:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334213.3990517 | source=vosk | rms=293 | updated_at=1787334212.8736084 | frequency_hz=248.4
- [2026-08-22 01:43:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334219.143566 | source=vosk | rms=293 | updated_at=1787334212.8736084 | frequency_hz=248.4
- [2026-08-22 01:43:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334219.8770308 | source=vosk | rms=1201 | updated_at=1787334219.3727858 | frequency_hz=248.4
- [2026-08-22 01:43:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334220.3799117 | source=vosk | rms=1203 | updated_at=1787334220.3799117 | frequency_hz=248.4
- [2026-08-22 01:43:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334221.1770396 | source=vosk | rms=1204 | updated_at=1787334220.6233737 | frequency_hz=248.4
- [2026-08-22 01:43:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334221.623533 | source=vosk | rms=275 | updated_at=1787334221.623533 | frequency_hz=248.4
- [2026-08-22 01:43:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334222.6399796 | source=vosk | rms=1201 | updated_at=1787334221.8732743 | frequency_hz=248.4
- [2026-08-22 01:43:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334223.1235921 | source=vosk | rms=199 | updated_at=1787334223.1235921 | frequency_hz=248.4
- [2026-08-22 01:43:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334223.6227143 | source=vosk | rms=199 | updated_at=1787334223.1235921 | frequency_hz=248.4
- [2026-08-22 01:43:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334224.6342156 | source=vosk | rms=1204 | updated_at=1787334224.6342156 | frequency_hz=248.4
- [2026-08-22 01:43:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334225.3927548 | source=vosk | rms=1201 | updated_at=1787334224.9115741 | frequency_hz=248.4
- [2026-08-22 01:43:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334228.3731663 | source=vosk | rms=1205 | updated_at=1787334228.3731663 | frequency_hz=248.4
- [2026-08-22 01:43:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334230.4288855 | source=vosk | rms=1200 | updated_at=1787334229.8780143 | frequency_hz=248.4
- [2026-08-22 01:43:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334233.123099 | source=vosk | rms=1176 | updated_at=1787334233.123099 | frequency_hz=248.4
- [2026-08-22 01:43:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334235.12286 | source=vosk | rms=1200 | updated_at=1787334234.1236632 | frequency_hz=248.4
- [2026-08-22 01:43:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334235.3747742 | source=vosk | rms=1024 | updated_at=1787334235.3747742 | frequency_hz=232.9
- [2026-08-22 01:43:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334236.3818684 | source=vosk | rms=1204 | updated_at=1787334235.8735814 | frequency_hz=232.9
- [2026-08-22 01:43:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334236.627114 | source=vosk | rms=1200 | updated_at=1787334236.627114 | frequency_hz=273.2
- [2026-08-22 01:43:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334237.3728464 | source=vosk | rms=840 | updated_at=1787334236.8731346 | frequency_hz=316.2
- [2026-08-22 01:43:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334238.8867526 | source=vosk | rms=1205 | updated_at=1787334238.8867526 | frequency_hz=310.0
- [2026-08-22 01:43:59] operator / voice_transcript_final / voice: two
  meta: kind=final | timestamp=1787334239.7929533 | source=final | rms=1202 | updated_at=1787334239.1237817 | frequency_hz=310.0
- [2026-08-22 01:43:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334239.8301623 | source=vosk | rms=1202 | updated_at=1787334239.1237817 | frequency_hz=310.0
- [2026-08-22 01:43:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334239.8301623 | source=vosk | rms=1205 | updated_at=1787334239.8301623 | frequency_hz=310.0
- [2026-08-22 01:44:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334241.3828096 | source=vosk | rms=1206 | updated_at=1787334240.9114497 | frequency_hz=310.0
- [2026-08-22 01:44:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334241.8733006 | source=vosk | rms=1207 | updated_at=1787334241.8733006 | frequency_hz=310.0
- [2026-08-22 01:44:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334242.3735082 | source=vosk | rms=1207 | updated_at=1787334241.8733006 | frequency_hz=310.0
- [2026-08-22 01:44:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334242.6367273 | source=vosk | rms=1202 | updated_at=1787334242.6367273 | frequency_hz=321.2
- [2026-08-22 01:44:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334243.6281302 | source=vosk | rms=1205 | updated_at=1787334243.1653035 | frequency_hz=321.2
- [2026-08-22 01:44:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334244.3932178 | source=vosk | rms=1206 | updated_at=1787334244.3932178 | frequency_hz=321.2
- [2026-08-22 01:44:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334244.9346282 | source=vosk | rms=1206 | updated_at=1787334244.3932178 | frequency_hz=321.2
- [2026-08-22 01:44:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334249.8732724 | source=vosk | rms=1204 | updated_at=1787334249.8732724 | frequency_hz=416.0
- [2026-08-22 01:44:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334250.8730443 | source=vosk | rms=1074 | updated_at=1787334250.3916142 | frequency_hz=416.0
- [2026-08-22 01:44:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334255.374766 | source=vosk | rms=1203 | updated_at=1787334255.374766 | frequency_hz=416.0
- [2026-08-22 01:44:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334256.6446383 | source=vosk | rms=1201 | updated_at=1787334256.126968 | frequency_hz=416.0
- [2026-08-22 01:44:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334257.3790367 | source=vosk | rms=1207 | updated_at=1787334257.3790367 | frequency_hz=416.0
- [2026-08-22 01:44:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334257.8732731 | source=vosk | rms=1207 | updated_at=1787334257.3790367 | frequency_hz=416.0
- [2026-08-22 01:44:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334263.8737733 | source=vosk | rms=1202 | updated_at=1787334263.8737733 | frequency_hz=410.0
- [2026-08-22 01:44:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334264.9296978 | source=vosk | rms=1033 | updated_at=1787334264.3739753 | frequency_hz=410.0
- [2026-08-22 01:44:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334266.1287117 | source=vosk | rms=1200 | updated_at=1787334266.1287117 | frequency_hz=410.0
- [2026-08-22 01:44:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334266.892523 | source=vosk | rms=1202 | updated_at=1787334266.4371855 | frequency_hz=410.0
- [2026-08-22 01:44:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334272.1288307 | source=vosk | rms=1203 | updated_at=1787334272.1288307 | frequency_hz=304.0
- [2026-08-22 01:44:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334273.12305 | source=vosk | rms=1203 | updated_at=1787334272.6330924 | frequency_hz=304.0
- [2026-08-22 01:44:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334277.8783975 | source=vosk | rms=1146 | updated_at=1787334277.8783975 | frequency_hz=230.0
- [2026-08-22 01:44:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334278.873925 | source=vosk | rms=1200 | updated_at=1787334278.378268 | frequency_hz=230.0
- [2026-08-22 01:44:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334279.1231756 | source=vosk | rms=741 | updated_at=1787334279.1231756 | frequency_hz=296.5
- [2026-08-22 01:44:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334280.1256075 | source=vosk | rms=1201 | updated_at=1787334279.627309 | frequency_hz=296.5
- [2026-08-22 01:44:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334280.6231394 | source=vosk | rms=1200 | updated_at=1787334280.6231394 | frequency_hz=325.7
- [2026-08-22 01:44:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334281.3760495 | source=vosk | rms=713 | updated_at=1787334280.8903842 | frequency_hz=326.5
- [2026-08-22 01:44:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334282.380447 | source=vosk | rms=178 | updated_at=1787334282.380447 | frequency_hz=82.0
- [2026-08-22 01:44:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334283.1234727 | source=vosk | rms=1163 | updated_at=1787334282.6272142 | frequency_hz=82.0
- [2026-08-22 01:44:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334285.4024968 | source=vosk | rms=1204 | updated_at=1787334285.4024968 | frequency_hz=82.0
- [2026-08-22 01:44:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334286.3732784 | source=vosk | rms=382 | updated_at=1787334285.880533 | frequency_hz=133.8
- [2026-08-22 01:44:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334288.3894553 | source=vosk | rms=382 | updated_at=1787334285.880533 | frequency_hz=133.8
- [2026-08-22 01:44:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334289.3729737 | source=vosk | rms=1207 | updated_at=1787334288.8732643 | frequency_hz=133.8
- [2026-08-22 01:44:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334289.6231947 | source=vosk | rms=1203 | updated_at=1787334289.6231947 | frequency_hz=133.8
- [2026-08-22 01:44:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334290.373837 | source=vosk | rms=1203 | updated_at=1787334289.8914714 | frequency_hz=133.8
- [2026-08-22 01:44:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334290.6241045 | source=vosk | rms=1200 | updated_at=1787334290.6241045 | frequency_hz=215.8
- [2026-08-22 01:44:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334291.62353 | source=vosk | rms=1201 | updated_at=1787334291.1499472 | frequency_hz=215.8
- [2026-08-22 01:44:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334293.3757482 | source=vosk | rms=1200 | updated_at=1787334293.3757482 | frequency_hz=215.8
- [2026-08-22 01:44:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334294.1277428 | source=vosk | rms=1200 | updated_at=1787334293.6367548 | frequency_hz=215.8
- [2026-08-22 01:44:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334298.128892 | source=vosk | rms=1200 | updated_at=1787334298.128892 | frequency_hz=215.8
- [2026-08-22 01:44:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334298.8746395 | source=vosk | rms=1202 | updated_at=1787334298.3737595 | frequency_hz=215.8
- [2026-08-22 01:45:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334301.8751733 | source=vosk | rms=996 | updated_at=1787334301.8751733 | frequency_hz=206.0
- [2026-08-22 01:45:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334303.6395166 | source=vosk | rms=733 | updated_at=1787334303.1246092 | frequency_hz=257.1
- [2026-08-22 01:45:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334310.1240184 | source=vosk | rms=1202 | updated_at=1787334310.1240184 | frequency_hz=257.1
- [2026-08-22 01:45:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334310.9002125 | source=vosk | rms=1202 | updated_at=1787334310.3741288 | frequency_hz=257.1
- [2026-08-22 01:45:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334312.642592 | source=vosk | rms=1201 | updated_at=1787334312.642592 | frequency_hz=257.1
- [2026-08-22 01:45:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334313.373222 | source=vosk | rms=1202 | updated_at=1787334312.8747888 | frequency_hz=257.1
- [2026-08-22 01:45:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334319.6237366 | source=vosk | rms=1203 | updated_at=1787334319.6237366 | frequency_hz=257.1
- [2026-08-22 01:45:20] operator / voice_transcript_final / voice: though
  meta: kind=final | timestamp=1787334320.1001606 | source=final | rms=1202 | updated_at=1787334319.8751562 | frequency_hz=257.1
- [2026-08-22 01:45:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334320.1378872 | source=vosk | rms=399 | updated_at=1787334320.1378872 | frequency_hz=286.1
- [2026-08-22 01:45:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334320.6452332 | source=vosk | rms=399 | updated_at=1787334320.1378872 | frequency_hz=286.1
- [2026-08-22 01:45:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334321.675167 | source=vosk | rms=1202 | updated_at=1787334321.675167 | frequency_hz=286.1
- [2026-08-22 01:45:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334322.374238 | source=vosk | rms=1202 | updated_at=1787334321.9060364 | frequency_hz=286.1
- [2026-08-22 01:45:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334324.1240308 | source=vosk | rms=1071 | updated_at=1787334324.1240308 | frequency_hz=258.0
- [2026-08-22 01:45:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334325.374463 | source=vosk | rms=1200 | updated_at=1787334324.936213 | frequency_hz=258.0
- [2026-08-22 01:45:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334326.128223 | source=vosk | rms=1200 | updated_at=1787334326.128223 | frequency_hz=287.4
- [2026-08-22 01:45:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334327.1238842 | source=vosk | rms=1205 | updated_at=1787334326.6259542 | frequency_hz=287.4
- [2026-08-22 01:45:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334327.925143 | source=vosk | rms=1202 | updated_at=1787334327.925143 | frequency_hz=287.4
- [2026-08-22 01:45:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334329.1239305 | source=vosk | rms=655 | updated_at=1787334328.628786 | frequency_hz=287.4
- [2026-08-22 01:45:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334331.1323698 | source=vosk | rms=1200 | updated_at=1787334331.1313698 | frequency_hz=287.4
- [2026-08-22 01:45:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334331.8744092 | source=vosk | rms=1202 | updated_at=1787334331.3737779 | frequency_hz=287.4
- [2026-08-22 01:45:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334340.890397 | source=vosk | rms=1204 | updated_at=1787334340.890397 | frequency_hz=287.4
- [2026-08-22 01:45:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334342.15282 | source=vosk | rms=869 | updated_at=1787334341.6252918 | frequency_hz=323.3
- [2026-08-22 01:45:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334342.6251009 | source=vosk | rms=1200 | updated_at=1787334342.6235974 | frequency_hz=323.3
- [2026-08-22 01:45:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334343.1269307 | source=vosk | rms=1200 | updated_at=1787334342.6235974 | frequency_hz=323.3
- [2026-08-22 01:45:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334349.263839 | source=vosk | rms=1204 | updated_at=1787334349.263839 | frequency_hz=298.0
- [2026-08-22 01:45:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334350.5136714 | source=vosk | rms=1200 | updated_at=1787334349.875302 | frequency_hz=298.0
- [2026-08-22 01:45:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334351.515258 | source=vosk | rms=1206 | updated_at=1787334351.515258 | frequency_hz=318.0
- [2026-08-22 01:45:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334354.0336614 | source=vosk | rms=1202 | updated_at=1787334353.5398834 | frequency_hz=318.0
- [2026-08-22 01:45:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334358.0354521 | source=vosk | rms=1202 | updated_at=1787334358.0354521 | frequency_hz=318.0
- [2026-08-22 01:45:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334358.867134 | source=vosk | rms=1202 | updated_at=1787334358.2838984 | frequency_hz=318.0
- [2026-08-22 01:46:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334360.0401917 | source=vosk | rms=1203 | updated_at=1787334360.0401917 | frequency_hz=344.0
- [2026-08-22 01:46:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334361.5387092 | source=vosk | rms=264 | updated_at=1787334361.0539837 | frequency_hz=308.3
- [2026-08-22 01:46:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334362.5369103 | source=vosk | rms=1205 | updated_at=1787334362.5369103 | frequency_hz=308.3
- [2026-08-22 01:46:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334363.0374992 | source=vosk | rms=1205 | updated_at=1787334362.5369103 | frequency_hz=308.3
- [2026-08-22 01:46:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334364.7851853 | source=vosk | rms=1200 | updated_at=1787334364.7841852 | frequency_hz=308.3
- [2026-08-22 01:46:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334365.534019 | source=vosk | rms=1201 | updated_at=1787334365.046632 | frequency_hz=308.3
- [2026-08-22 01:46:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334367.0353947 | source=vosk | rms=1201 | updated_at=1787334367.0353947 | frequency_hz=414.0
- [2026-08-22 01:46:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334368.0341823 | source=vosk | rms=1087 | updated_at=1787334367.5388787 | frequency_hz=414.0
- [2026-08-22 01:46:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334372.285337 | source=vosk | rms=1200 | updated_at=1787334372.285337 | frequency_hz=414.0
- [2026-08-22 01:46:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334373.0588403 | source=vosk | rms=1204 | updated_at=1787334372.533929 | frequency_hz=414.0
- [2026-08-22 01:46:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334373.7965174 | source=vosk | rms=558 | updated_at=1787334373.7965174 | frequency_hz=319.5
- [2026-08-22 01:46:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334374.8142197 | source=vosk | rms=1202 | updated_at=1787334374.285258 | frequency_hz=319.5
- [2026-08-22 01:46:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334375.2849038 | source=vosk | rms=1202 | updated_at=1787334374.285258 | frequency_hz=319.5
- [2026-08-22 01:46:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334376.2846944 | source=vosk | rms=1202 | updated_at=1787334375.814241 | frequency_hz=319.5
- [2026-08-22 01:46:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334377.2991633 | source=vosk | rms=1200 | updated_at=1787334377.2991633 | frequency_hz=319.5
- [2026-08-22 01:46:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334377.7855413 | source=vosk | rms=1200 | updated_at=1787334377.2991633 | frequency_hz=319.5
- [2026-08-22 01:46:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334379.8363388 | source=vosk | rms=726 | updated_at=1787334379.8363388 | frequency_hz=224.0
- [2026-08-22 01:46:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334380.534671 | source=vosk | rms=956 | updated_at=1787334380.0340858 | frequency_hz=224.0
- [2026-08-22 01:46:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334385.54263 | source=vosk | rms=1201 | updated_at=1787334385.54263 | frequency_hz=224.0
- [2026-08-22 01:46:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334386.283933 | source=vosk | rms=1203 | updated_at=1787334385.7847395 | frequency_hz=224.0
- [2026-08-22 01:46:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334389.28782 | source=vosk | rms=1200 | updated_at=1787334389.28782 | frequency_hz=224.0
- [2026-08-22 01:46:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334390.2889924 | source=vosk | rms=406 | updated_at=1787334389.7841148 | frequency_hz=256.9
- [2026-08-22 01:46:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334392.0339632 | source=vosk | rms=1202 | updated_at=1787334392.0339632 | frequency_hz=256.9
- [2026-08-22 01:46:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334393.0354927 | source=vosk | rms=1206 | updated_at=1787334392.5340447 | frequency_hz=256.9
- [2026-08-22 01:46:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334394.3018243 | source=vosk | rms=1201 | updated_at=1787334394.3018243 | frequency_hz=378.0
- [2026-08-22 01:46:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334395.289186 | source=vosk | rms=1201 | updated_at=1787334394.815423 | frequency_hz=378.0
- [2026-08-22 01:46:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334397.3384802 | source=vosk | rms=1202 | updated_at=1787334397.3384802 | frequency_hz=378.0
- [2026-08-22 01:46:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334398.533793 | source=vosk | rms=1202 | updated_at=1787334398.0585122 | frequency_hz=378.0
- [2026-08-22 01:46:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334399.0339427 | source=vosk | rms=1202 | updated_at=1787334398.0585122 | frequency_hz=378.0
- [2026-08-22 01:46:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334399.5347073 | source=vosk | rms=1202 | updated_at=1787334398.0585122 | frequency_hz=378.0
- [2026-08-22 01:46:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334404.547756 | source=vosk | rms=1200 | updated_at=1787334404.547756 | frequency_hz=378.0
- [2026-08-22 01:46:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334406.0356412 | source=vosk | rms=1201 | updated_at=1787334405.5629454 | frequency_hz=357.0
- [2026-08-22 01:46:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334406.2907171 | source=vosk | rms=1201 | updated_at=1787334406.2907171 | frequency_hz=357.0
- [2026-08-22 01:46:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334407.0345776 | source=vosk | rms=1204 | updated_at=1787334406.5403037 | frequency_hz=357.0
- [2026-08-22 01:46:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334407.5342393 | source=vosk | rms=1204 | updated_at=1787334406.5403037 | frequency_hz=357.0
- [2026-08-22 01:46:48] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1787334408.3232074 | source=vosk | rms=1204 | updated_at=1787334406.5403037 | frequency_hz=357.0
- [2026-08-22 01:46:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334409.3815837 | source=vosk | rms=1204 | updated_at=1787334406.5403037 | frequency_hz=357.0
- [2026-08-22 01:46:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334409.878354 | source=vosk | rms=233 | updated_at=1787334409.878354 | frequency_hz=357.0
- [2026-08-22 01:46:49] operator / voice_transcript_partial / voice: to to do
  meta: kind=partial | timestamp=1787334409.8999057 | source=vosk | rms=233 | updated_at=1787334409.878354 | frequency_hz=357.0
- [2026-08-22 01:46:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334410.125793 | source=vosk | rms=420 | updated_at=1787334410.125793 | frequency_hz=357.0
- [2026-08-22 01:46:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334410.3747582 | source=vosk | rms=214 | updated_at=1787334410.3747582 | frequency_hz=357.0
- [2026-08-22 01:46:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334410.6343174 | source=vosk | rms=387 | updated_at=1787334410.6343174 | frequency_hz=357.0
- [2026-08-22 01:46:50] operator / voice_transcript_partial / voice: to to to do
  meta: kind=partial | timestamp=1787334410.6898108 | source=vosk | rms=387 | updated_at=1787334410.6343174 | frequency_hz=357.0
- [2026-08-22 01:46:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334411.1538377 | source=vosk | rms=387 | updated_at=1787334410.6343174 | frequency_hz=357.0
- [2026-08-22 01:46:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334411.9028733 | source=vosk | rms=335 | updated_at=1787334411.9028733 | frequency_hz=357.0
- [2026-08-22 01:46:51] operator / voice_transcript_partial / voice: to to to do with it
  meta: kind=partial | timestamp=1787334411.9539523 | source=vosk | rms=335 | updated_at=1787334411.9028733 | frequency_hz=357.0
- [2026-08-22 01:46:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334412.1337192 | source=vosk | rms=805 | updated_at=1787334412.1337192 | frequency_hz=357.0
- [2026-08-22 01:46:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334412.4335675 | source=vosk | rms=868 | updated_at=1787334412.4335675 | frequency_hz=357.0
- [2026-08-22 01:46:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334413.1281328 | source=vosk | rms=868 | updated_at=1787334412.4335675 | frequency_hz=357.0
- [2026-08-22 01:46:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334413.6242752 | source=vosk | rms=1203 | updated_at=1787334413.6242752 | frequency_hz=357.0
- [2026-08-22 01:46:53] operator / voice_transcript_partial / voice: to to to do with it blew
  meta: kind=partial | timestamp=1787334413.6847992 | source=vosk | rms=1203 | updated_at=1787334413.6242752 | frequency_hz=357.0
- [2026-08-22 01:46:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334413.88428 | source=vosk | rms=1202 | updated_at=1787334413.88428 | frequency_hz=357.0
- [2026-08-22 01:46:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334414.131002 | source=vosk | rms=1202 | updated_at=1787334414.131002 | frequency_hz=357.0
- [2026-08-22 01:46:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334414.6328502 | source=vosk | rms=1202 | updated_at=1787334414.131002 | frequency_hz=357.0
- [2026-08-22 01:46:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334415.1257355 | source=vosk | rms=1202 | updated_at=1787334414.131002 | frequency_hz=357.0
- [2026-08-22 01:46:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334415.6456192 | source=vosk | rms=1200 | updated_at=1787334415.6456192 | frequency_hz=357.0
- [2026-08-22 01:46:56] operator / voice_transcript_final / voice: to to do do with it clue
  meta: kind=final | timestamp=1787334416.060658 | source=final | rms=1200 | updated_at=1787334415.6456192 | frequency_hz=357.0
- [2026-08-22 01:46:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334416.2116203 | source=vosk | rms=1200 | updated_at=1787334415.6456192 | frequency_hz=357.0
- [2026-08-22 01:46:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334416.2116203 | source=vosk | rms=1200 | updated_at=1787334416.2116203 | frequency_hz=357.0
- [2026-08-22 01:46:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334416.8746126 | source=vosk | rms=1201 | updated_at=1787334416.3979836 | frequency_hz=357.0
- [2026-08-22 01:46:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334417.400245 | source=vosk | rms=1203 | updated_at=1787334417.3997412 | frequency_hz=357.0
- [2026-08-22 01:46:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334418.6386247 | source=vosk | rms=965 | updated_at=1787334418.1741486 | frequency_hz=357.0
- [2026-08-22 01:46:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334418.8740706 | source=vosk | rms=965 | updated_at=1787334418.1741486 | frequency_hz=357.0
- [2026-08-22 01:46:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334419.3750222 | source=vosk | rms=965 | updated_at=1787334418.1741486 | frequency_hz=357.0
- [2026-08-22 01:46:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334419.624044 | source=vosk | rms=965 | updated_at=1787334418.1741486 | frequency_hz=357.0
- [2026-08-22 01:47:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334420.1249301 | source=vosk | rms=965 | updated_at=1787334418.1741486 | frequency_hz=357.0
- [2026-08-22 01:47:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334422.3742924 | source=vosk | rms=1204 | updated_at=1787334422.3742924 | frequency_hz=357.0
- [2026-08-22 01:47:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334424.1743116 | source=vosk | rms=396 | updated_at=1787334423.6249352 | frequency_hz=357.0
- [2026-08-22 01:47:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334430.124506 | source=vosk | rms=1204 | updated_at=1787334430.124506 | frequency_hz=357.0
- [2026-08-22 01:47:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334431.6477582 | source=vosk | rms=404 | updated_at=1787334431.1308818 | frequency_hz=357.0
- [2026-08-22 01:47:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334435.130901 | source=vosk | rms=1203 | updated_at=1787334435.130901 | frequency_hz=357.0
- [2026-08-22 01:47:15] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1787334435.369102 | source=final | rms=1203 | updated_at=1787334435.130901 | frequency_hz=357.0
- [2026-08-22 01:47:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334435.404482 | source=vosk | rms=1202 | updated_at=1787334435.404482 | frequency_hz=357.0
- [2026-08-22 01:47:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334436.3750708 | source=vosk | rms=1201 | updated_at=1787334435.6477616 | frequency_hz=357.0
- [2026-08-22 01:47:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334438.3748674 | source=vosk | rms=1201 | updated_at=1787334438.3748674 | frequency_hz=357.0
- [2026-08-22 01:47:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334439.1457863 | source=vosk | rms=1201 | updated_at=1787334438.6350226 | frequency_hz=357.0
- [2026-08-22 01:47:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334439.3912373 | source=vosk | rms=1201 | updated_at=1787334438.6350226 | frequency_hz=357.0
- [2026-08-22 01:47:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334440.132455 | source=vosk | rms=1201 | updated_at=1787334438.6350226 | frequency_hz=357.0
- [2026-08-22 01:47:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334440.3750944 | source=vosk | rms=1204 | updated_at=1787334440.3750944 | frequency_hz=357.0
- [2026-08-22 01:47:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334441.6467352 | source=vosk | rms=1205 | updated_at=1787334441.12726 | frequency_hz=357.0
- [2026-08-22 01:47:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334446.1977677 | source=vosk | rms=1200 | updated_at=1787334446.1977677 | frequency_hz=357.0
- [2026-08-22 01:47:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334447.3923163 | source=vosk | rms=1201 | updated_at=1787334446.3783152 | frequency_hz=357.0
- [2026-08-22 01:47:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334448.1282294 | source=vosk | rms=1203 | updated_at=1787334448.1282294 | frequency_hz=357.0
- [2026-08-22 01:47:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334448.8746865 | source=vosk | rms=1201 | updated_at=1787334448.374645 | frequency_hz=357.0
- [2026-08-22 01:47:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334454.8581269 | source=vosk | rms=1201 | updated_at=1787334454.8581269 | frequency_hz=357.0
- [2026-08-22 01:47:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334455.8651686 | source=vosk | rms=294 | updated_at=1787334455.3692493 | frequency_hz=357.0
- [2026-08-22 01:47:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334456.1106727 | source=vosk | rms=1202 | updated_at=1787334456.1106727 | frequency_hz=357.0
- [2026-08-22 01:47:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334458.659465 | source=vosk | rms=1201 | updated_at=1787334458.1047132 | frequency_hz=361.6
- [2026-08-22 01:47:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334462.8825855 | source=vosk | rms=1204 | updated_at=1787334462.8825855 | frequency_hz=361.6
- [2026-08-22 01:47:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334463.8784902 | source=vosk | rms=1038 | updated_at=1787334463.370473 | frequency_hz=361.6
- [2026-08-22 01:47:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334465.6052892 | source=vosk | rms=284 | updated_at=1787334465.6052892 | frequency_hz=361.6
- [2026-08-22 01:47:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334468.605064 | source=vosk | rms=1200 | updated_at=1787334468.1547499 | frequency_hz=361.6
- [2026-08-22 01:47:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334469.354691 | source=vosk | rms=1206 | updated_at=1787334469.354691 | frequency_hz=373.6
- [2026-08-22 01:47:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334470.3606577 | source=vosk | rms=1122 | updated_at=1787334469.8841343 | frequency_hz=373.6
- [2026-08-22 01:47:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334470.6059763 | source=vosk | rms=1203 | updated_at=1787334470.6059763 | frequency_hz=373.6
- [2026-08-22 01:47:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334471.629976 | source=vosk | rms=1204 | updated_at=1787334470.8550336 | frequency_hz=373.6
- [2026-08-22 01:47:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334472.60536 | source=vosk | rms=1203 | updated_at=1787334472.60536 | frequency_hz=373.6
- [2026-08-22 01:47:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334473.354759 | source=vosk | rms=1200 | updated_at=1787334472.8547528 | frequency_hz=373.6
- [2026-08-22 01:47:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334475.1208062 | source=vosk | rms=1200 | updated_at=1787334475.1208062 | frequency_hz=373.6
- [2026-08-22 01:47:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334476.1385589 | source=vosk | rms=881 | updated_at=1787334475.605472 | frequency_hz=373.6
- [2026-08-22 01:47:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334477.9168932 | source=vosk | rms=1205 | updated_at=1787334477.9168932 | frequency_hz=268.0
- [2026-08-22 01:47:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334478.617971 | source=vosk | rms=1204 | updated_at=1787334478.1423657 | frequency_hz=268.0
- [2026-08-22 01:47:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334479.8673904 | source=vosk | rms=1201 | updated_at=1787334479.8673904 | frequency_hz=268.0
- [2026-08-22 01:48:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334480.6218836 | source=vosk | rms=1202 | updated_at=1787334480.1400843 | frequency_hz=268.0
- [2026-08-22 01:48:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334481.1562076 | source=vosk | rms=1202 | updated_at=1787334481.1562076 | frequency_hz=268.0
- [2026-08-22 01:48:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334481.8760636 | source=vosk | rms=1201 | updated_at=1787334481.3656023 | frequency_hz=268.0
- [2026-08-22 01:48:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334483.6150157 | source=vosk | rms=1200 | updated_at=1787334483.6150157 | frequency_hz=268.0
- [2026-08-22 01:48:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334484.6188982 | source=vosk | rms=1200 | updated_at=1787334484.114729 | frequency_hz=268.0
- [2026-08-22 01:48:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334490.141857 | source=vosk | rms=1204 | updated_at=1787334490.141857 | frequency_hz=268.0
- [2026-08-22 01:48:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334491.2141364 | source=vosk | rms=1202 | updated_at=1787334490.378105 | frequency_hz=268.0
- [2026-08-22 01:48:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334492.9571064 | source=vosk | rms=1200 | updated_at=1787334492.956103 | frequency_hz=268.0
- [2026-08-22 01:48:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334494.0012846 | source=vosk | rms=928 | updated_at=1787334493.4548125 | frequency_hz=268.0
- [2026-08-22 01:48:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334494.7046707 | source=vosk | rms=928 | updated_at=1787334493.4548125 | frequency_hz=268.0
- [2026-08-22 01:48:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334495.2199683 | source=vosk | rms=928 | updated_at=1787334493.4548125 | frequency_hz=268.0
- [2026-08-22 01:48:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334495.9562662 | source=vosk | rms=1204 | updated_at=1787334495.9562662 | frequency_hz=268.0
- [2026-08-22 01:48:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334497.2065778 | source=vosk | rms=1201 | updated_at=1787334496.2098215 | frequency_hz=268.0
- [2026-08-22 01:48:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334500.7073534 | source=vosk | rms=972 | updated_at=1787334500.7073534 | frequency_hz=268.0
- [2026-08-22 01:48:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334501.9545896 | source=vosk | rms=1202 | updated_at=1787334501.4553952 | frequency_hz=268.0
- [2026-08-22 01:48:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334503.234653 | source=vosk | rms=971 | updated_at=1787334503.234653 | frequency_hz=268.0
- [2026-08-22 01:48:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334504.4625793 | source=vosk | rms=1202 | updated_at=1787334503.9942656 | frequency_hz=268.0
- [2026-08-22 01:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334512.204941 | source=vosk | rms=1201 | updated_at=1787334512.204941 | frequency_hz=268.0
- [2026-08-22 01:48:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334512.9927652 | source=vosk | rms=1202 | updated_at=1787334512.455018 | frequency_hz=268.0
- [2026-08-22 01:48:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334513.206983 | source=vosk | rms=572 | updated_at=1787334513.2064798 | frequency_hz=268.0
- [2026-08-22 01:48:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334514.2261963 | source=vosk | rms=343 | updated_at=1787334513.7048185 | frequency_hz=268.0
- [2026-08-22 01:48:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334514.4572237 | source=vosk | rms=1202 | updated_at=1787334514.4572237 | frequency_hz=268.0
- [2026-08-22 01:48:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334515.7817075 | source=vosk | rms=364 | updated_at=1787334514.9550576 | frequency_hz=268.0
- [2026-08-22 01:48:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334516.4683053 | source=vosk | rms=364 | updated_at=1787334514.9550576 | frequency_hz=268.0
- [2026-08-22 01:48:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334516.9595714 | source=vosk | rms=364 | updated_at=1787334514.9550576 | frequency_hz=268.0
- [2026-08-22 01:48:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334517.9597423 | source=vosk | rms=491 | updated_at=1787334517.9597423 | frequency_hz=268.0
- [2026-08-22 01:48:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334518.7280908 | source=vosk | rms=371 | updated_at=1787334518.2217364 | frequency_hz=268.0
- [2026-08-22 01:48:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334518.9583611 | source=vosk | rms=688 | updated_at=1787334518.9583611 | frequency_hz=268.0
- [2026-08-22 01:48:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334520.9552803 | source=vosk | rms=295 | updated_at=1787334520.4802892 | frequency_hz=268.0
- [2026-08-22 01:48:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334521.955718 | source=vosk | rms=1201 | updated_at=1787334521.955718 | frequency_hz=268.0
- [2026-08-22 01:48:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334522.7050185 | source=vosk | rms=1200 | updated_at=1787334522.206721 | frequency_hz=268.0
- [2026-08-22 01:48:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334524.4642181 | source=vosk | rms=1200 | updated_at=1787334522.206721 | frequency_hz=268.0
- [2026-08-22 01:48:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334525.709307 | source=vosk | rms=438 | updated_at=1787334525.0675468 | frequency_hz=268.0
- [2026-08-22 01:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334526.9676247 | source=vosk | rms=1203 | updated_at=1787334526.9676247 | frequency_hz=268.0
- [2026-08-22 01:48:47] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1787334527.229335 | source=vosk | rms=1204 | updated_at=1787334527.2047153 | frequency_hz=268.0
- [2026-08-22 01:48:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334527.7228086 | source=vosk | rms=1204 | updated_at=1787334527.2047153 | frequency_hz=268.0
- [2026-08-22 01:48:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334529.9686637 | source=vosk | rms=1023 | updated_at=1787334529.9686637 | frequency_hz=268.0
- [2026-08-22 01:48:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334530.227068 | source=vosk | rms=1101 | updated_at=1787334530.227068 | frequency_hz=268.0
- [2026-08-22 01:48:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334530.7348766 | source=vosk | rms=1101 | updated_at=1787334530.227068 | frequency_hz=268.0
- [2026-08-22 01:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334534.0000103 | source=vosk | rms=1202 | updated_at=1787334534.0000103 | frequency_hz=268.0
- [2026-08-22 01:48:54] operator / voice_transcript_final / voice: know
  meta: kind=final | timestamp=1787334534.6041331 | source=final | rms=1202 | updated_at=1787334534.0000103 | frequency_hz=268.0
- [2026-08-22 01:48:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334534.6548357 | source=vosk | rms=1202 | updated_at=1787334534.0000103 | frequency_hz=268.0
- [2026-08-22 01:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334534.6548357 | source=vosk | rms=1204 | updated_at=1787334534.6548357 | frequency_hz=268.0
- [2026-08-22 01:48:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334535.9664738 | source=vosk | rms=1204 | updated_at=1787334534.6548357 | frequency_hz=268.0
- [2026-08-22 01:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334536.7290745 | source=vosk | rms=1132 | updated_at=1787334536.7290745 | frequency_hz=240.0
- [2026-08-22 01:48:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334537.707943 | source=vosk | rms=1205 | updated_at=1787334537.2386355 | frequency_hz=240.0
- [2026-08-22 01:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334537.9637504 | source=vosk | rms=933 | updated_at=1787334537.9637504 | frequency_hz=240.0
- [2026-08-22 01:48:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334538.4552832 | source=vosk | rms=933 | updated_at=1787334537.9637504 | frequency_hz=240.0
- [2026-08-22 01:48:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334539.0085292 | source=vosk | rms=1015 | updated_at=1787334539.0085292 | frequency_hz=253.3
- [2026-08-22 01:48:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334539.7383432 | source=vosk | rms=1204 | updated_at=1787334539.2197404 | frequency_hz=253.3
- [2026-08-22 01:49:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334540.7300959 | source=vosk | rms=1201 | updated_at=1787334540.7300959 | frequency_hz=253.3
- [2026-08-22 01:49:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334541.4552128 | source=vosk | rms=1201 | updated_at=1787334540.9989865 | frequency_hz=253.3
- [2026-08-22 01:49:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334543.2139053 | source=vosk | rms=1202 | updated_at=1787334543.2139053 | frequency_hz=253.3
- [2026-08-22 01:49:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334543.9555497 | source=vosk | rms=1203 | updated_at=1787334543.5038733 | frequency_hz=253.3
- [2026-08-22 01:49:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334545.740161 | source=vosk | rms=671 | updated_at=1787334545.740161 | frequency_hz=253.3
- [2026-08-22 01:49:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334547.2056627 | source=vosk | rms=756 | updated_at=1787334546.7050343 | frequency_hz=310.9
- [2026-08-22 01:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334547.9660563 | source=vosk | rms=1203 | updated_at=1787334547.9660563 | frequency_hz=341.4
- [2026-08-22 01:49:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334549.2147543 | source=vosk | rms=427 | updated_at=1787334548.7054906 | frequency_hz=341.4
- [2026-08-22 01:49:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334551.2065384 | source=vosk | rms=684 | updated_at=1787334551.2050338 | frequency_hz=174.0
- [2026-08-22 01:49:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334552.2088022 | source=vosk | rms=1202 | updated_at=1787334551.7060223 | frequency_hz=174.0
- [2026-08-22 01:49:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334553.9550192 | source=vosk | rms=1202 | updated_at=1787334551.7060223 | frequency_hz=174.0
- [2026-08-22 01:49:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334555.2058547 | source=vosk | rms=1204 | updated_at=1787334554.709739 | frequency_hz=174.0
- [2026-08-22 01:49:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334555.9565115 | source=vosk | rms=1057 | updated_at=1787334555.9565115 | frequency_hz=174.0
- [2026-08-22 01:49:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334556.9566371 | source=vosk | rms=1203 | updated_at=1787334556.456295 | frequency_hz=174.0
- [2026-08-22 01:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334557.4559386 | source=vosk | rms=1032 | updated_at=1787334557.4559386 | frequency_hz=174.0
- [2026-08-22 01:49:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334557.9560053 | source=vosk | rms=1032 | updated_at=1787334557.4559386 | frequency_hz=174.0
- [2026-08-22 01:49:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334559.219938 | source=vosk | rms=1032 | updated_at=1787334557.4559386 | frequency_hz=174.0
- [2026-08-22 01:49:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334559.7414281 | source=vosk | rms=1032 | updated_at=1787334557.4559386 | frequency_hz=174.0
- [2026-08-22 01:49:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334559.986486 | source=vosk | rms=1205 | updated_at=1787334559.9854865 | frequency_hz=174.0
- [2026-08-22 01:49:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334560.9977014 | source=vosk | rms=1042 | updated_at=1787334560.500185 | frequency_hz=174.0
- [2026-08-22 01:49:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334561.475493 | source=vosk | rms=1203 | updated_at=1787334561.475493 | frequency_hz=174.0
- [2026-08-22 01:49:22] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1787334562.4825633 | source=final | rms=1204 | updated_at=1787334562.206512 | frequency_hz=174.0
- [2026-08-22 01:49:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334562.7180617 | source=vosk | rms=1204 | updated_at=1787334562.206512 | frequency_hz=174.0
- [2026-08-22 01:49:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334562.7180617 | source=vosk | rms=1204 | updated_at=1787334562.206512 | frequency_hz=174.0
- [2026-08-22 01:49:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334563.205474 | source=vosk | rms=1204 | updated_at=1787334562.206512 | frequency_hz=174.0
- [2026-08-22 01:49:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334563.9815388 | source=vosk | rms=1204 | updated_at=1787334563.9815388 | frequency_hz=174.0
- [2026-08-22 01:49:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334565.2050617 | source=vosk | rms=1205 | updated_at=1787334564.72813 | frequency_hz=174.0
- [2026-08-22 01:49:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334568.7339756 | source=vosk | rms=719 | updated_at=1787334568.7339756 | frequency_hz=152.0
- [2026-08-22 01:49:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334569.7177825 | source=vosk | rms=1201 | updated_at=1787334569.2049809 | frequency_hz=152.0
- [2026-08-22 01:49:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334571.4565322 | source=vosk | rms=1202 | updated_at=1787334571.4560285 | frequency_hz=152.0
- [2026-08-22 01:49:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334572.4865913 | source=vosk | rms=1017 | updated_at=1787334571.9555182 | frequency_hz=152.0
- [2026-08-22 01:49:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334573.9555242 | source=vosk | rms=1201 | updated_at=1787334573.9555242 | frequency_hz=152.0
- [2026-08-22 01:49:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334574.7118342 | source=vosk | rms=1204 | updated_at=1787334574.2057 | frequency_hz=152.0
- [2026-08-22 01:49:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334575.708826 | source=vosk | rms=882 | updated_at=1787334575.708826 | frequency_hz=208.0
- [2026-08-22 01:49:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334576.7050912 | source=vosk | rms=1202 | updated_at=1787334576.2060268 | frequency_hz=208.0
- [2026-08-22 01:49:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334581.7060196 | source=vosk | rms=446 | updated_at=1787334581.7060196 | frequency_hz=208.0
- [2026-08-22 01:49:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334582.7053638 | source=vosk | rms=1203 | updated_at=1787334582.213376 | frequency_hz=208.0
- [2026-08-22 01:49:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334588.8273642 | source=vosk | rms=1203 | updated_at=1787334582.213376 | frequency_hz=208.0
- [2026-08-22 01:49:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334589.3356636 | source=vosk | rms=1203 | updated_at=1787334582.213376 | frequency_hz=208.0
- [2026-08-22 01:49:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334592.3244302 | source=vosk | rms=500 | updated_at=1787334592.3244302 | frequency_hz=208.0
- [2026-08-22 01:49:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334593.556175 | source=vosk | rms=1202 | updated_at=1787334593.059874 | frequency_hz=208.0
- [2026-08-22 01:49:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334596.8061326 | source=vosk | rms=1202 | updated_at=1787334593.059874 | frequency_hz=208.0
- [2026-08-22 01:49:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334597.3069654 | source=vosk | rms=1202 | updated_at=1787334593.059874 | frequency_hz=208.0
- [2026-08-22 01:50:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334606.829835 | source=vosk | rms=230 | updated_at=1787334606.829835 | frequency_hz=208.0
- [2026-08-22 01:50:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334607.3061564 | source=vosk | rms=230 | updated_at=1787334606.829835 | frequency_hz=208.0
- [2026-08-22 01:50:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334607.8092403 | source=vosk | rms=230 | updated_at=1787334606.829835 | frequency_hz=208.0
- [2026-08-22 01:50:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334608.3119648 | source=vosk | rms=230 | updated_at=1787334606.829835 | frequency_hz=208.0
- [2026-08-22 01:50:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334608.8158891 | source=vosk | rms=545 | updated_at=1787334608.8158891 | frequency_hz=208.0
- [2026-08-22 01:50:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334610.559117 | source=vosk | rms=330 | updated_at=1787334609.3119786 | frequency_hz=208.0
- [2026-08-22 01:50:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334610.8061202 | source=vosk | rms=330 | updated_at=1787334609.3119786 | frequency_hz=208.0
- [2026-08-22 01:50:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334612.3060493 | source=vosk | rms=330 | updated_at=1787334609.3119786 | frequency_hz=208.0
- [2026-08-22 01:50:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334612.5559807 | source=vosk | rms=330 | updated_at=1787334609.3119786 | frequency_hz=208.0
- [2026-08-22 01:50:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334613.8147426 | source=vosk | rms=207 | updated_at=1787334613.3088787 | frequency_hz=208.0
- [2026-08-22 01:50:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334614.0601964 | source=vosk | rms=207 | updated_at=1787334613.3088787 | frequency_hz=208.0
- [2026-08-22 01:50:15] operator / voice_transcript_partial / voice: i've been
  meta: kind=partial | timestamp=1787334615.3335302 | source=vosk | rms=207 | updated_at=1787334613.3088787 | frequency_hz=208.0
- [2026-08-22 01:50:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334615.5583494 | source=vosk | rms=207 | updated_at=1787334613.3088787 | frequency_hz=208.0
- [2026-08-22 01:50:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334616.0618641 | source=vosk | rms=207 | updated_at=1787334613.3088787 | frequency_hz=208.0
- [2026-08-22 01:50:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334616.5621388 | source=vosk | rms=409 | updated_at=1787334616.5621388 | frequency_hz=208.0
- [2026-08-22 01:50:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334616.831411 | source=vosk | rms=561 | updated_at=1787334616.831411 | frequency_hz=208.0
- [2026-08-22 01:50:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334617.5921273 | source=vosk | rms=561 | updated_at=1787334616.831411 | frequency_hz=208.0
- [2026-08-22 01:50:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334618.5916092 | source=vosk | rms=1202 | updated_at=1787334618.5916092 | frequency_hz=208.0
- [2026-08-22 01:50:18] operator / voice_transcript_partial / voice: i've been in it's
  meta: kind=partial | timestamp=1787334618.606371 | source=vosk | rms=1202 | updated_at=1787334618.5916092 | frequency_hz=208.0
- [2026-08-22 01:50:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334618.8217304 | source=vosk | rms=1200 | updated_at=1787334618.8217304 | frequency_hz=208.0
- [2026-08-22 01:50:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334619.0708692 | source=vosk | rms=410 | updated_at=1787334619.0708692 | frequency_hz=208.0
- [2026-08-22 01:50:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334619.332527 | source=vosk | rms=1204 | updated_at=1787334619.332527 | frequency_hz=208.0
- [2026-08-22 01:50:19] operator / voice_transcript_final / voice: i ve been it s
  meta: kind=final | timestamp=1787334619.7684543 | source=final | rms=1204 | updated_at=1787334619.332527 | frequency_hz=208.0
- [2026-08-22 01:50:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334620.7635727 | source=vosk | rms=1204 | updated_at=1787334619.332527 | frequency_hz=208.0
- [2026-08-22 01:50:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334620.7635727 | source=vosk | rms=1202 | updated_at=1787334620.7635727 | frequency_hz=208.0
- [2026-08-22 01:50:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334621.3340113 | source=vosk | rms=225 | updated_at=1787334620.8169446 | frequency_hz=208.0
- [2026-08-22 01:50:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334621.6057088 | source=vosk | rms=225 | updated_at=1787334620.8169446 | frequency_hz=208.0
- [2026-08-22 01:50:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334622.559471 | source=vosk | rms=289 | updated_at=1787334621.8061767 | frequency_hz=208.0
- [2026-08-22 01:50:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334622.8086674 | source=vosk | rms=289 | updated_at=1787334621.8061767 | frequency_hz=208.0
- [2026-08-22 01:50:22] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787334622.844464 | source=vosk | rms=289 | updated_at=1787334621.8061767 | frequency_hz=208.0
- [2026-08-22 01:50:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334623.334305 | source=vosk | rms=289 | updated_at=1787334621.8061767 | frequency_hz=208.0
- [2026-08-22 01:50:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334623.8156097 | source=vosk | rms=289 | updated_at=1787334621.8061767 | frequency_hz=208.0
- [2026-08-22 01:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334624.068563 | source=vosk | rms=166 | updated_at=1787334624.068563 | frequency_hz=208.0
- [2026-08-22 01:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334624.3057077 | source=vosk | rms=176 | updated_at=1787334624.3057077 | frequency_hz=208.0
- [2026-08-22 01:50:24] operator / voice_transcript_partial / voice: it's over the
  meta: kind=partial | timestamp=1787334624.3778346 | source=vosk | rms=176 | updated_at=1787334624.3057077 | frequency_hz=208.0
- [2026-08-22 01:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334624.5560243 | source=vosk | rms=157 | updated_at=1787334624.5560243 | frequency_hz=208.0
- [2026-08-22 01:50:24] operator / voice_transcript_partial / voice: it's a really
  meta: kind=partial | timestamp=1787334624.6016521 | source=vosk | rms=157 | updated_at=1787334624.5560243 | frequency_hz=208.0
- [2026-08-22 01:50:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334625.0736792 | source=vosk | rms=186 | updated_at=1787334625.0736792 | frequency_hz=208.0
- [2026-08-22 01:50:25] operator / voice_transcript_partial / voice: it's over the
  meta: kind=partial | timestamp=1787334625.1355038 | source=vosk | rms=186 | updated_at=1787334625.0736792 | frequency_hz=208.0
- [2026-08-22 01:50:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334625.331416 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334625.5597503 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:25] operator / voice_transcript_partial / voice: it's a really good
  meta: kind=partial | timestamp=1787334625.6137135 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334626.0556982 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334626.5673394 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:27] operator / voice_transcript_final / voice: it s over the gate
  meta: kind=final | timestamp=1787334627.0012734 | source=final | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334627.1354148 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334627.810269 | source=vosk | rms=123 | updated_at=1787334625.331416 | frequency_hz=208.0
- [2026-08-22 01:50:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334629.5560937 | source=vosk | rms=128 | updated_at=1787334628.557651 | frequency_hz=282.2
- [2026-08-22 01:50:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334629.8061955 | source=vosk | rms=134 | updated_at=1787334629.8061955 | frequency_hz=282.2
- [2026-08-22 01:50:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334630.3057308 | source=vosk | rms=134 | updated_at=1787334629.8061955 | frequency_hz=282.2
- [2026-08-22 01:50:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334634.06133 | source=vosk | rms=134 | updated_at=1787334629.8061955 | frequency_hz=282.2
- [2026-08-22 01:50:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334634.6173718 | source=vosk | rms=134 | updated_at=1787334629.8061955 | frequency_hz=282.2
- [2026-08-22 01:50:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334639.5557337 | source=vosk | rms=217 | updated_at=1787334639.5557337 | frequency_hz=282.2
- [2026-08-22 01:50:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334640.0575454 | source=vosk | rms=217 | updated_at=1787334639.5557337 | frequency_hz=282.2
- [2026-08-22 01:50:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334640.3088782 | source=vosk | rms=217 | updated_at=1787334639.5557337 | frequency_hz=282.2
- [2026-08-22 01:50:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334641.557243 | source=vosk | rms=217 | updated_at=1787334639.5557337 | frequency_hz=282.2
- [2026-08-22 01:50:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334649.5608928 | source=vosk | rms=176 | updated_at=1787334649.5608928 | frequency_hz=282.2
- [2026-08-22 01:50:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334650.8058417 | source=vosk | rms=197 | updated_at=1787334650.0561268 | frequency_hz=282.2
- [2026-08-22 01:50:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334652.3065667 | source=vosk | rms=145 | updated_at=1787334652.3065667 | frequency_hz=282.2
- [2026-08-22 01:50:54] operator / voice_transcript_final / voice: sure
  meta: kind=final | timestamp=1787334654.1810515 | source=final | rms=133 | updated_at=1787334652.6137605 | frequency_hz=282.2
- [2026-08-22 01:50:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334654.237267 | source=vosk | rms=133 | updated_at=1787334652.6137605 | frequency_hz=282.2
- [2026-08-22 01:50:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334654.8351078 | source=vosk | rms=133 | updated_at=1787334652.6137605 | frequency_hz=282.2
- [2026-08-22 01:50:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334656.5781586 | source=vosk | rms=133 | updated_at=1787334652.6137605 | frequency_hz=282.2
- [2026-08-22 01:50:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334657.8128245 | source=vosk | rms=122 | updated_at=1787334657.0786793 | frequency_hz=282.2
- [2026-08-22 01:50:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334659.5562997 | source=vosk | rms=122 | updated_at=1787334657.0786793 | frequency_hz=282.2
- [2026-08-22 01:51:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334660.0561316 | source=vosk | rms=122 | updated_at=1787334657.0786793 | frequency_hz=282.2
- [2026-08-22 01:51:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334661.8339765 | source=vosk | rms=281 | updated_at=1787334661.8339765 | frequency_hz=282.2
- [2026-08-22 01:51:05] operator / voice_transcript_final / voice: blue
  meta: kind=final | timestamp=1787334665.7884917 | source=final | rms=322 | updated_at=1787334665.56439 | frequency_hz=282.2
- [2026-08-22 01:51:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334665.8206992 | source=vosk | rms=306 | updated_at=1787334665.8206992 | frequency_hz=282.2
- [2026-08-22 01:51:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334667.6359046 | source=vosk | rms=207 | updated_at=1787334666.3402143 | frequency_hz=282.2
- [2026-08-22 01:51:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334667.8706915 | source=vosk | rms=275 | updated_at=1787334667.8706915 | frequency_hz=282.2
- [2026-08-22 01:51:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334672.3661754 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334673.1166666 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334673.619537 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334678.623498 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334679.1703262 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334680.6314976 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334682.1165938 | source=vosk | rms=189 | updated_at=1787334671.8689995 | frequency_hz=282.2
- [2026-08-22 01:51:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334683.875615 | source=vosk | rms=401 | updated_at=1787334683.875615 | frequency_hz=144.0
- [2026-08-22 01:51:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334685.3718514 | source=vosk | rms=370 | updated_at=1787334684.8754947 | frequency_hz=144.0
- [2026-08-22 01:51:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334688.8661513 | source=vosk | rms=370 | updated_at=1787334684.8754947 | frequency_hz=144.0
- [2026-08-22 01:51:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334689.8691297 | source=vosk | rms=194 | updated_at=1787334689.1418083 | frequency_hz=144.0
- [2026-08-22 01:51:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334690.1221519 | source=vosk | rms=194 | updated_at=1787334689.1418083 | frequency_hz=144.0
- [2026-08-22 01:51:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334692.6490655 | source=vosk | rms=191 | updated_at=1787334692.1336064 | frequency_hz=144.0
- [2026-08-22 01:51:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334696.6166668 | source=vosk | rms=227 | updated_at=1787334696.6166668 | frequency_hz=144.0
- [2026-08-22 01:51:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334697.3668673 | source=vosk | rms=145 | updated_at=1787334696.8666859 | frequency_hz=144.0
- [2026-08-22 01:51:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334697.6347237 | source=vosk | rms=145 | updated_at=1787334696.8666859 | frequency_hz=144.0
- [2026-08-22 01:51:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334700.3667152 | source=vosk | rms=139 | updated_at=1787334699.8855808 | frequency_hz=144.0
- [2026-08-22 01:51:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334700.8678193 | source=vosk | rms=185 | updated_at=1787334700.8678193 | frequency_hz=144.0
- [2026-08-22 01:51:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334701.6269383 | source=vosk | rms=143 | updated_at=1787334701.1374576 | frequency_hz=144.0
- [2026-08-22 01:51:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334702.1189368 | source=vosk | rms=143 | updated_at=1787334701.1374576 | frequency_hz=144.0
- [2026-08-22 01:51:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334703.1192725 | source=vosk | rms=143 | updated_at=1787334701.1374576 | frequency_hz=144.0
- [2026-08-22 01:51:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334703.3668945 | source=vosk | rms=174 | updated_at=1787334703.3668945 | frequency_hz=144.0
- [2026-08-22 01:51:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334704.367732 | source=vosk | rms=124 | updated_at=1787334703.8706112 | frequency_hz=144.0
- [2026-08-22 01:51:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334705.866382 | source=vosk | rms=124 | updated_at=1787334703.8706112 | frequency_hz=144.0
- [2026-08-22 01:51:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334707.1450224 | source=vosk | rms=618 | updated_at=1787334706.116755 | frequency_hz=144.0
- [2026-08-22 01:51:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334708.1385612 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334708.6168177 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334709.6169806 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334710.3772254 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334710.6949573 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334711.143462 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334713.3665965 | source=vosk | rms=143 | updated_at=1787334708.1385612 | frequency_hz=144.0
- [2026-08-22 01:51:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334715.866648 | source=vosk | rms=311 | updated_at=1787334715.3958433 | frequency_hz=223.1
- [2026-08-22 01:51:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334716.1477897 | source=vosk | rms=125 | updated_at=1787334716.1477897 | frequency_hz=219.9
- [2026-08-22 01:51:59] operator / voice_transcript_final / voice: gordon
  meta: kind=final | timestamp=1787334719.6784587 | source=final | rms=1203 | updated_at=1787334719.3664188 | frequency_hz=219.9
- [2026-08-22 01:51:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334719.7661202 | source=vosk | rms=1202 | updated_at=1787334719.7661202 | frequency_hz=219.9
- [2026-08-22 01:52:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334720.37178 | source=vosk | rms=219 | updated_at=1787334719.8791993 | frequency_hz=219.9
- [2026-08-22 01:52:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334722.6177397 | source=vosk | rms=219 | updated_at=1787334719.8791993 | frequency_hz=219.9
- [2026-08-22 01:52:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334723.1461039 | source=vosk | rms=219 | updated_at=1787334719.8791993 | frequency_hz=219.9
- [2026-08-22 01:52:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334724.616302 | source=vosk | rms=219 | updated_at=1787334719.8791993 | frequency_hz=219.9
- [2026-08-22 01:52:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334727.3667753 | source=vosk | rms=135 | updated_at=1787334726.634497 | frequency_hz=219.9
- [2026-08-22 01:52:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334728.135284 | source=vosk | rms=135 | updated_at=1787334726.634497 | frequency_hz=219.9
- [2026-08-22 01:52:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334728.6235247 | source=vosk | rms=135 | updated_at=1787334726.634497 | frequency_hz=219.9
- [2026-08-22 01:52:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334729.1256504 | source=vosk | rms=135 | updated_at=1787334726.634497 | frequency_hz=219.9
- [2026-08-22 01:52:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334730.367813 | source=vosk | rms=135 | updated_at=1787334726.634497 | frequency_hz=219.9
- [2026-08-22 01:52:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334733.1163821 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334733.6489153 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334734.1219933 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334734.6254265 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334735.6214519 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:15] operator / voice_transcript_partial / voice: the submission
  meta: kind=partial | timestamp=1787334735.7086005 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334735.8946328 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334736.3755136 | source=vosk | rms=181 | updated_at=1787334733.1163821 | frequency_hz=219.9
- [2026-08-22 01:52:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334736.8685658 | source=vosk | rms=302 | updated_at=1787334736.8685658 | frequency_hz=219.9
- [2026-08-22 01:52:18] operator / voice_transcript_final / voice: submission
  meta: kind=final | timestamp=1787334738.0488617 | source=final | rms=302 | updated_at=1787334736.8685658 | frequency_hz=219.9
- [2026-08-22 01:52:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334738.1316664 | source=vosk | rms=302 | updated_at=1787334736.8685658 | frequency_hz=219.9
- [2026-08-22 01:52:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334738.1316664 | source=vosk | rms=302 | updated_at=1787334736.8685658 | frequency_hz=219.9
- [2026-08-22 01:52:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334738.660596 | source=vosk | rms=242 | updated_at=1787334738.153078 | frequency_hz=219.9
- [2026-08-22 01:52:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334740.955612 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334741.4364219 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334742.9367173 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:22] operator / voice_transcript_partial / voice: panasonic
  meta: kind=partial | timestamp=1787334742.955387 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334743.437032 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334744.6865766 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:24] operator / voice_transcript_partial / voice: fantasy
  meta: kind=partial | timestamp=1787334744.7104192 | source=vosk | rms=254 | updated_at=1787334740.955612 | frequency_hz=219.9
- [2026-08-22 01:52:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334744.9446816 | source=vosk | rms=125 | updated_at=1787334744.9446816 | frequency_hz=219.9
- [2026-08-22 01:52:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334745.193248 | source=vosk | rms=522 | updated_at=1787334745.193248 | frequency_hz=219.9
- [2026-08-22 01:52:25] operator / voice_transcript_final / voice: fantasy
  meta: kind=final | timestamp=1787334745.4938722 | source=final | rms=522 | updated_at=1787334745.193248 | frequency_hz=219.9
- [2026-08-22 01:52:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334745.5300987 | source=vosk | rms=689 | updated_at=1787334745.5300987 | frequency_hz=219.9
- [2026-08-22 01:52:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334746.4415488 | source=vosk | rms=474 | updated_at=1787334745.9394443 | frequency_hz=219.9
- [2026-08-22 01:52:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334747.7101865 | source=vosk | rms=259 | updated_at=1787334747.7101865 | frequency_hz=219.9
- [2026-08-22 01:52:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334748.6863794 | source=vosk | rms=259 | updated_at=1787334747.7101865 | frequency_hz=219.9
- [2026-08-22 01:52:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334749.9365299 | source=vosk | rms=259 | updated_at=1787334747.7101865 | frequency_hz=219.9
- [2026-08-22 01:52:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334750.9381003 | source=vosk | rms=362 | updated_at=1787334750.440746 | frequency_hz=219.9
- [2026-08-22 01:52:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334751.1866653 | source=vosk | rms=362 | updated_at=1787334750.440746 | frequency_hz=219.9
- [2026-08-22 01:52:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334751.6902082 | source=vosk | rms=362 | updated_at=1787334750.440746 | frequency_hz=219.9
- [2026-08-22 01:52:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334755.436434 | source=vosk | rms=1104 | updated_at=1787334755.436434 | frequency_hz=219.9
- [2026-08-22 01:52:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334756.9366465 | source=vosk | rms=692 | updated_at=1787334756.443142 | frequency_hz=219.9
- [2026-08-22 01:52:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334758.4702134 | source=vosk | rms=692 | updated_at=1787334756.443142 | frequency_hz=219.9
- [2026-08-22 01:52:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334758.9364054 | source=vosk | rms=692 | updated_at=1787334756.443142 | frequency_hz=219.9
- [2026-08-22 01:52:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334759.687381 | source=vosk | rms=1124 | updated_at=1787334759.687381 | frequency_hz=219.9
- [2026-08-22 01:52:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334760.2041125 | source=vosk | rms=1124 | updated_at=1787334759.687381 | frequency_hz=219.9
- [2026-08-22 01:52:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334760.720934 | source=vosk | rms=249 | updated_at=1787334760.720934 | frequency_hz=219.9
- [2026-08-22 01:52:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334761.207912 | source=vosk | rms=249 | updated_at=1787334760.720934 | frequency_hz=219.9
- [2026-08-22 01:52:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334762.46481 | source=vosk | rms=1192 | updated_at=1787334762.46481 | frequency_hz=219.9
- [2026-08-22 01:52:43] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1787334763.907024 | source=final | rms=192 | updated_at=1787334763.7122889 | frequency_hz=219.9
- [2026-08-22 01:52:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334763.9616995 | source=vosk | rms=493 | updated_at=1787334763.9616995 | frequency_hz=219.9
- [2026-08-22 01:52:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334765.4575684 | source=vosk | rms=179 | updated_at=1787334764.9617493 | frequency_hz=219.9
- [2026-08-22 01:52:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334766.457313 | source=vosk | rms=179 | updated_at=1787334764.9617493 | frequency_hz=219.9
- [2026-08-22 01:52:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334767.706973 | source=vosk | rms=179 | updated_at=1787334764.9617493 | frequency_hz=219.9
- [2026-08-22 01:52:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334769.4568248 | source=vosk | rms=1206 | updated_at=1787334769.4568248 | frequency_hz=219.9
- [2026-08-22 01:52:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334770.4618807 | source=vosk | rms=237 | updated_at=1787334769.95793 | frequency_hz=219.9
- [2026-08-22 01:52:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334771.7260394 | source=vosk | rms=237 | updated_at=1787334769.95793 | frequency_hz=219.9
- [2026-08-22 01:52:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334772.2319014 | source=vosk | rms=237 | updated_at=1787334769.95793 | frequency_hz=219.9
- [2026-08-22 01:52:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334775.456669 | source=vosk | rms=301 | updated_at=1787334775.456669 | frequency_hz=219.9
- [2026-08-22 01:52:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334775.9567177 | source=vosk | rms=301 | updated_at=1787334775.456669 | frequency_hz=219.9
- [2026-08-22 01:52:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334777.738251 | source=vosk | rms=1204 | updated_at=1787334777.738251 | frequency_hz=336.0
- [2026-08-22 01:52:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334779.4572344 | source=vosk | rms=1100 | updated_at=1787334778.9586775 | frequency_hz=319.2
- [2026-08-22 01:53:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334782.5726173 | source=vosk | rms=1100 | updated_at=1787334778.9586775 | frequency_hz=319.2
- [2026-08-22 01:53:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334783.236246 | source=vosk | rms=1100 | updated_at=1787334778.9586775 | frequency_hz=319.2
- [2026-08-22 01:53:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334785.9760232 | source=vosk | rms=1100 | updated_at=1787334778.9586775 | frequency_hz=319.2
- [2026-08-22 01:53:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334786.4564834 | source=vosk | rms=1100 | updated_at=1787334778.9586775 | frequency_hz=319.2
- [2026-08-22 01:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334788.9692414 | source=vosk | rms=1200 | updated_at=1787334788.9692414 | frequency_hz=319.2
- [2026-08-22 01:53:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334789.708448 | source=vosk | rms=1201 | updated_at=1787334789.2134285 | frequency_hz=319.2
- [2026-08-22 01:53:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334791.7382584 | source=vosk | rms=894 | updated_at=1787334791.7367551 | frequency_hz=319.2
- [2026-08-22 01:53:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334792.7117143 | source=vosk | rms=1202 | updated_at=1787334792.2118669 | frequency_hz=319.2
- [2026-08-22 01:53:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334797.9593513 | source=vosk | rms=1200 | updated_at=1787334797.9593513 | frequency_hz=319.2
- [2026-08-22 01:53:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334798.4575088 | source=vosk | rms=1200 | updated_at=1787334797.9593513 | frequency_hz=319.2
- [2026-08-22 01:53:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334800.7415185 | source=vosk | rms=1200 | updated_at=1787334800.7415185 | frequency_hz=319.2
- [2026-08-22 01:53:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334802.959051 | source=vosk | rms=1201 | updated_at=1787334802.4605536 | frequency_hz=255.1
- [2026-08-22 01:53:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334807.2127159 | source=vosk | rms=173 | updated_at=1787334807.2127159 | frequency_hz=255.1
- [2026-08-22 01:53:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334808.2165637 | source=vosk | rms=173 | updated_at=1787334807.2127159 | frequency_hz=255.1
- [2026-08-22 01:53:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334810.98561 | source=vosk | rms=1200 | updated_at=1787334810.98561 | frequency_hz=255.1
- [2026-08-22 01:53:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334811.7365556 | source=vosk | rms=1119 | updated_at=1787334811.232526 | frequency_hz=255.1
- [2026-08-22 01:53:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334811.99374 | source=vosk | rms=1201 | updated_at=1787334811.99374 | frequency_hz=255.1
- [2026-08-22 01:53:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334812.711783 | source=vosk | rms=1203 | updated_at=1787334812.2068908 | frequency_hz=255.1
- [2026-08-22 01:53:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334813.2204456 | source=vosk | rms=1203 | updated_at=1787334812.2068908 | frequency_hz=255.1
- [2026-08-22 01:53:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334813.712019 | source=vosk | rms=1203 | updated_at=1787334812.2068908 | frequency_hz=255.1
- [2026-08-22 01:53:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334814.0166543 | source=vosk | rms=1202 | updated_at=1787334814.0166543 | frequency_hz=255.1
- [2026-08-22 01:53:37] operator / voice_transcript_partial / voice: german
  meta: kind=partial | timestamp=1787334817.5291457 | source=vosk | rms=215 | updated_at=1787334817.4670084 | frequency_hz=255.1
- [2026-08-22 01:53:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334817.956895 | source=vosk | rms=215 | updated_at=1787334817.4670084 | frequency_hz=255.1
- [2026-08-22 01:53:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334818.20755 | source=vosk | rms=334 | updated_at=1787334818.20755 | frequency_hz=255.1
- [2026-08-22 01:53:38] operator / voice_transcript_partial / voice: german shepherd
  meta: kind=partial | timestamp=1787334818.2272658 | source=vosk | rms=334 | updated_at=1787334818.20755 | frequency_hz=255.1
- [2026-08-22 01:53:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334818.4573495 | source=vosk | rms=334 | updated_at=1787334818.4573495 | frequency_hz=255.1
- [2026-08-22 01:53:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334818.7185783 | source=vosk | rms=334 | updated_at=1787334818.4573495 | frequency_hz=255.1
- [2026-08-22 01:53:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334818.9576678 | source=vosk | rms=340 | updated_at=1787334818.9576678 | frequency_hz=255.1
- [2026-08-22 01:53:39] operator / voice_transcript_final / voice: german shepherd
  meta: kind=final | timestamp=1787334819.2792943 | source=final | rms=340 | updated_at=1787334818.9576678 | frequency_hz=255.1
- [2026-08-22 01:53:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334819.3415053 | source=vosk | rms=341 | updated_at=1787334819.3415053 | frequency_hz=255.1
- [2026-08-22 01:53:41] operator / voice_transcript_partial / voice: i could give
  meta: kind=partial | timestamp=1787334821.2192874 | source=vosk | rms=1005 | updated_at=1787334821.1355078 | frequency_hz=255.1
- [2026-08-22 01:53:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334821.3504903 | source=vosk | rms=1204 | updated_at=1787334821.3504903 | frequency_hz=255.1
- [2026-08-22 01:53:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334821.5982213 | source=vosk | rms=1204 | updated_at=1787334821.3504903 | frequency_hz=255.1
- [2026-08-22 01:53:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334821.8473878 | source=vosk | rms=1204 | updated_at=1787334821.3504903 | frequency_hz=255.1
- [2026-08-22 01:53:42] operator / voice_transcript_final / voice: i could give favorite
  meta: kind=final | timestamp=1787334822.2216852 | source=final | rms=1204 | updated_at=1787334821.3504903 | frequency_hz=255.1
- [2026-08-22 01:53:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334822.3327148 | source=vosk | rms=1204 | updated_at=1787334821.3504903 | frequency_hz=255.1
- [2026-08-22 01:53:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334822.3327148 | source=vosk | rms=402 | updated_at=1787334822.3327148 | frequency_hz=255.1
- [2026-08-22 01:53:42] operator / voice_transcript_partial / voice: you can
  meta: kind=partial | timestamp=1787334822.3933463 | source=vosk | rms=402 | updated_at=1787334822.3327148 | frequency_hz=255.1
- [2026-08-22 01:53:42] operator / voice_transcript_partial / voice: you can develop
  meta: kind=partial | timestamp=1787334822.4868922 | source=vosk | rms=301 | updated_at=1787334822.3933463 | frequency_hz=255.1
- [2026-08-22 01:53:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334822.640457 | source=vosk | rms=1204 | updated_at=1787334822.640457 | frequency_hz=255.1
- [2026-08-22 01:53:42] operator / voice_transcript_partial / voice: you can benefit
  meta: kind=partial | timestamp=1787334822.665319 | source=vosk | rms=1204 | updated_at=1787334822.640457 | frequency_hz=255.1
- [2026-08-22 01:53:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334822.8572085 | source=vosk | rms=1202 | updated_at=1787334822.8572085 | frequency_hz=255.1
- [2026-08-22 01:53:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334823.1533258 | source=vosk | rms=1202 | updated_at=1787334823.1533258 | frequency_hz=255.1
- [2026-08-22 01:53:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334823.4218907 | source=vosk | rms=306 | updated_at=1787334823.4218907 | frequency_hz=255.1
- [2026-08-22 01:53:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334823.626987 | source=vosk | rms=306 | updated_at=1787334823.4218907 | frequency_hz=255.1
- [2026-08-22 01:53:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334824.1551015 | source=vosk | rms=306 | updated_at=1787334823.4218907 | frequency_hz=255.1
- [2026-08-22 01:53:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334825.3772883 | source=vosk | rms=306 | updated_at=1787334823.4218907 | frequency_hz=255.1
- [2026-08-22 01:53:45] operator / voice_transcript_partial / voice: you can benefit the going to be
  meta: kind=partial | timestamp=1787334825.4343035 | source=vosk | rms=306 | updated_at=1787334823.4218907 | frequency_hz=255.1
- [2026-08-22 01:53:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334825.8776515 | source=vosk | rms=306 | updated_at=1787334823.4218907 | frequency_hz=255.1
- [2026-08-22 01:53:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334826.3770125 | source=vosk | rms=483 | updated_at=1787334826.3770125 | frequency_hz=255.1
- [2026-08-22 01:53:46] operator / voice_transcript_partial / voice: people that i'm gonna do you
  meta: kind=partial | timestamp=1787334826.4094253 | source=vosk | rms=483 | updated_at=1787334826.3770125 | frequency_hz=255.1
- [2026-08-22 01:53:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334826.6635554 | source=vosk | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334827.3778121 | source=vosk | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334827.628434 | source=vosk | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334828.1280603 | source=vosk | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334828.4124851 | source=vosk | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:48] operator / voice_transcript_final / voice: you can benefit the going to be of
  meta: kind=final | timestamp=1787334828.8536878 | source=final | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334828.9834538 | source=vosk | rms=314 | updated_at=1787334826.6635554 | frequency_hz=255.1
- [2026-08-22 01:53:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334829.6686985 | source=vosk | rms=1204 | updated_at=1787334829.6686985 | frequency_hz=255.1
- [2026-08-22 01:53:51] operator / voice_transcript_partial / voice: the that
  meta: kind=partial | timestamp=1787334831.1751666 | source=vosk | rms=382 | updated_at=1787334830.9053328 | frequency_hz=255.1
- [2026-08-22 01:53:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334831.3776376 | source=vosk | rms=477 | updated_at=1787334831.3776376 | frequency_hz=255.1
- [2026-08-22 01:53:51] operator / voice_transcript_partial / voice: predicted i'm not
  meta: kind=partial | timestamp=1787334831.427898 | source=vosk | rms=477 | updated_at=1787334831.3776376 | frequency_hz=255.1
- [2026-08-22 01:53:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334831.6505659 | source=vosk | rms=477 | updated_at=1787334831.3776376 | frequency_hz=255.1
- [2026-08-22 01:53:51] operator / voice_transcript_partial / voice: predicted i'm not good
  meta: kind=partial | timestamp=1787334831.725898 | source=vosk | rms=477 | updated_at=1787334831.3776376 | frequency_hz=255.1
- [2026-08-22 01:53:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334831.9071438 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:51] operator / voice_transcript_partial / voice: it didn't have gotten
  meta: kind=partial | timestamp=1787334831.9724567 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334832.1815772 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:52] operator / voice_transcript_partial / voice: it didn't work out the
  meta: kind=partial | timestamp=1787334832.2305512 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334832.9085724 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334835.3786025 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:55] operator / voice_transcript_partial / voice: it didn't work out the empirical
  meta: kind=partial | timestamp=1787334835.455861 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334835.904165 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334836.4133158 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334836.9105623 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334838.1273036 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334838.6315484 | source=vosk | rms=580 | updated_at=1787334831.9071438 | frequency_hz=255.1
- [2026-08-22 01:53:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334839.1760073 | source=vosk | rms=1203 | updated_at=1787334839.1760073 | frequency_hz=255.1
- [2026-08-22 01:53:59] operator / voice_transcript_partial / voice: it didn't work out the empirical do about it
  meta: kind=partial | timestamp=1787334839.2643476 | source=vosk | rms=1203 | updated_at=1787334839.1760073 | frequency_hz=255.1
- [2026-08-22 01:53:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334839.3905308 | source=vosk | rms=1203 | updated_at=1787334839.3905308 | frequency_hz=255.1
- [2026-08-22 01:53:59] operator / voice_transcript_partial / voice: it didn't work out the empirical about
  meta: kind=partial | timestamp=1787334839.4927337 | source=vosk | rms=1203 | updated_at=1787334839.3905308 | frequency_hz=255.1
- [2026-08-22 01:53:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334839.6726487 | source=vosk | rms=1200 | updated_at=1787334839.671649 | frequency_hz=255.1
- [2026-08-22 01:54:00] operator / voice_transcript_final / voice: it didn t work out the empirical do about it
  meta: kind=final | timestamp=1787334840.1898458 | source=final | rms=1200 | updated_at=1787334839.671649 | frequency_hz=255.1
- [2026-08-22 01:54:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334840.3580828 | source=vosk | rms=1200 | updated_at=1787334839.671649 | frequency_hz=255.1
- [2026-08-22 01:54:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334840.6686666 | source=vosk | rms=1200 | updated_at=1787334839.671649 | frequency_hz=255.1
- [2026-08-22 01:54:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334841.1274338 | source=vosk | rms=1200 | updated_at=1787334839.671649 | frequency_hz=255.1
- [2026-08-22 01:54:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334847.5494425 | source=vosk | rms=255 | updated_at=1787334847.5494425 | frequency_hz=255.1
- [2026-08-22 01:54:07] operator / voice_transcript_partial / voice: what about
  meta: kind=partial | timestamp=1787334847.5645392 | source=vosk | rms=255 | updated_at=1787334847.5494425 | frequency_hz=255.1
- [2026-08-22 01:54:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334848.0189762 | source=vosk | rms=255 | updated_at=1787334847.5494425 | frequency_hz=255.1
- [2026-08-22 01:54:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334850.518055 | source=vosk | rms=284 | updated_at=1787334850.518055 | frequency_hz=255.1
- [2026-08-22 01:54:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334851.1238308 | source=vosk | rms=1202 | updated_at=1787334851.1238308 | frequency_hz=255.1
- [2026-08-22 01:54:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334851.5664608 | source=vosk | rms=846 | updated_at=1787334851.5664608 | frequency_hz=255.1
- [2026-08-22 01:54:11] operator / voice_transcript_final / voice: what can you do
  meta: kind=final | timestamp=1787334851.9629016 | source=final | rms=846 | updated_at=1787334851.5664608 | frequency_hz=255.1
- [2026-08-22 01:54:12] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787334852.0395455 | source=state | rms=846 | updated_at=1787334851.5664608 | frequency_hz=255.1
- [2026-08-22 01:54:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334852.0395455 | source=state | rms=846 | updated_at=1787334851.5664608 | frequency_hz=255.1
- [2026-08-22 01:54:12] operator / voice_command / voice: what can you do
  meta: normalized=True
- [2026-08-22 01:54:12] assistant / assistant_prompt / text: Right now I can answer questions, help explain Smart Sentry, run diagnostics when you ask, and handle supported commands.
  meta: task_kind=prompt | speak_requested=True
- [2026-08-22 01:54:13] assistant / spoken_reply / voice: Right now I can answer questions, help explain Smart Sentry, run diagnostics when you ask, and handle supported commands.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-08-22 01:54:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334856.0216048 | source=vosk | rms=249 | updated_at=1787334856.0216048 | frequency_hz=255.1
- [2026-08-22 01:54:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334856.5175884 | source=vosk | rms=249 | updated_at=1787334856.0216048 | frequency_hz=255.1
- [2026-08-22 01:54:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334856.775981 | source=vosk | rms=593 | updated_at=1787334856.775981 | frequency_hz=255.1
- [2026-08-22 01:54:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334858.9319844 | source=vosk | rms=518 | updated_at=1787334858.271229 | frequency_hz=255.1
- [2026-08-22 01:54:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334858.9319844 | source=vosk | rms=229 | updated_at=1787334858.9319844 | frequency_hz=255.1
- [2026-08-22 01:54:24] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command
  meta: kind=partial | timestamp=1787334864.817355 | source=vosk | rms=197 | updated_at=1787334864.7897778 | frequency_hz=244.2
- [2026-08-22 01:54:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334865.2878327 | source=vosk | rms=197 | updated_at=1787334864.7897778 | frequency_hz=244.2
- [2026-08-22 01:54:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334866.5449839 | source=vosk | rms=413 | updated_at=1787334866.5449839 | frequency_hz=244.2
- [2026-08-22 01:54:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334866.7680008 | source=vosk | rms=271 | updated_at=1787334866.7680008 | frequency_hz=244.2
- [2026-08-22 01:54:26] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop
  meta: kind=partial | timestamp=1787334866.8729289 | source=vosk | rms=271 | updated_at=1787334866.7680008 | frequency_hz=244.2
- [2026-08-22 01:54:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334867.021557 | source=vosk | rms=211 | updated_at=1787334867.021557 | frequency_hz=244.2
- [2026-08-22 01:54:27] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to
  meta: kind=partial | timestamp=1787334867.119902 | source=vosk | rms=211 | updated_at=1787334867.021557 | frequency_hz=244.2
- [2026-08-22 01:54:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334867.2681813 | source=vosk | rms=345 | updated_at=1787334867.2681813 | frequency_hz=244.2
- [2026-08-22 01:54:27] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to compile
  meta: kind=partial | timestamp=1787334867.588368 | source=vosk | rms=345 | updated_at=1787334867.2681813 | frequency_hz=244.2
- [2026-08-22 01:54:27] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to can have been
  meta: kind=partial | timestamp=1787334867.736409 | source=vosk | rms=453 | updated_at=1787334867.5888803 | frequency_hz=244.2
- [2026-08-22 01:54:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334867.7680516 | source=vosk | rms=263 | updated_at=1787334867.7680516 | frequency_hz=244.2
- [2026-08-22 01:54:27] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a
  meta: kind=partial | timestamp=1787334867.8863099 | source=vosk | rms=263 | updated_at=1787334867.7680516 | frequency_hz=244.2
- [2026-08-22 01:54:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334868.0212195 | source=vosk | rms=263 | updated_at=1787334867.7680516 | frequency_hz=244.2
- [2026-08-22 01:54:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334868.5183904 | source=vosk | rms=891 | updated_at=1787334868.5183904 | frequency_hz=244.2
- [2026-08-22 01:54:28] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a person but
  meta: kind=partial | timestamp=1787334868.6306298 | source=vosk | rms=891 | updated_at=1787334868.5183904 | frequency_hz=244.2
- [2026-08-22 01:54:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334868.7679732 | source=vosk | rms=282 | updated_at=1787334868.7679732 | frequency_hz=244.2
- [2026-08-22 01:54:28] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a be seen by millions
  meta: kind=partial | timestamp=1787334868.8581157 | source=vosk | rms=282 | updated_at=1787334868.7679732 | frequency_hz=244.2
- [2026-08-22 01:54:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334869.0481405 | source=vosk | rms=406 | updated_at=1787334869.0481405 | frequency_hz=244.2
- [2026-08-22 01:54:29] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a person but my little
  meta: kind=partial | timestamp=1787334869.161505 | source=vosk | rms=406 | updated_at=1787334869.0481405 | frequency_hz=244.2
- [2026-08-22 01:54:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334869.5188336 | source=vosk | rms=269 | updated_at=1787334869.5188336 | frequency_hz=244.2
- [2026-08-22 01:54:29] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a person but my goal is
  meta: kind=partial | timestamp=1787334869.5586684 | source=vosk | rms=269 | updated_at=1787334869.5188336 | frequency_hz=244.2
- [2026-08-22 01:54:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334869.7681646 | source=vosk | rms=319 | updated_at=1787334869.7681646 | frequency_hz=244.2
- [2026-08-22 01:54:29] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a person but my little go to shit but
  meta: kind=partial | timestamp=1787334869.8707485 | source=vosk | rms=319 | updated_at=1787334869.7681646 | frequency_hz=244.2
- [2026-08-22 01:54:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334870.5541961 | source=vosk | rms=319 | updated_at=1787334869.7681646 | frequency_hz=244.2
- [2026-08-22 01:54:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334876.2732968 | source=vosk | rms=412 | updated_at=1787334876.2732968 | frequency_hz=244.2
- [2026-08-22 01:54:36] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a person but my little go to shit but i'm
  meta: kind=partial | timestamp=1787334876.4028158 | source=vosk | rms=412 | updated_at=1787334876.2732968 | frequency_hz=244.2
- [2026-08-22 01:54:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334877.0741398 | source=vosk | rms=412 | updated_at=1787334876.2732968 | frequency_hz=244.2
- [2026-08-22 01:54:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334878.7679224 | source=vosk | rms=471 | updated_at=1787334878.7679224 | frequency_hz=244.2
- [2026-08-22 01:54:38] operator / voice_transcript_partial / voice: right now i can answer questions help explain smart century run diagnostics when you asked and handle supported command gop gonna go to guy putting a person but my little go to shit but i'm gonna lose
  meta: kind=partial | timestamp=1787334878.8318794 | source=vosk | rms=471 | updated_at=1787334878.7679224 | frequency_hz=244.2
- [2026-08-22 01:54:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334879.0180948 | source=vosk | rms=471 | updated_at=1787334878.7679224 | frequency_hz=244.2
- [2026-08-22 01:54:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334879.5178986 | source=vosk | rms=471 | updated_at=1787334878.7679224 | frequency_hz=244.2
- [2026-08-22 01:54:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334880.2678268 | source=vosk | rms=1203 | updated_at=1787334880.2678268 | frequency_hz=244.2
- [2026-08-22 01:54:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334880.76824 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334881.0527377 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:41] operator / voice_transcript_final / voice: run diagnostics
  meta: kind=final | timestamp=1787334881.379417 | source=final | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334882.026981 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334882.026981 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334883.017891 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334883.7142963 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334884.208113 | source=vosk | rms=1201 | updated_at=1787334880.76824 | frequency_hz=244.2
- [2026-08-22 01:54:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334893.463066 | source=vosk | rms=395 | updated_at=1787334893.463066 | frequency_hz=244.2
- [2026-08-22 01:54:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334893.9643536 | source=vosk | rms=395 | updated_at=1787334893.463066 | frequency_hz=244.2
- [2026-08-22 01:54:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334897.2220476 | source=vosk | rms=395 | updated_at=1787334893.463066 | frequency_hz=244.2
- [2026-08-22 01:54:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334898.7195108 | source=vosk | rms=1201 | updated_at=1787334898.225578 | frequency_hz=244.2
- [2026-08-22 01:55:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334903.989163 | source=vosk | rms=469 | updated_at=1787334903.989163 | frequency_hz=244.2
- [2026-08-22 01:55:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334905.4584374 | source=vosk | rms=269 | updated_at=1787334904.957538 | frequency_hz=244.2
- [2026-08-22 01:55:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334905.9593024 | source=vosk | rms=269 | updated_at=1787334904.957538 | frequency_hz=244.2
- [2026-08-22 01:55:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334906.7313201 | source=vosk | rms=120 | updated_at=1787334906.2517338 | frequency_hz=244.2
- [2026-08-22 01:55:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334907.708714 | source=vosk | rms=120 | updated_at=1787334906.2517338 | frequency_hz=244.2
- [2026-08-22 01:55:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334908.5864308 | source=vosk | rms=120 | updated_at=1787334906.2517338 | frequency_hz=244.2
- [2026-08-22 01:55:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334910.4470694 | source=vosk | rms=120 | updated_at=1787334906.2517338 | frequency_hz=244.2
- [2026-08-22 01:55:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334910.9597528 | source=vosk | rms=120 | updated_at=1787334906.2517338 | frequency_hz=244.2
- [2026-08-22 01:55:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334919.199291 | source=vosk | rms=174 | updated_at=1787334919.199291 | frequency_hz=244.2
- [2026-08-22 01:55:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334919.697758 | source=vosk | rms=174 | updated_at=1787334919.199291 | frequency_hz=244.2
- [2026-08-22 01:55:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334920.4479926 | source=vosk | rms=778 | updated_at=1787334920.4479926 | frequency_hz=244.2
- [2026-08-22 01:55:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334921.215559 | source=vosk | rms=177 | updated_at=1787334920.7069788 | frequency_hz=244.2
- [2026-08-22 01:55:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334921.69766 | source=vosk | rms=210 | updated_at=1787334921.69766 | frequency_hz=244.2
- [2026-08-22 01:55:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334922.9554925 | source=vosk | rms=176 | updated_at=1787334922.4535222 | frequency_hz=244.2
- [2026-08-22 01:55:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334924.2459655 | source=vosk | rms=176 | updated_at=1787334922.4535222 | frequency_hz=244.2
- [2026-08-22 01:55:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334925.2056477 | source=vosk | rms=176 | updated_at=1787334922.4535222 | frequency_hz=244.2
- [2026-08-22 01:55:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334925.6986043 | source=vosk | rms=176 | updated_at=1787334922.4535222 | frequency_hz=244.2
- [2026-08-22 01:55:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334926.4472346 | source=vosk | rms=133 | updated_at=1787334925.9542038 | frequency_hz=244.2
- [2026-08-22 01:55:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334927.7115533 | source=vosk | rms=238 | updated_at=1787334927.7115533 | frequency_hz=244.2
- [2026-08-22 01:55:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334929.947263 | source=vosk | rms=161 | updated_at=1787334928.6972435 | frequency_hz=244.2
- [2026-08-22 01:55:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334930.2026024 | source=vosk | rms=161 | updated_at=1787334928.6972435 | frequency_hz=244.2
- [2026-08-22 01:55:30] operator / voice_transcript_partial / voice: stop me
  meta: kind=partial | timestamp=1787334930.2789297 | source=vosk | rms=161 | updated_at=1787334928.6972435 | frequency_hz=244.2
- [2026-08-22 01:55:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334930.7181084 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334931.1989706 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334932.7219203 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334933.2022893 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334936.9515295 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:38] operator / voice_transcript_final / voice: they stop me
  meta: kind=final | timestamp=1787334938.3720012 | source=final | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334938.7431831 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334938.7431831 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334939.1975973 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334941.2098835 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334941.697384 | source=vosk | rms=468 | updated_at=1787334930.7181084 | frequency_hz=244.2
- [2026-08-22 01:55:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334942.948934 | source=vosk | rms=176 | updated_at=1787334942.948934 | frequency_hz=244.2
- [2026-08-22 01:55:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334944.1982443 | source=vosk | rms=176 | updated_at=1787334942.948934 | frequency_hz=244.2
- [2026-08-22 01:55:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334944.454027 | source=vosk | rms=176 | updated_at=1787334942.948934 | frequency_hz=244.2
- [2026-08-22 01:55:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334944.9484046 | source=vosk | rms=176 | updated_at=1787334942.948934 | frequency_hz=244.2
- [2026-08-22 01:55:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334947.9536915 | source=vosk | rms=176 | updated_at=1787334942.948934 | frequency_hz=244.2
- [2026-08-22 01:55:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334948.461302 | source=vosk | rms=176 | updated_at=1787334942.948934 | frequency_hz=244.2
- [2026-08-22 01:55:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334949.725634 | source=vosk | rms=1012 | updated_at=1787334949.725634 | frequency_hz=240.0
- [2026-08-22 01:55:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334951.1975856 | source=vosk | rms=888 | updated_at=1787334950.7350047 | frequency_hz=302.3
- [2026-08-22 01:55:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334951.7019997 | source=vosk | rms=122 | updated_at=1787334951.7019997 | frequency_hz=302.3
- [2026-08-22 01:55:53] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787334953.0325644 | source=vosk | rms=125 | updated_at=1787334952.9578564 | frequency_hz=302.3
- [2026-08-22 01:55:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334953.4877214 | source=vosk | rms=125 | updated_at=1787334952.9578564 | frequency_hz=302.3
- [2026-08-22 01:55:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334953.7045214 | source=vosk | rms=125 | updated_at=1787334952.9578564 | frequency_hz=302.3
- [2026-08-22 01:55:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334954.2358127 | source=vosk | rms=125 | updated_at=1787334952.9578564 | frequency_hz=302.3
- [2026-08-22 01:55:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334955.4482663 | source=vosk | rms=1205 | updated_at=1787334955.4482663 | frequency_hz=302.3
- [2026-08-22 01:55:55] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1787334955.706749 | source=final | rms=1205 | updated_at=1787334955.4482663 | frequency_hz=302.3
- [2026-08-22 01:55:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334955.7495575 | source=vosk | rms=827 | updated_at=1787334955.7495575 | frequency_hz=300.8
- [2026-08-22 01:55:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334956.6986544 | source=vosk | rms=827 | updated_at=1787334955.7495575 | frequency_hz=300.8
- [2026-08-22 01:55:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334957.6976204 | source=vosk | rms=463 | updated_at=1787334957.6976204 | frequency_hz=300.8
- [2026-08-22 01:55:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334958.2583117 | source=vosk | rms=463 | updated_at=1787334957.6976204 | frequency_hz=300.8
- [2026-08-22 01:55:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334958.4781277 | source=vosk | rms=437 | updated_at=1787334958.4781277 | frequency_hz=300.8
- [2026-08-22 01:55:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334959.4525778 | source=vosk | rms=220 | updated_at=1787334958.7447605 | frequency_hz=300.8
- [2026-08-22 01:55:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334959.6982863 | source=vosk | rms=254 | updated_at=1787334959.6982863 | frequency_hz=300.8
- [2026-08-22 01:55:59] operator / voice_transcript_partial / voice: so
  meta: kind=partial | timestamp=1787334959.7103994 | source=vosk | rms=254 | updated_at=1787334959.6982863 | frequency_hz=300.8
- [2026-08-22 01:55:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334959.9492002 | source=vosk | rms=152 | updated_at=1787334959.9492002 | frequency_hz=300.8
- [2026-08-22 01:56:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334960.214997 | source=vosk | rms=155 | updated_at=1787334960.214997 | frequency_hz=300.8
- [2026-08-22 01:56:00] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1787334960.4470203 | source=final | rms=155 | updated_at=1787334960.214997 | frequency_hz=300.8
- [2026-08-22 01:56:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334960.700573 | source=vosk | rms=155 | updated_at=1787334960.214997 | frequency_hz=300.8
- [2026-08-22 01:56:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334965.4479704 | source=vosk | rms=155 | updated_at=1787334960.214997 | frequency_hz=300.8
- [2026-08-22 01:56:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334965.9491727 | source=vosk | rms=155 | updated_at=1787334960.214997 | frequency_hz=300.8
- [2026-08-22 01:56:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334968.2026079 | source=vosk | rms=553 | updated_at=1787334968.2026079 | frequency_hz=300.8
- [2026-08-22 01:56:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334969.0070674 | source=vosk | rms=222 | updated_at=1787334968.4480398 | frequency_hz=300.8
- [2026-08-22 01:56:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334969.1977382 | source=vosk | rms=222 | updated_at=1787334968.4480398 | frequency_hz=300.8
- [2026-08-22 01:56:09] operator / voice_transcript_partial / voice: okay with
  meta: kind=partial | timestamp=1787334969.990624 | source=vosk | rms=153 | updated_at=1787334969.4521892 | frequency_hz=300.8
- [2026-08-22 01:56:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334970.2095191 | source=vosk | rms=153 | updated_at=1787334969.4521892 | frequency_hz=300.8
- [2026-08-22 01:56:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334970.448277 | source=vosk | rms=153 | updated_at=1787334969.4521892 | frequency_hz=300.8
- [2026-08-22 01:56:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334970.768103 | source=vosk | rms=329 | updated_at=1787334970.768103 | frequency_hz=300.8
- [2026-08-22 01:56:11] operator / voice_transcript_final / voice: okay with
  meta: kind=final | timestamp=1787334971.2927363 | source=final | rms=329 | updated_at=1787334970.768103 | frequency_hz=300.8
- [2026-08-22 01:56:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334971.3406498 | source=vosk | rms=329 | updated_at=1787334970.768103 | frequency_hz=300.8
- [2026-08-22 01:56:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334971.3406498 | source=vosk | rms=411 | updated_at=1787334971.3406498 | frequency_hz=300.8
- [2026-08-22 01:56:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334971.9534016 | source=vosk | rms=411 | updated_at=1787334971.3406498 | frequency_hz=300.8
- [2026-08-22 01:56:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334973.2024806 | source=vosk | rms=1199 | updated_at=1787334973.20148 | frequency_hz=300.8
- [2026-08-22 01:56:13] operator / voice_transcript_partial / voice: since
  meta: kind=partial | timestamp=1787334973.2811315 | source=vosk | rms=1199 | updated_at=1787334973.20148 | frequency_hz=300.8
- [2026-08-22 01:56:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334973.4835181 | source=vosk | rms=1200 | updated_at=1787334973.4835181 | frequency_hz=300.8
- [2026-08-22 01:56:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334973.6981604 | source=vosk | rms=1200 | updated_at=1787334973.6981604 | frequency_hz=300.8
- [2026-08-22 01:56:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334973.9846926 | source=vosk | rms=1205 | updated_at=1787334973.9846926 | frequency_hz=300.8
- [2026-08-22 01:56:14] operator / voice_transcript_final / voice: says
  meta: kind=final | timestamp=1787334974.2425342 | source=final | rms=1205 | updated_at=1787334973.9846926 | frequency_hz=300.8
- [2026-08-22 01:56:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334974.4819515 | source=vosk | rms=1205 | updated_at=1787334973.9846926 | frequency_hz=300.8
- [2026-08-22 01:56:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334975.2181363 | source=vosk | rms=1205 | updated_at=1787334973.9846926 | frequency_hz=300.8
- [2026-08-22 01:56:15] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1787334975.747937 | source=vosk | rms=171 | updated_at=1787334975.71192 | frequency_hz=300.8
- [2026-08-22 01:56:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334975.9483783 | source=vosk | rms=171 | updated_at=1787334975.71192 | frequency_hz=300.8
- [2026-08-22 01:56:15] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1787334975.9708943 | source=vosk | rms=171 | updated_at=1787334975.71192 | frequency_hz=300.8
- [2026-08-22 01:56:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334976.447847 | source=vosk | rms=171 | updated_at=1787334975.71192 | frequency_hz=300.8
- [2026-08-22 01:56:16] operator / voice_transcript_partial / voice: to plan that
  meta: kind=partial | timestamp=1787334976.4749014 | source=vosk | rms=171 | updated_at=1787334975.71192 | frequency_hz=300.8
- [2026-08-22 01:56:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334976.7331133 | source=vosk | rms=190 | updated_at=1787334976.7331133 | frequency_hz=300.8
- [2026-08-22 01:56:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334976.9642131 | source=vosk | rms=190 | updated_at=1787334976.7331133 | frequency_hz=300.8
- [2026-08-22 01:56:16] operator / voice_transcript_partial / voice: to plan that be a
  meta: kind=partial | timestamp=1787334976.991328 | source=vosk | rms=190 | updated_at=1787334976.7331133 | frequency_hz=300.8
- [2026-08-22 01:56:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334977.2407331 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334977.5255141 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334978.2294266 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334978.6998477 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:19] operator / voice_transcript_final / voice: to plan that be a paper
  meta: kind=final | timestamp=1787334979.312216 | source=final | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334979.4230797 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334979.4230797 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334980.4949005 | source=vosk | rms=142 | updated_at=1787334977.2407331 | frequency_hz=300.8
- [2026-08-22 01:56:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334980.9975808 | source=vosk | rms=329 | updated_at=1787334980.9975808 | frequency_hz=300.8
- [2026-08-22 01:56:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334981.7210488 | source=vosk | rms=166 | updated_at=1787334981.2518258 | frequency_hz=300.8
- [2026-08-22 01:56:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334988.2026322 | source=vosk | rms=166 | updated_at=1787334981.2518258 | frequency_hz=300.8
- [2026-08-22 01:56:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334990.2415066 | source=vosk | rms=299 | updated_at=1787334989.7070813 | frequency_hz=300.8
- [2026-08-22 01:56:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334990.9478776 | source=vosk | rms=342 | updated_at=1787334990.9478776 | frequency_hz=300.8
- [2026-08-22 01:56:32] operator / voice_transcript_partial / voice: oh crap oh by
  meta: kind=partial | timestamp=1787334992.9728453 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334993.4514773 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334996.202882 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:36] operator / voice_transcript_partial / voice: oh crap a biopsy
  meta: kind=partial | timestamp=1787334996.2649071 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334996.4496336 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:36] operator / voice_transcript_partial / voice: or crapo biopsies
  meta: kind=partial | timestamp=1787334996.5046778 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334996.6982179 | source=vosk | rms=218 | updated_at=1787334992.4479713 | frequency_hz=300.8
- [2026-08-22 01:56:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334997.2001238 | source=vosk | rms=734 | updated_at=1787334997.2001238 | frequency_hz=300.8
- [2026-08-22 01:56:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334997.4486647 | source=vosk | rms=1200 | updated_at=1787334997.4486647 | frequency_hz=300.8
- [2026-08-22 01:56:37] operator / voice_transcript_final / voice: or crap a biopsy
  meta: kind=final | timestamp=1787334997.9363396 | source=final | rms=1200 | updated_at=1787334997.4486647 | frequency_hz=300.8
- [2026-08-22 01:56:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334998.0602684 | source=vosk | rms=1200 | updated_at=1787334997.4486647 | frequency_hz=300.8
- [2026-08-22 01:56:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787334998.1986723 | source=vosk | rms=1200 | updated_at=1787334997.4486647 | frequency_hz=300.8
- [2026-08-22 01:56:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787334998.9481654 | source=vosk | rms=1200 | updated_at=1787334997.4486647 | frequency_hz=300.8
- [2026-08-22 01:56:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335001.7414227 | source=vosk | rms=1200 | updated_at=1787334997.4486647 | frequency_hz=300.8
- [2026-08-22 01:56:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335003.2383144 | source=vosk | rms=160 | updated_at=1787335002.5700321 | frequency_hz=300.8
- [2026-08-22 01:56:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335003.7385952 | source=vosk | rms=154 | updated_at=1787335003.7385952 | frequency_hz=300.8
- [2026-08-22 01:56:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335004.4888422 | source=vosk | rms=331 | updated_at=1787335004.0203824 | frequency_hz=300.8
- [2026-08-22 01:56:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335006.4903915 | source=vosk | rms=127 | updated_at=1787335006.4903915 | frequency_hz=300.8
- [2026-08-22 01:56:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335006.987989 | source=vosk | rms=127 | updated_at=1787335006.4903915 | frequency_hz=300.8
- [2026-08-22 01:56:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335007.9887788 | source=vosk | rms=1200 | updated_at=1787335007.9887788 | frequency_hz=300.8
- [2026-08-22 01:56:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335009.2532818 | source=vosk | rms=1203 | updated_at=1787335008.2399583 | frequency_hz=300.8
- [2026-08-22 01:56:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335012.7484438 | source=vosk | rms=228 | updated_at=1787335012.7484438 | frequency_hz=300.8
- [2026-08-22 01:56:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335013.2553027 | source=vosk | rms=228 | updated_at=1787335012.7484438 | frequency_hz=300.8
- [2026-08-22 01:56:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335016.5364652 | source=vosk | rms=228 | updated_at=1787335012.7484438 | frequency_hz=300.8
- [2026-08-22 01:56:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335016.9996278 | source=vosk | rms=228 | updated_at=1787335012.7484438 | frequency_hz=300.8
- [2026-08-22 01:56:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335017.5159523 | source=vosk | rms=228 | updated_at=1787335012.7484438 | frequency_hz=300.8
- [2026-08-22 01:56:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335017.9996102 | source=vosk | rms=228 | updated_at=1787335012.7484438 | frequency_hz=300.8
- [2026-08-22 01:56:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335018.4983132 | source=vosk | rms=189 | updated_at=1787335018.4983132 | frequency_hz=300.8
- [2026-08-22 01:56:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335018.9996722 | source=vosk | rms=189 | updated_at=1787335018.4983132 | frequency_hz=300.8
- [2026-08-22 01:57:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335022.0105278 | source=vosk | rms=189 | updated_at=1787335018.4983132 | frequency_hz=300.8
- [2026-08-22 01:57:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335022.511586 | source=vosk | rms=189 | updated_at=1787335018.4983132 | frequency_hz=300.8
- [2026-08-22 01:57:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335023.2733421 | source=vosk | rms=1203 | updated_at=1787335023.2733421 | frequency_hz=300.8
- [2026-08-22 01:57:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335025.51748 | source=vosk | rms=262 | updated_at=1787335025.0472715 | frequency_hz=300.8
- [2026-08-22 01:57:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335026.2815924 | source=vosk | rms=286 | updated_at=1787335026.2815924 | frequency_hz=300.8
- [2026-08-22 01:57:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335029.138853 | source=vosk | rms=270 | updated_at=1787335028.6425707 | frequency_hz=300.8
- [2026-08-22 01:57:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335030.902853 | source=vosk | rms=270 | updated_at=1787335028.6425707 | frequency_hz=300.8
- [2026-08-22 01:57:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335031.9265828 | source=vosk | rms=1206 | updated_at=1787335031.3887515 | frequency_hz=300.8
- [2026-08-22 01:57:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335032.388341 | source=vosk | rms=127 | updated_at=1787335032.388341 | frequency_hz=300.8
- [2026-08-22 01:57:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335035.4037547 | source=vosk | rms=1204 | updated_at=1787335034.3885353 | frequency_hz=300.8
- [2026-08-22 01:57:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335036.686985 | source=vosk | rms=125 | updated_at=1787335036.686985 | frequency_hz=300.8
- [2026-08-22 01:57:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335038.1634343 | source=vosk | rms=271 | updated_at=1787335037.3882613 | frequency_hz=300.8
- [2026-08-22 01:57:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335038.889883 | source=vosk | rms=271 | updated_at=1787335037.3882613 | frequency_hz=300.8
- [2026-08-22 01:57:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335039.3986197 | source=vosk | rms=271 | updated_at=1787335037.3882613 | frequency_hz=300.8
- [2026-08-22 01:57:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335043.888666 | source=vosk | rms=1577 | updated_at=1787335043.888666 | frequency_hz=300.8
- [2026-08-22 01:57:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335046.1437914 | source=vosk | rms=234 | updated_at=1787335044.3885033 | frequency_hz=300.8
- [2026-08-22 01:57:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335047.8891222 | source=vosk | rms=234 | updated_at=1787335044.3885033 | frequency_hz=300.8
- [2026-08-22 01:57:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335048.4090166 | source=vosk | rms=234 | updated_at=1787335044.3885033 | frequency_hz=300.8
- [2026-08-22 01:57:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335049.1383374 | source=vosk | rms=722 | updated_at=1787335049.1383374 | frequency_hz=300.8
- [2026-08-22 01:57:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335049.9047878 | source=vosk | rms=722 | updated_at=1787335049.1383374 | frequency_hz=300.8
- [2026-08-22 01:57:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335051.1954718 | source=vosk | rms=722 | updated_at=1787335049.1383374 | frequency_hz=300.8
- [2026-08-22 01:57:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335051.6749651 | source=vosk | rms=722 | updated_at=1787335049.1383374 | frequency_hz=300.8
- [2026-08-22 01:57:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335054.3882165 | source=vosk | rms=203 | updated_at=1787335054.3882165 | frequency_hz=300.8
- [2026-08-22 01:57:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335054.8884697 | source=vosk | rms=203 | updated_at=1787335054.3882165 | frequency_hz=300.8
- [2026-08-22 01:57:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335056.164394 | source=vosk | rms=203 | updated_at=1787335054.3882165 | frequency_hz=300.8
- [2026-08-22 01:57:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335056.9014027 | source=vosk | rms=203 | updated_at=1787335054.3882165 | frequency_hz=300.8
- [2026-08-22 01:57:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335057.6389349 | source=vosk | rms=203 | updated_at=1787335054.3882165 | frequency_hz=300.8
- [2026-08-22 01:57:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335058.1401162 | source=vosk | rms=203 | updated_at=1787335054.3882165 | frequency_hz=300.8
- [2026-08-22 01:57:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335058.6612968 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335059.389333 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335060.8892105 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:40] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1787335060.910144 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335061.3891225 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335064.6344948 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335065.1469095 | source=vosk | rms=374 | updated_at=1787335058.6612968 | frequency_hz=300.8
- [2026-08-22 01:57:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335066.1411405 | source=vosk | rms=167 | updated_at=1787335066.1411405 | frequency_hz=300.8
- [2026-08-22 01:57:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335066.4213102 | source=vosk | rms=167 | updated_at=1787335066.1411405 | frequency_hz=300.8
- [2026-08-22 01:57:46] operator / voice_transcript_final / voice: pics
  meta: kind=final | timestamp=1787335066.7259684 | source=final | rms=167 | updated_at=1787335066.1411405 | frequency_hz=300.8
- [2026-08-22 01:57:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335066.942474 | source=vosk | rms=167 | updated_at=1787335066.1411405 | frequency_hz=300.8
- [2026-08-22 01:57:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335070.687318 | source=vosk | rms=262 | updated_at=1787335070.687318 | frequency_hz=300.8
- [2026-08-22 01:57:56] operator / voice_transcript_final / voice: eric
  meta: kind=final | timestamp=1787335076.7574265 | source=final | rms=208 | updated_at=1787335075.6632285 | frequency_hz=300.8
- [2026-08-22 01:57:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335076.7954843 | source=vosk | rms=346 | updated_at=1787335076.7954843 | frequency_hz=300.8
- [2026-08-22 01:57:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335078.6401772 | source=vosk | rms=401 | updated_at=1787335078.1816087 | frequency_hz=300.8
- [2026-08-22 01:57:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335078.88864 | source=vosk | rms=401 | updated_at=1787335078.1816087 | frequency_hz=300.8
- [2026-08-22 01:57:58] operator / voice_transcript_partial / voice: it took
  meta: kind=partial | timestamp=1787335078.9854062 | source=vosk | rms=401 | updated_at=1787335078.1816087 | frequency_hz=300.8
- [2026-08-22 01:57:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335079.1397126 | source=vosk | rms=401 | updated_at=1787335078.1816087 | frequency_hz=300.8
- [2026-08-22 01:58:00] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1787335080.2116923 | source=vosk | rms=175 | updated_at=1787335080.1452556 | frequency_hz=300.8
- [2026-08-22 01:58:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335080.4471877 | source=vosk | rms=218 | updated_at=1787335080.4471877 | frequency_hz=300.8
- [2026-08-22 01:58:00] operator / voice_transcript_partial / voice: today than it did it
  meta: kind=partial | timestamp=1787335080.495884 | source=vosk | rms=218 | updated_at=1787335080.4471877 | frequency_hz=300.8
- [2026-08-22 01:58:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335081.1756167 | source=vosk | rms=218 | updated_at=1787335080.4471877 | frequency_hz=300.8
- [2026-08-22 01:58:01] operator / voice_transcript_partial / voice: it took longer than a good day
  meta: kind=partial | timestamp=1787335081.2935107 | source=vosk | rms=218 | updated_at=1787335080.4471877 | frequency_hz=300.8
- [2026-08-22 01:58:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335081.3892813 | source=vosk | rms=213 | updated_at=1787335081.3892813 | frequency_hz=300.8
- [2026-08-22 01:58:01] operator / voice_transcript_partial / voice: today than it did they
  meta: kind=partial | timestamp=1787335081.4304268 | source=vosk | rms=213 | updated_at=1787335081.3892813 | frequency_hz=300.8
- [2026-08-22 01:58:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335081.638694 | source=vosk | rms=183 | updated_at=1787335081.638694 | frequency_hz=300.8
- [2026-08-22 01:58:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335081.91769 | source=vosk | rms=183 | updated_at=1787335081.91769 | frequency_hz=300.8
- [2026-08-22 01:58:02] operator / voice_transcript_final / voice: it took longer than it did day
  meta: kind=final | timestamp=1787335082.315779 | source=final | rms=183 | updated_at=1787335081.91769 | frequency_hz=300.8
- [2026-08-22 01:58:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335082.451209 | source=vosk | rms=183 | updated_at=1787335081.91769 | frequency_hz=300.8
- [2026-08-22 01:58:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335082.451209 | source=vosk | rms=470 | updated_at=1787335082.451209 | frequency_hz=300.8
- [2026-08-22 01:58:03] operator / voice_transcript_partial / voice: as mentioned above
  meta: kind=partial | timestamp=1787335083.695786 | source=vosk | rms=359 | updated_at=1787335083.6392398 | frequency_hz=300.8
- [2026-08-22 01:58:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335083.8887646 | source=vosk | rms=551 | updated_at=1787335083.8887646 | frequency_hz=300.8
- [2026-08-22 01:58:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335084.1387572 | source=vosk | rms=551 | updated_at=1787335083.8887646 | frequency_hz=300.8
- [2026-08-22 01:58:04] operator / voice_transcript_final / voice: as mentioned above
  meta: kind=final | timestamp=1787335084.518738 | source=final | rms=551 | updated_at=1787335083.8887646 | frequency_hz=300.8
- [2026-08-22 01:58:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335084.6900818 | source=vosk | rms=551 | updated_at=1787335083.8887646 | frequency_hz=300.8
- [2026-08-22 01:58:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335084.6900818 | source=vosk | rms=183 | updated_at=1787335084.6900818 | frequency_hz=300.8
- [2026-08-22 01:58:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335085.9170752 | source=vosk | rms=385 | updated_at=1787335085.1387913 | frequency_hz=300.8
- [2026-08-22 01:58:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335086.6703389 | source=vosk | rms=275 | updated_at=1787335086.6703389 | frequency_hz=300.8
- [2026-08-22 01:58:06] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787335086.9068036 | source=vosk | rms=420 | updated_at=1787335086.8908966 | frequency_hz=300.8
- [2026-08-22 01:58:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335087.1390495 | source=vosk | rms=420 | updated_at=1787335086.8908966 | frequency_hz=300.8
- [2026-08-22 01:58:07] operator / voice_transcript_partial / voice: the housing
  meta: kind=partial | timestamp=1787335087.2149148 | source=vosk | rms=420 | updated_at=1787335086.8908966 | frequency_hz=300.8
- [2026-08-22 01:58:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335087.417502 | source=vosk | rms=167 | updated_at=1787335087.417502 | frequency_hz=300.8
- [2026-08-22 01:58:07] operator / voice_transcript_partial / voice: the housing and
  meta: kind=partial | timestamp=1787335087.4941194 | source=vosk | rms=167 | updated_at=1787335087.417502 | frequency_hz=300.8
- [2026-08-22 01:58:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335087.6388426 | source=vosk | rms=177 | updated_at=1787335087.6388426 | frequency_hz=300.8
- [2026-08-22 01:58:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335088.1784918 | source=vosk | rms=365 | updated_at=1787335088.1784918 | frequency_hz=300.8
- [2026-08-22 01:58:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335088.3893666 | source=vosk | rms=582 | updated_at=1787335088.3893666 | frequency_hz=300.8
- [2026-08-22 01:58:08] operator / voice_transcript_final / voice: the housing and
  meta: kind=final | timestamp=1787335088.8347962 | source=final | rms=582 | updated_at=1787335088.3893666 | frequency_hz=300.8
- [2026-08-22 01:58:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335088.9758086 | source=vosk | rms=582 | updated_at=1787335088.3893666 | frequency_hz=300.8
- [2026-08-22 01:58:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335088.9758086 | source=vosk | rms=618 | updated_at=1787335088.9758086 | frequency_hz=300.8
- [2026-08-22 01:58:09] operator / voice_transcript_partial / voice: and you
  meta: kind=partial | timestamp=1787335089.0627027 | source=vosk | rms=618 | updated_at=1787335088.9758086 | frequency_hz=300.8
- [2026-08-22 01:58:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335089.2107522 | source=vosk | rms=618 | updated_at=1787335088.9758086 | frequency_hz=300.8
- [2026-08-22 01:58:09] operator / voice_transcript_partial / voice: and you took
  meta: kind=partial | timestamp=1787335089.2663012 | source=vosk | rms=618 | updated_at=1787335088.9758086 | frequency_hz=300.8
- [2026-08-22 01:58:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335089.4300416 | source=vosk | rms=618 | updated_at=1787335088.9758086 | frequency_hz=300.8
- [2026-08-22 01:58:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335089.641213 | source=vosk | rms=294 | updated_at=1787335089.641213 | frequency_hz=300.8
- [2026-08-22 01:58:09] operator / voice_transcript_partial / voice: and you should
  meta: kind=partial | timestamp=1787335089.688548 | source=vosk | rms=294 | updated_at=1787335089.641213 | frequency_hz=300.8
- [2026-08-22 01:58:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335089.903587 | source=vosk | rms=294 | updated_at=1787335089.641213 | frequency_hz=300.8
- [2026-08-22 01:58:09] operator / voice_transcript_partial / voice: and you took
  meta: kind=partial | timestamp=1787335089.9557657 | source=vosk | rms=294 | updated_at=1787335089.641213 | frequency_hz=300.8
- [2026-08-22 01:58:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335090.1815195 | source=vosk | rms=223 | updated_at=1787335090.1815195 | frequency_hz=300.8
- [2026-08-22 01:58:10] operator / voice_transcript_partial / voice: and you took some pictures
  meta: kind=partial | timestamp=1787335090.253215 | source=vosk | rms=223 | updated_at=1787335090.1815195 | frequency_hz=300.8
- [2026-08-22 01:58:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335090.9158823 | source=vosk | rms=223 | updated_at=1787335090.1815195 | frequency_hz=300.8
- [2026-08-22 01:58:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335091.8901384 | source=vosk | rms=518 | updated_at=1787335091.8901384 | frequency_hz=300.8
- [2026-08-22 01:58:11] operator / voice_transcript_partial / voice: and you took some of
  meta: kind=partial | timestamp=1787335091.96648 | source=vosk | rms=518 | updated_at=1787335091.8901384 | frequency_hz=300.8
- [2026-08-22 01:58:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335092.2088037 | source=vosk | rms=1149 | updated_at=1787335092.2088037 | frequency_hz=300.8
- [2026-08-22 01:58:12] operator / voice_transcript_partial / voice: and you should sort of
  meta: kind=partial | timestamp=1787335092.2772005 | source=vosk | rms=1149 | updated_at=1787335092.2088037 | frequency_hz=300.8
- [2026-08-22 01:58:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335092.423094 | source=vosk | rms=1203 | updated_at=1787335092.423094 | frequency_hz=300.8
- [2026-08-22 01:58:12] operator / voice_transcript_partial / voice: and you took some of those living
  meta: kind=partial | timestamp=1787335092.5327568 | source=vosk | rms=1203 | updated_at=1787335092.423094 | frequency_hz=300.8
- [2026-08-22 01:58:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335092.648061 | source=vosk | rms=1200 | updated_at=1787335092.648061 | frequency_hz=300.8
- [2026-08-22 01:58:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335092.8914254 | source=vosk | rms=186 | updated_at=1787335092.8914254 | frequency_hz=300.8
- [2026-08-22 01:58:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335093.1393836 | source=vosk | rms=573 | updated_at=1787335093.1393836 | frequency_hz=300.8
- [2026-08-22 01:58:13] operator / voice_transcript_partial / voice: and you took some of those living in
  meta: kind=partial | timestamp=1787335093.1605024 | source=vosk | rms=573 | updated_at=1787335093.1393836 | frequency_hz=300.8
- [2026-08-22 01:58:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335093.3890395 | source=vosk | rms=530 | updated_at=1787335093.3890395 | frequency_hz=300.8
- [2026-08-22 01:58:13] operator / voice_transcript_final / voice: and you took some of those living
  meta: kind=final | timestamp=1787335093.8798614 | source=final | rms=530 | updated_at=1787335093.3890395 | frequency_hz=300.8
- [2026-08-22 01:58:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335094.0526571 | source=vosk | rms=530 | updated_at=1787335093.3890395 | frequency_hz=300.8
- [2026-08-22 01:58:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335094.0526571 | source=vosk | rms=376 | updated_at=1787335094.0526571 | frequency_hz=300.8
- [2026-08-22 01:58:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335094.6387727 | source=vosk | rms=183 | updated_at=1787335094.1389008 | frequency_hz=300.8
- [2026-08-22 01:58:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335094.8904908 | source=vosk | rms=183 | updated_at=1787335094.1389008 | frequency_hz=300.8
- [2026-08-22 01:58:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335096.4272833 | source=vosk | rms=281 | updated_at=1787335095.6390603 | frequency_hz=300.8
- [2026-08-22 01:58:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335097.677373 | source=vosk | rms=540 | updated_at=1787335097.677373 | frequency_hz=300.8
- [2026-08-22 01:58:18] operator / voice_transcript_partial / voice: that was
  meta: kind=partial | timestamp=1787335098.2749214 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335098.4289372 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:18] operator / voice_transcript_partial / voice: that was before
  meta: kind=partial | timestamp=1787335098.536999 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335099.1404183 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335099.6389813 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:19] operator / voice_transcript_partial / voice: that was
  meta: kind=partial | timestamp=1787335099.722101 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335099.8971996 | source=vosk | rms=337 | updated_at=1787335097.904934 | frequency_hz=300.8
- [2026-08-22 01:58:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335100.402745 | source=vosk | rms=1200 | updated_at=1787335100.402745 | frequency_hz=300.8
- [2026-08-22 01:58:20] operator / voice_transcript_final / voice: not was be
  meta: kind=final | timestamp=1787335100.8074262 | source=final | rms=1200 | updated_at=1787335100.402745 | frequency_hz=300.8
- [2026-08-22 01:58:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335100.950321 | source=vosk | rms=1200 | updated_at=1787335100.402745 | frequency_hz=300.8
- [2026-08-22 01:58:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335100.950321 | source=vosk | rms=1202 | updated_at=1787335100.950321 | frequency_hz=300.8
- [2026-08-22 01:58:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335101.414984 | source=vosk | rms=1202 | updated_at=1787335100.950321 | frequency_hz=300.8
- [2026-08-22 01:58:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335101.6402555 | source=vosk | rms=1202 | updated_at=1787335100.950321 | frequency_hz=300.8
- [2026-08-22 01:58:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335102.8887773 | source=vosk | rms=351 | updated_at=1787335102.1438599 | frequency_hz=300.8
- [2026-08-22 01:58:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335110.388805 | source=vosk | rms=276 | updated_at=1787335110.388805 | frequency_hz=300.8
- [2026-08-22 01:58:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335110.903791 | source=vosk | rms=276 | updated_at=1787335110.388805 | frequency_hz=300.8
- [2026-08-22 01:58:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335113.3892796 | source=vosk | rms=208 | updated_at=1787335113.3892796 | frequency_hz=300.8
- [2026-08-22 01:58:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335114.6838636 | source=vosk | rms=178 | updated_at=1787335114.145854 | frequency_hz=300.8
- [2026-08-22 01:58:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335115.3890185 | source=vosk | rms=178 | updated_at=1787335114.145854 | frequency_hz=300.8
- [2026-08-22 01:58:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335115.8924294 | source=vosk | rms=178 | updated_at=1787335114.145854 | frequency_hz=300.8
- [2026-08-22 01:58:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335116.3889794 | source=vosk | rms=178 | updated_at=1787335114.145854 | frequency_hz=300.8
- [2026-08-22 01:58:36] operator / voice_transcript_partial / voice: it makes
  meta: kind=partial | timestamp=1787335116.7813408 | source=vosk | rms=178 | updated_at=1787335114.145854 | frequency_hz=300.8
- [2026-08-22 01:58:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335117.395288 | source=vosk | rms=178 | updated_at=1787335114.145854 | frequency_hz=300.8
- [2026-08-22 01:58:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335118.8913813 | source=vosk | rms=225 | updated_at=1787335118.8913813 | frequency_hz=300.8
- [2026-08-22 01:58:38] operator / voice_transcript_partial / voice: it became
  meta: kind=partial | timestamp=1787335118.9589279 | source=vosk | rms=225 | updated_at=1787335118.8913813 | frequency_hz=300.8
- [2026-08-22 01:58:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335119.1445236 | source=vosk | rms=225 | updated_at=1787335118.8913813 | frequency_hz=300.8
- [2026-08-22 01:58:39] operator / voice_transcript_partial / voice: make
  meta: kind=partial | timestamp=1787335119.2012632 | source=vosk | rms=225 | updated_at=1787335118.8913813 | frequency_hz=300.8
- [2026-08-22 01:58:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335119.6680713 | source=vosk | rms=225 | updated_at=1787335118.8913813 | frequency_hz=300.8
- [2026-08-22 01:58:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335119.8887799 | source=vosk | rms=189 | updated_at=1787335119.8887799 | frequency_hz=300.8
- [2026-08-22 01:58:40] operator / voice_transcript_final / voice: arabic
  meta: kind=final | timestamp=1787335120.2537692 | source=final | rms=189 | updated_at=1787335119.8887799 | frequency_hz=300.8
- [2026-08-22 01:58:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335120.2924445 | source=vosk | rms=189 | updated_at=1787335119.8887799 | frequency_hz=300.8
- [2026-08-22 01:58:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335121.6715434 | source=vosk | rms=546 | updated_at=1787335121.1690006 | frequency_hz=300.8
- [2026-08-22 01:58:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335122.4078104 | source=vosk | rms=546 | updated_at=1787335121.1690006 | frequency_hz=300.8
- [2026-08-22 01:58:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335123.145003 | source=vosk | rms=546 | updated_at=1787335121.1690006 | frequency_hz=300.8
- [2026-08-22 01:58:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335125.6622925 | source=vosk | rms=178 | updated_at=1787335125.6622925 | frequency_hz=300.8
- [2026-08-22 01:58:46] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787335126.6999195 | source=vosk | rms=178 | updated_at=1787335125.6622925 | frequency_hz=300.8
- [2026-08-22 01:58:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335127.1395402 | source=vosk | rms=178 | updated_at=1787335125.6622925 | frequency_hz=300.8
- [2026-08-22 01:58:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335128.639298 | source=vosk | rms=178 | updated_at=1787335125.6622925 | frequency_hz=300.8
- [2026-08-22 01:58:48] operator / voice_transcript_partial / voice: to be
  meta: kind=partial | timestamp=1787335128.6616223 | source=vosk | rms=178 | updated_at=1787335125.6622925 | frequency_hz=300.8
- [2026-08-22 01:58:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335129.171637 | source=vosk | rms=215 | updated_at=1787335129.171637 | frequency_hz=300.8
- [2026-08-22 01:58:49] operator / voice_transcript_partial / voice: to be here
  meta: kind=partial | timestamp=1787335129.2223477 | source=vosk | rms=215 | updated_at=1787335129.171637 | frequency_hz=300.8
- [2026-08-22 01:58:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335129.6659052 | source=vosk | rms=215 | updated_at=1787335129.171637 | frequency_hz=300.8
- [2026-08-22 01:58:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335129.9423132 | source=vosk | rms=215 | updated_at=1787335129.171637 | frequency_hz=300.8
- [2026-08-22 01:58:49] operator / voice_transcript_partial / voice: to be here with
  meta: kind=partial | timestamp=1787335129.9757988 | source=vosk | rms=215 | updated_at=1787335129.171637 | frequency_hz=300.8
- [2026-08-22 01:58:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335130.1387901 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335130.4185698 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:50] operator / voice_transcript_final / voice: to be here with you
  meta: kind=final | timestamp=1787335130.8655047 | source=final | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335131.0712924 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335131.0712924 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335131.6582682 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335132.399008 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:58:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335133.4386473 | source=vosk | rms=170 | updated_at=1787335130.1387901 | frequency_hz=300.8
- [2026-08-22 01:59:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335141.3892186 | source=vosk | rms=139 | updated_at=1787335141.3892186 | frequency_hz=300.8
- [2026-08-22 01:59:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335143.1565673 | source=vosk | rms=161 | updated_at=1787335142.6394267 | frequency_hz=300.8
- [2026-08-22 01:59:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335144.1754868 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335144.680518 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335145.2729635 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:05] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1787335145.9362426 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335146.1467829 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335146.6547656 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335150.6418207 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335151.1758723 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335155.1392248 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:15] operator / voice_transcript_final / voice: by
  meta: kind=final | timestamp=1787335155.4312758 | source=final | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335155.6759858 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335157.7992067 | source=vosk | rms=134 | updated_at=1787335144.1754868 | frequency_hz=300.8
- [2026-08-22 01:59:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335159.145809 | source=vosk | rms=121 | updated_at=1787335158.4207335 | frequency_hz=300.8
- [2026-08-22 01:59:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335159.3899486 | source=vosk | rms=185 | updated_at=1787335159.3899486 | frequency_hz=300.8
- [2026-08-22 01:59:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335159.8887477 | source=vosk | rms=185 | updated_at=1787335159.3899486 | frequency_hz=300.8
- [2026-08-22 01:59:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335160.1392717 | source=vosk | rms=185 | updated_at=1787335159.3899486 | frequency_hz=300.8
- [2026-08-22 01:59:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335161.6397102 | source=vosk | rms=134 | updated_at=1787335160.8908434 | frequency_hz=300.8
- [2026-08-22 01:59:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335162.1584117 | source=vosk | rms=299 | updated_at=1787335162.1584117 | frequency_hz=300.8
- [2026-08-22 01:59:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335162.8897731 | source=vosk | rms=299 | updated_at=1787335162.1584117 | frequency_hz=300.8
- [2026-08-22 01:59:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335164.892035 | source=vosk | rms=361 | updated_at=1787335164.892035 | frequency_hz=300.8
- [2026-08-22 01:59:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335165.389606 | source=vosk | rms=361 | updated_at=1787335164.892035 | frequency_hz=300.8
- [2026-08-22 01:59:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335167.6453366 | source=vosk | rms=361 | updated_at=1787335164.892035 | frequency_hz=300.8
- [2026-08-22 01:59:28] operator / voice_transcript_partial / voice: it's the most
  meta: kind=partial | timestamp=1787335168.4655724 | source=vosk | rms=124 | updated_at=1787335168.1642566 | frequency_hz=300.8
- [2026-08-22 01:59:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335168.6458015 | source=vosk | rms=194 | updated_at=1787335168.6458015 | frequency_hz=300.8
- [2026-08-22 01:59:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335168.8894563 | source=vosk | rms=252 | updated_at=1787335168.8894563 | frequency_hz=300.8
- [2026-08-22 01:59:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335169.1598241 | source=vosk | rms=171 | updated_at=1787335169.1598241 | frequency_hz=300.8
- [2026-08-22 01:59:29] operator / voice_transcript_final / voice: it s the most
  meta: kind=final | timestamp=1787335169.6263628 | source=final | rms=171 | updated_at=1787335169.1598241 | frequency_hz=300.8
- [2026-08-22 01:59:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335169.7391858 | source=vosk | rms=171 | updated_at=1787335169.1598241 | frequency_hz=300.8
- [2026-08-22 01:59:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335169.7391858 | source=vosk | rms=120 | updated_at=1787335169.7391858 | frequency_hz=300.8
- [2026-08-22 01:59:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335170.4248052 | source=vosk | rms=139 | updated_at=1787335169.7557328 | frequency_hz=300.8
- [2026-08-22 01:59:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335171.3890734 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335171.9242399 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335174.4053116 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335175.664956 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335175.8920357 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335177.171861 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335178.1407819 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:38] operator / voice_transcript_partial / voice: turns out
  meta: kind=partial | timestamp=1787335178.2167017 | source=vosk | rms=122 | updated_at=1787335171.3890734 | frequency_hz=300.8
- [2026-08-22 01:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335178.4265337 | source=vosk | rms=1201 | updated_at=1787335178.4265337 | frequency_hz=300.8
- [2026-08-22 01:59:38] operator / voice_transcript_partial / voice: turns out that
  meta: kind=partial | timestamp=1787335178.4650357 | source=vosk | rms=1201 | updated_at=1787335178.4265337 | frequency_hz=300.8
- [2026-08-22 01:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335178.6391556 | source=vosk | rms=1202 | updated_at=1787335178.6391556 | frequency_hz=300.8
- [2026-08-22 01:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335178.9277887 | source=vosk | rms=269 | updated_at=1787335178.9277887 | frequency_hz=300.8
- [2026-08-22 01:59:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335179.435233 | source=vosk | rms=269 | updated_at=1787335178.9277887 | frequency_hz=300.8
- [2026-08-22 01:59:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335180.663573 | source=vosk | rms=269 | updated_at=1787335178.9277887 | frequency_hz=300.8
- [2026-08-22 01:59:41] operator / voice_transcript_final / voice: turns out that
  meta: kind=final | timestamp=1787335181.0823936 | source=final | rms=269 | updated_at=1787335178.9277887 | frequency_hz=300.8
- [2026-08-22 01:59:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335181.2089427 | source=vosk | rms=269 | updated_at=1787335178.9277887 | frequency_hz=300.8
- [2026-08-22 01:59:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335181.2089427 | source=vosk | rms=269 | updated_at=1787335178.9277887 | frequency_hz=300.8
- [2026-08-22 01:59:44] operator / voice_transcript_partial / voice: so it
  meta: kind=partial | timestamp=1787335184.6794336 | source=vosk | rms=363 | updated_at=1787335184.6401098 | frequency_hz=300.8
- [2026-08-22 01:59:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335184.8906362 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335185.177364 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335185.6918106 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:46] operator / voice_transcript_final / voice: search
  meta: kind=final | timestamp=1787335186.13405 | source=final | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335186.2517276 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335186.2517276 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335186.895322 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335187.6637251 | source=vosk | rms=263 | updated_at=1787335184.8906362 | frequency_hz=300.8
- [2026-08-22 01:59:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335189.9163263 | source=vosk | rms=192 | updated_at=1787335189.4013333 | frequency_hz=300.8
- [2026-08-22 01:59:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335190.1391847 | source=vosk | rms=192 | updated_at=1787335189.4013333 | frequency_hz=300.8
- [2026-08-22 01:59:51] operator / voice_transcript_partial / voice: still
  meta: kind=partial | timestamp=1787335191.2051501 | source=vosk | rms=462 | updated_at=1787335191.1434977 | frequency_hz=300.8
- [2026-08-22 01:59:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335191.4344282 | source=vosk | rms=194 | updated_at=1787335191.4344282 | frequency_hz=300.8
- [2026-08-22 01:59:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335191.642765 | source=vosk | rms=160 | updated_at=1787335191.642765 | frequency_hz=300.8
- [2026-08-22 01:59:51] operator / voice_transcript_partial / voice: still see
  meta: kind=partial | timestamp=1787335191.6558762 | source=vosk | rms=160 | updated_at=1787335191.642765 | frequency_hz=300.8
- [2026-08-22 01:59:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335192.1533391 | source=vosk | rms=419 | updated_at=1787335192.1533391 | frequency_hz=300.8
- [2026-08-22 01:59:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335192.4576795 | source=vosk | rms=419 | updated_at=1787335192.1533391 | frequency_hz=300.8
- [2026-08-22 01:59:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335192.902615 | source=vosk | rms=206 | updated_at=1787335192.902615 | frequency_hz=300.8
- [2026-08-22 01:59:52] operator / voice_transcript_partial / voice: still see so
  meta: kind=partial | timestamp=1787335192.9698253 | source=vosk | rms=206 | updated_at=1787335192.902615 | frequency_hz=300.8
- [2026-08-22 01:59:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335193.3944492 | source=vosk | rms=206 | updated_at=1787335192.902615 | frequency_hz=300.8
- [2026-08-22 01:59:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335193.6461453 | source=vosk | rms=822 | updated_at=1787335193.6461453 | frequency_hz=300.8
- [2026-08-22 01:59:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335193.949163 | source=vosk | rms=354 | updated_at=1787335193.949163 | frequency_hz=300.8
- [2026-08-22 01:59:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335194.149261 | source=vosk | rms=299 | updated_at=1787335194.149261 | frequency_hz=300.8
- [2026-08-22 01:59:54] operator / voice_transcript_partial / voice: still see so the
  meta: kind=partial | timestamp=1787335194.167853 | source=vosk | rms=299 | updated_at=1787335194.149261 | frequency_hz=300.8
- [2026-08-22 01:59:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335194.3901217 | source=vosk | rms=546 | updated_at=1787335194.3901217 | frequency_hz=300.8
- [2026-08-22 01:59:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335194.6402302 | source=vosk | rms=337 | updated_at=1787335194.6402302 | frequency_hz=300.8
- [2026-08-22 01:59:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335194.8978467 | source=vosk | rms=337 | updated_at=1787335194.6402302 | frequency_hz=300.8
- [2026-08-22 01:59:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335195.1681664 | source=vosk | rms=263 | updated_at=1787335195.1681664 | frequency_hz=300.8
- [2026-08-22 01:59:55] operator / voice_transcript_partial / voice: still see so the stuff
  meta: kind=partial | timestamp=1787335195.1969438 | source=vosk | rms=263 | updated_at=1787335195.1681664 | frequency_hz=300.8
- [2026-08-22 01:59:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335195.715875 | source=vosk | rms=263 | updated_at=1787335195.1681664 | frequency_hz=300.8
- [2026-08-22 01:59:55] operator / voice_transcript_partial / voice: still see sold the stock market
  meta: kind=partial | timestamp=1787335195.769365 | source=vosk | rms=263 | updated_at=1787335195.1681664 | frequency_hz=300.8
- [2026-08-22 01:59:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335195.9285808 | source=vosk | rms=263 | updated_at=1787335195.1681664 | frequency_hz=300.8
- [2026-08-22 01:59:55] operator / voice_transcript_partial / voice: still see sold the stock
  meta: kind=partial | timestamp=1787335195.9654293 | source=vosk | rms=263 | updated_at=1787335195.1681664 | frequency_hz=300.8
- [2026-08-22 01:59:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335196.1507869 | source=vosk | rms=139 | updated_at=1787335196.1507869 | frequency_hz=300.8
- [2026-08-22 01:59:56] operator / voice_transcript_partial / voice: still see so the stop me
  meta: kind=partial | timestamp=1787335196.2180967 | source=vosk | rms=139 | updated_at=1787335196.1507869 | frequency_hz=300.8
- [2026-08-22 01:59:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335196.4273996 | source=vosk | rms=139 | updated_at=1787335196.1507869 | frequency_hz=300.8
- [2026-08-22 01:59:56] operator / voice_transcript_final / voice: still see so the stop me
  meta: kind=final | timestamp=1787335196.9708002 | source=final | rms=139 | updated_at=1787335196.1507869 | frequency_hz=300.8
- [2026-08-22 01:59:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335197.369558 | source=vosk | rms=139 | updated_at=1787335196.1507869 | frequency_hz=300.8
- [2026-08-22 01:59:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335198.1434908 | source=vosk | rms=264 | updated_at=1787335198.1434908 | frequency_hz=300.8
- [2026-08-22 01:59:59] operator / voice_transcript_partial / voice: good
  meta: kind=partial | timestamp=1787335199.1748302 | source=vosk | rms=423 | updated_at=1787335199.1567273 | frequency_hz=300.8
- [2026-08-22 01:59:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335199.6399379 | source=vosk | rms=152 | updated_at=1787335199.6399379 | frequency_hz=300.8
- [2026-08-22 02:00:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335200.1628053 | source=vosk | rms=152 | updated_at=1787335199.6399379 | frequency_hz=300.8
- [2026-08-22 02:00:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335203.145143 | source=vosk | rms=350 | updated_at=1787335203.145143 | frequency_hz=300.8
- [2026-08-22 02:00:03] operator / voice_transcript_partial / voice: good to me
  meta: kind=partial | timestamp=1787335203.1917455 | source=vosk | rms=350 | updated_at=1787335203.145143 | frequency_hz=300.8
- [2026-08-22 02:00:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335203.647489 | source=vosk | rms=350 | updated_at=1787335203.145143 | frequency_hz=300.8
- [2026-08-22 02:00:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335203.8898387 | source=vosk | rms=350 | updated_at=1787335203.145143 | frequency_hz=300.8
- [2026-08-22 02:00:03] operator / voice_transcript_partial / voice: good to meet
  meta: kind=partial | timestamp=1787335203.9120073 | source=vosk | rms=350 | updated_at=1787335203.145143 | frequency_hz=300.8
- [2026-08-22 02:00:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335204.4083753 | source=vosk | rms=350 | updated_at=1787335203.145143 | frequency_hz=300.8
- [2026-08-22 02:00:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335204.6455486 | source=vosk | rms=1200 | updated_at=1787335204.6455486 | frequency_hz=300.8
- [2026-08-22 02:00:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335204.9981086 | source=vosk | rms=1201 | updated_at=1787335204.9981086 | frequency_hz=300.8
- [2026-08-22 02:00:05] operator / voice_transcript_final / voice: good that me
  meta: kind=final | timestamp=1787335205.6346338 | source=final | rms=1082 | updated_at=1787335205.1504836 | frequency_hz=300.8
- [2026-08-22 02:00:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335205.777494 | source=vosk | rms=1082 | updated_at=1787335205.1504836 | frequency_hz=300.8
- [2026-08-22 02:00:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335205.777494 | source=vosk | rms=1082 | updated_at=1787335205.1504836 | frequency_hz=300.8
- [2026-08-22 02:00:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335206.4108126 | source=vosk | rms=1082 | updated_at=1787335205.1504836 | frequency_hz=300.8
- [2026-08-22 02:00:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335207.1647346 | source=vosk | rms=1082 | updated_at=1787335205.1504836 | frequency_hz=300.8
- [2026-08-22 02:00:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335208.389815 | source=vosk | rms=179 | updated_at=1787335207.8896003 | frequency_hz=300.8
- [2026-08-22 02:00:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335209.4200573 | source=vosk | rms=179 | updated_at=1787335207.8896003 | frequency_hz=300.8
- [2026-08-22 02:00:09] operator / voice_transcript_partial / voice: turns
  meta: kind=partial | timestamp=1787335209.4320688 | source=vosk | rms=179 | updated_at=1787335207.8896003 | frequency_hz=300.8
- [2026-08-22 02:00:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335209.701625 | source=vosk | rms=221 | updated_at=1787335209.701625 | frequency_hz=300.8
- [2026-08-22 02:00:09] operator / voice_transcript_partial / voice: turns out
  meta: kind=partial | timestamp=1787335209.721142 | source=vosk | rms=221 | updated_at=1787335209.701625 | frequency_hz=300.8
- [2026-08-22 02:00:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335209.8942597 | source=vosk | rms=235 | updated_at=1787335209.8942597 | frequency_hz=300.8
- [2026-08-22 02:00:09] operator / voice_transcript_partial / voice: turns green
  meta: kind=partial | timestamp=1787335209.9539628 | source=vosk | rms=235 | updated_at=1787335209.8942597 | frequency_hz=300.8
- [2026-08-22 02:00:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335210.1492782 | source=vosk | rms=187 | updated_at=1787335210.1492782 | frequency_hz=300.8
- [2026-08-22 02:00:10] operator / voice_transcript_partial / voice: turns out
  meta: kind=partial | timestamp=1787335210.2285826 | source=vosk | rms=187 | updated_at=1787335210.1492782 | frequency_hz=300.8
- [2026-08-22 02:00:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335210.410924 | source=vosk | rms=208 | updated_at=1787335210.410924 | frequency_hz=300.8
- [2026-08-22 02:00:10] operator / voice_transcript_final / voice: turns green
  meta: kind=final | timestamp=1787335210.7140212 | source=final | rms=208 | updated_at=1787335210.410924 | frequency_hz=300.8
- [2026-08-22 02:00:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335210.7566357 | source=vosk | rms=262 | updated_at=1787335210.7566357 | frequency_hz=300.8
- [2026-08-22 02:00:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335211.4372337 | source=vosk | rms=262 | updated_at=1787335210.7566357 | frequency_hz=300.8
- [2026-08-22 02:00:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335212.9238577 | source=vosk | rms=1204 | updated_at=1787335212.9238577 | frequency_hz=300.8
- [2026-08-22 02:00:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335213.6722016 | source=vosk | rms=887 | updated_at=1787335213.1402624 | frequency_hz=300.8
- [2026-08-22 02:00:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335216.6566339 | source=vosk | rms=455 | updated_at=1787335216.6566339 | frequency_hz=300.8
- [2026-08-22 02:00:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335217.1874025 | source=vosk | rms=455 | updated_at=1787335216.6566339 | frequency_hz=300.8
- [2026-08-22 02:00:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335218.4239151 | source=vosk | rms=1200 | updated_at=1787335218.4239151 | frequency_hz=300.8
- [2026-08-22 02:00:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335220.6402683 | source=vosk | rms=246 | updated_at=1787335220.1551495 | frequency_hz=330.6
- [2026-08-22 02:00:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335220.983998 | source=vosk | rms=246 | updated_at=1787335220.1551495 | frequency_hz=330.6
- [2026-08-22 02:00:23] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1787335223.7143228 | source=vosk | rms=1204 | updated_at=1787335223.6430383 | frequency_hz=330.6
- [2026-08-22 02:00:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335223.8901482 | source=vosk | rms=1201 | updated_at=1787335223.8901482 | frequency_hz=330.6
- [2026-08-22 02:00:23] operator / voice_transcript_partial / voice: human spirit
  meta: kind=partial | timestamp=1787335223.952051 | source=vosk | rms=1201 | updated_at=1787335223.8901482 | frequency_hz=330.6
- [2026-08-22 02:00:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335224.1421824 | source=vosk | rms=1202 | updated_at=1787335224.1421824 | frequency_hz=330.6
- [2026-08-22 02:00:24] operator / voice_transcript_final / voice: kinda scary
  meta: kind=final | timestamp=1787335224.3677132 | source=final | rms=1202 | updated_at=1787335224.1421824 | frequency_hz=330.6
- [2026-08-22 02:00:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335224.6441717 | source=vosk | rms=1202 | updated_at=1787335224.1421824 | frequency_hz=330.6
- [2026-08-22 02:00:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335230.9122744 | source=vosk | rms=1202 | updated_at=1787335224.1421824 | frequency_hz=330.6
- [2026-08-22 02:00:32] operator / voice_transcript_partial / voice: stop me
  meta: kind=partial | timestamp=1787335232.203125 | source=vosk | rms=208 | updated_at=1787335231.648528 | frequency_hz=330.6
- [2026-08-22 02:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335232.6397064 | source=vosk | rms=967 | updated_at=1787335232.6397064 | frequency_hz=330.6
- [2026-08-22 02:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335232.8944306 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335233.1416929 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:33] operator / voice_transcript_final / voice: stop me
  meta: kind=final | timestamp=1787335233.459751 | source=final | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335233.712694 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335234.890976 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:35] operator / voice_transcript_partial / voice: being a
  meta: kind=partial | timestamp=1787335235.9313958 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335236.1411448 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:36] operator / voice_transcript_partial / voice: being a good
  meta: kind=partial | timestamp=1787335236.1711028 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335236.3904748 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335236.9308963 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:36] operator / voice_transcript_partial / voice: being a do
  meta: kind=partial | timestamp=1787335236.9853354 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335237.6405082 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335238.1413357 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:38] operator / voice_transcript_final / voice: being i do
  meta: kind=final | timestamp=1787335238.5322878 | source=final | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335238.6845472 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335239.7417722 | source=vosk | rms=243 | updated_at=1787335232.8944306 | frequency_hz=330.6
- [2026-08-22 02:00:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335241.653209 | source=vosk | rms=922 | updated_at=1787335240.6945531 | frequency_hz=330.6
- [2026-08-22 02:00:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335243.7877836 | source=vosk | rms=345 | updated_at=1787335243.7877836 | frequency_hz=330.6
- [2026-08-22 02:00:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335245.047569 | source=vosk | rms=203 | updated_at=1787335244.042468 | frequency_hz=330.6
- [2026-08-22 02:00:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335245.5102942 | source=vosk | rms=188 | updated_at=1787335245.5102942 | frequency_hz=330.6
- [2026-08-22 02:00:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335246.2803013 | source=vosk | rms=180 | updated_at=1787335245.7604187 | frequency_hz=330.6
- [2026-08-22 02:00:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335246.5279274 | source=vosk | rms=263 | updated_at=1787335246.5279274 | frequency_hz=330.6
- [2026-08-22 02:00:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335247.7601166 | source=vosk | rms=331 | updated_at=1787335247.262352 | frequency_hz=330.6
- [2026-08-22 02:00:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335250.7603421 | source=vosk | rms=331 | updated_at=1787335247.262352 | frequency_hz=330.6
- [2026-08-22 02:00:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335251.3037074 | source=vosk | rms=331 | updated_at=1787335247.262352 | frequency_hz=330.6
- [2026-08-22 02:00:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335251.5108068 | source=vosk | rms=190 | updated_at=1787335251.5108068 | frequency_hz=330.6
- [2026-08-22 02:00:52] operator / voice_transcript_partial / voice: dude
  meta: kind=partial | timestamp=1787335252.0454578 | source=vosk | rms=291 | updated_at=1787335252.0348735 | frequency_hz=330.6
- [2026-08-22 02:00:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335252.2633734 | source=vosk | rms=188 | updated_at=1787335252.2633734 | frequency_hz=330.6
- [2026-08-22 02:00:52] operator / voice_transcript_partial / voice: do do
  meta: kind=partial | timestamp=1787335252.2887778 | source=vosk | rms=188 | updated_at=1787335252.2633734 | frequency_hz=330.6
- [2026-08-22 02:00:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335252.5115113 | source=vosk | rms=184 | updated_at=1787335252.5115113 | frequency_hz=330.6
- [2026-08-22 02:00:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335252.7596939 | source=vosk | rms=155 | updated_at=1787335252.7596939 | frequency_hz=330.6
- [2026-08-22 02:00:52] operator / voice_transcript_partial / voice: do do do
  meta: kind=partial | timestamp=1787335252.7832239 | source=vosk | rms=155 | updated_at=1787335252.7596939 | frequency_hz=330.6
- [2026-08-22 02:00:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335253.0512168 | source=vosk | rms=1200 | updated_at=1787335253.0512168 | frequency_hz=330.6
- [2026-08-22 02:00:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335253.2757914 | source=vosk | rms=1013 | updated_at=1787335253.2757914 | frequency_hz=330.6
- [2026-08-22 02:00:53] operator / voice_transcript_partial / voice: do do do do
  meta: kind=partial | timestamp=1787335253.2832994 | source=vosk | rms=1013 | updated_at=1787335253.2757914 | frequency_hz=330.6
- [2026-08-22 02:00:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335253.5111938 | source=vosk | rms=150 | updated_at=1787335253.5111938 | frequency_hz=330.6
- [2026-08-22 02:00:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335253.7992313 | source=vosk | rms=150 | updated_at=1787335253.7992313 | frequency_hz=330.6
- [2026-08-22 02:00:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335254.0488403 | source=vosk | rms=150 | updated_at=1787335253.7992313 | frequency_hz=330.6
- [2026-08-22 02:00:54] operator / voice_transcript_final / voice: what do you do
  meta: kind=final | timestamp=1787335254.311157 | source=final | rms=150 | updated_at=1787335253.7992313 | frequency_hz=330.6
- [2026-08-22 02:00:54] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787335254.350145 | source=state | rms=150 | updated_at=1787335253.7992313 | frequency_hz=330.6
- [2026-08-22 02:00:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335254.350145 | source=state | rms=150 | updated_at=1787335253.7992313 | frequency_hz=330.6
- [2026-08-22 02:00:54] operator / voice_command / voice: what do you do
  meta: normalized=True
- [2026-08-22 02:00:55] assistant / assistant_prompt / text: My current scope is normal conversation, Smart Sentry help, diagnostics on request, and supported command handling.
  meta: task_kind=prompt | speak_requested=True
- [2026-08-22 02:00:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335254.350145 | source=vosk | rms=150 | updated_at=1787335253.7992313 | frequency_hz=330.6
- [2026-08-22 02:00:55] assistant / spoken_reply / voice: My current scope is normal conversation, Smart Sentry help, diagnostics on request, and supported command handling.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-08-22 02:00:56] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1787335256.8532639 | source=vosk | rms=1204 | updated_at=1787335256.7757697 | frequency_hz=330.6
- [2026-08-22 02:00:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335257.265992 | source=vosk | rms=1204 | updated_at=1787335256.7757697 | frequency_hz=330.6
- [2026-08-22 02:00:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335257.5098684 | source=vosk | rms=1204 | updated_at=1787335256.7757697 | frequency_hz=330.6
- [2026-08-22 02:00:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335257.799595 | source=vosk | rms=1204 | updated_at=1787335256.7757697 | frequency_hz=330.6
- [2026-08-22 02:00:57] operator / voice_transcript_partial / voice: do do
  meta: kind=partial | timestamp=1787335257.8315022 | source=vosk | rms=1204 | updated_at=1787335256.7757697 | frequency_hz=330.6
- [2026-08-22 02:00:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335258.0466642 | source=vosk | rms=704 | updated_at=1787335258.0466642 | frequency_hz=330.6
- [2026-08-22 02:00:58] operator / voice_transcript_partial / voice: do do do
  meta: kind=partial | timestamp=1787335258.093245 | source=vosk | rms=704 | updated_at=1787335258.0466642 | frequency_hz=330.6
- [2026-08-22 02:00:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335258.2612174 | source=vosk | rms=1173 | updated_at=1787335258.2612174 | frequency_hz=330.6
- [2026-08-22 02:00:58] operator / voice_transcript_partial / voice: do do do my
  meta: kind=partial | timestamp=1787335258.2833052 | source=vosk | rms=1173 | updated_at=1787335258.2612174 | frequency_hz=330.6
- [2026-08-22 02:00:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335258.5147326 | source=vosk | rms=806 | updated_at=1787335258.5147326 | frequency_hz=330.6
- [2026-08-22 02:00:58] operator / voice_transcript_partial / voice: do do do my current
  meta: kind=partial | timestamp=1787335258.607843 | source=vosk | rms=806 | updated_at=1787335258.5147326 | frequency_hz=330.6
- [2026-08-22 02:00:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335258.7995918 | source=vosk | rms=434 | updated_at=1787335258.7995918 | frequency_hz=330.6
- [2026-08-22 02:00:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335259.0356662 | source=vosk | rms=623 | updated_at=1787335259.0356662 | frequency_hz=330.6
- [2026-08-22 02:00:59] operator / voice_transcript_partial / voice: do do do my current scope
  meta: kind=partial | timestamp=1787335259.048742 | source=vosk | rms=623 | updated_at=1787335259.0356662 | frequency_hz=330.6
- [2026-08-22 02:00:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335259.2605705 | source=vosk | rms=709 | updated_at=1787335259.2605705 | frequency_hz=330.6
- [2026-08-22 02:00:59] operator / voice_transcript_partial / voice: do do do my current scope is
  meta: kind=partial | timestamp=1787335259.2946398 | source=vosk | rms=709 | updated_at=1787335259.2605705 | frequency_hz=330.6
- [2026-08-22 02:00:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335259.515042 | source=vosk | rms=495 | updated_at=1787335259.515042 | frequency_hz=330.6
- [2026-08-22 02:00:59] operator / voice_transcript_partial / voice: do do do my current scope is normal
  meta: kind=partial | timestamp=1787335259.535899 | source=vosk | rms=495 | updated_at=1787335259.515042 | frequency_hz=330.6
- [2026-08-22 02:00:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335259.7601137 | source=vosk | rms=1154 | updated_at=1787335259.7601137 | frequency_hz=330.6
- [2026-08-22 02:00:59] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation
  meta: kind=partial | timestamp=1787335259.7729146 | source=vosk | rms=1154 | updated_at=1787335259.7601137 | frequency_hz=330.6
- [2026-08-22 02:01:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335260.0129547 | source=vosk | rms=894 | updated_at=1787335260.0129547 | frequency_hz=330.6
- [2026-08-22 02:01:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335260.3215315 | source=vosk | rms=764 | updated_at=1787335260.3215315 | frequency_hz=330.6
- [2026-08-22 02:01:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335260.5166748 | source=vosk | rms=501 | updated_at=1787335260.5166748 | frequency_hz=330.6
- [2026-08-22 02:01:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335260.7776856 | source=vosk | rms=1204 | updated_at=1787335260.7776856 | frequency_hz=330.6
- [2026-08-22 02:01:00] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation bulk up
  meta: kind=partial | timestamp=1787335260.8188887 | source=vosk | rms=1204 | updated_at=1787335260.7776856 | frequency_hz=330.6
- [2026-08-22 02:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335261.0094924 | source=vosk | rms=632 | updated_at=1787335261.0094924 | frequency_hz=330.6
- [2026-08-22 02:01:01] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy
  meta: kind=partial | timestamp=1787335261.0300186 | source=vosk | rms=632 | updated_at=1787335261.0094924 | frequency_hz=330.6
- [2026-08-22 02:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335261.2818847 | source=vosk | rms=809 | updated_at=1787335261.2818847 | frequency_hz=330.6
- [2026-08-22 02:01:01] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart
  meta: kind=partial | timestamp=1787335261.303481 | source=vosk | rms=809 | updated_at=1787335261.2818847 | frequency_hz=330.6
- [2026-08-22 02:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335261.5098948 | source=vosk | rms=410 | updated_at=1787335261.5098948 | frequency_hz=330.6
- [2026-08-22 02:01:01] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century
  meta: kind=partial | timestamp=1787335261.5330257 | source=vosk | rms=410 | updated_at=1787335261.5098948 | frequency_hz=330.6
- [2026-08-22 02:01:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335262.0102954 | source=vosk | rms=1204 | updated_at=1787335262.0102954 | frequency_hz=330.6
- [2026-08-22 02:01:02] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century house
  meta: kind=partial | timestamp=1787335262.0272439 | source=vosk | rms=1204 | updated_at=1787335262.0102954 | frequency_hz=330.6
- [2026-08-22 02:01:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335262.259824 | source=vosk | rms=930 | updated_at=1787335262.259824 | frequency_hz=330.6
- [2026-08-22 02:01:02] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help
  meta: kind=partial | timestamp=1787335262.2758462 | source=vosk | rms=930 | updated_at=1787335262.259824 | frequency_hz=330.6
- [2026-08-22 02:01:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335262.5190446 | source=vosk | rms=645 | updated_at=1787335262.5190446 | frequency_hz=330.6
- [2026-08-22 02:01:02] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnose
  meta: kind=partial | timestamp=1787335262.5687058 | source=vosk | rms=645 | updated_at=1787335262.5190446 | frequency_hz=330.6
- [2026-08-22 02:01:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335262.7712266 | source=vosk | rms=492 | updated_at=1787335262.7712266 | frequency_hz=330.6
- [2026-08-22 02:01:02] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help
  meta: kind=partial | timestamp=1787335262.838595 | source=vosk | rms=492 | updated_at=1787335262.7712266 | frequency_hz=330.6
- [2026-08-22 02:01:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335263.0132296 | source=vosk | rms=1150 | updated_at=1787335263.0132296 | frequency_hz=330.6
- [2026-08-22 02:01:03] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics
  meta: kind=partial | timestamp=1787335263.0359373 | source=vosk | rms=1150 | updated_at=1787335263.0132296 | frequency_hz=330.6
- [2026-08-22 02:01:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335263.2614467 | source=vosk | rms=407 | updated_at=1787335263.2614467 | frequency_hz=330.6
- [2026-08-22 02:01:03] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm requesting
  meta: kind=partial | timestamp=1787335263.293261 | source=vosk | rms=407 | updated_at=1787335263.2614467 | frequency_hz=330.6
- [2026-08-22 02:01:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335263.782249 | source=vosk | rms=730 | updated_at=1787335263.782249 | frequency_hz=330.6
- [2026-08-22 02:01:03] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and
  meta: kind=partial | timestamp=1787335263.7952845 | source=vosk | rms=730 | updated_at=1787335263.782249 | frequency_hz=330.6
- [2026-08-22 02:01:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335264.0248868 | source=vosk | rms=707 | updated_at=1787335264.0248868 | frequency_hz=330.6
- [2026-08-22 02:01:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335264.2646754 | source=vosk | rms=523 | updated_at=1787335264.2646754 | frequency_hz=330.6
- [2026-08-22 02:01:04] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported
  meta: kind=partial | timestamp=1787335264.330368 | source=vosk | rms=523 | updated_at=1787335264.2646754 | frequency_hz=330.6
- [2026-08-22 02:01:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335264.5097158 | source=vosk | rms=737 | updated_at=1787335264.5097158 | frequency_hz=330.6
- [2026-08-22 02:01:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335264.7615428 | source=vosk | rms=509 | updated_at=1787335264.7615428 | frequency_hz=330.6
- [2026-08-22 02:01:04] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported command
  meta: kind=partial | timestamp=1787335264.8177104 | source=vosk | rms=509 | updated_at=1787335264.7615428 | frequency_hz=330.6
- [2026-08-22 02:01:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335265.0107343 | source=vosk | rms=509 | updated_at=1787335264.7615428 | frequency_hz=330.6
- [2026-08-22 02:01:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335265.5161357 | source=vosk | rms=509 | updated_at=1787335264.7615428 | frequency_hz=330.6
- [2026-08-22 02:01:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335265.7975452 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:05] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported command handling
  meta: kind=partial | timestamp=1787335265.8067136 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335266.2629683 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335266.7655485 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335267.033402 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:07] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported command handling of games
  meta: kind=partial | timestamp=1787335267.098178 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335267.7917173 | source=vosk | rms=344 | updated_at=1787335265.7975452 | frequency_hz=330.6
- [2026-08-22 02:01:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335274.0375497 | source=vosk | rms=417 | updated_at=1787335274.0375497 | frequency_hz=330.6
- [2026-08-22 02:01:14] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported command handling of games a
  meta: kind=partial | timestamp=1787335274.110013 | source=vosk | rms=417 | updated_at=1787335274.0375497 | frequency_hz=330.6
- [2026-08-22 02:01:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335274.3305204 | source=vosk | rms=742 | updated_at=1787335274.3305204 | frequency_hz=330.6
- [2026-08-22 02:01:14] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported command handling of games a soap opera
  meta: kind=partial | timestamp=1787335274.418782 | source=vosk | rms=742 | updated_at=1787335274.3305204 | frequency_hz=330.6
- [2026-08-22 02:01:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335274.5995924 | source=vosk | rms=470 | updated_at=1787335274.510049 | frequency_hz=330.6
- [2026-08-22 02:01:14] operator / voice_transcript_partial / voice: do do do my current scope is normal conversation polygamy smart century help diagnostics i'm request and supported command handling of games a
  meta: kind=partial | timestamp=1787335274.6056015 | source=vosk | rms=470 | updated_at=1787335274.510049 | frequency_hz=330.6
- [2026-08-22 02:01:15] operator / voice_transcript_final / voice: do do do my current scope is normal conversation polygamy smart sentry help diagnostics i m request and supported command handling of games a shop
  meta: kind=final | timestamp=1787335275.5209756 | source=final | rms=818 | updated_at=1787335274.7698433 | frequency_hz=330.6
- [2026-08-22 02:01:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335276.1170835 | source=vosk | rms=818 | updated_at=1787335274.7698433 | frequency_hz=330.6
- [2026-08-22 02:01:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335276.1170835 | source=vosk | rms=357 | updated_at=1787335276.1170835 | frequency_hz=330.6
- [2026-08-22 02:01:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335276.764044 | source=vosk | rms=561 | updated_at=1787335276.185837 | frequency_hz=330.6
- [2026-08-22 02:01:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335277.6224484 | source=vosk | rms=1201 | updated_at=1787335277.6224484 | frequency_hz=330.6
- [2026-08-22 02:01:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335278.2652512 | source=vosk | rms=1203 | updated_at=1787335277.7668447 | frequency_hz=330.6
- [2026-08-22 02:01:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335282.276189 | source=vosk | rms=1203 | updated_at=1787335277.7668447 | frequency_hz=330.6
- [2026-08-22 02:01:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335282.7862134 | source=vosk | rms=1203 | updated_at=1787335277.7668447 | frequency_hz=330.6
- [2026-08-22 02:01:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335283.0400517 | source=vosk | rms=529 | updated_at=1787335283.0400517 | frequency_hz=330.6
- [2026-08-22 02:01:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335284.7599084 | source=vosk | rms=1201 | updated_at=1787335284.2837677 | frequency_hz=330.6
- [2026-08-22 02:01:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335285.7869203 | source=vosk | rms=1201 | updated_at=1787335284.2837677 | frequency_hz=330.6
- [2026-08-22 02:01:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335287.7924528 | source=vosk | rms=1201 | updated_at=1787335287.2625313 | frequency_hz=330.6
- [2026-08-22 02:01:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335288.0179884 | source=vosk | rms=300 | updated_at=1787335288.0179884 | frequency_hz=330.6
- [2026-08-22 02:01:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335289.0236454 | source=vosk | rms=1203 | updated_at=1787335288.5454314 | frequency_hz=330.6
- [2026-08-22 02:01:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335290.02399 | source=vosk | rms=1203 | updated_at=1787335288.5454314 | frequency_hz=330.6
- [2026-08-22 02:01:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335291.009949 | source=vosk | rms=1203 | updated_at=1787335288.5454314 | frequency_hz=330.6
- [2026-08-22 02:01:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335292.778616 | source=vosk | rms=1203 | updated_at=1787335288.5454314 | frequency_hz=330.6
- [2026-08-22 02:01:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335293.262569 | source=vosk | rms=1203 | updated_at=1787335288.5454314 | frequency_hz=330.6
- [2026-08-22 02:01:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335293.7596774 | source=vosk | rms=1203 | updated_at=1787335293.7596774 | frequency_hz=330.6
- [2026-08-22 02:01:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335294.8039048 | source=vosk | rms=629 | updated_at=1787335294.2783666 | frequency_hz=330.6
- [2026-08-22 02:01:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335296.922766 | source=vosk | rms=629 | updated_at=1787335294.2783666 | frequency_hz=330.6
- [2026-08-22 02:01:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335297.5156066 | source=vosk | rms=629 | updated_at=1787335294.2783666 | frequency_hz=330.6
- [2026-08-22 02:01:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335302.2619405 | source=vosk | rms=1027 | updated_at=1787335302.2619405 | frequency_hz=330.6
- [2026-08-22 02:01:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787335302.5882142 | source=vosk | rms=968 | updated_at=1787335302.5481398 | frequency_hz=330.6
- [2026-08-22 02:01:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335302.762729 | source=vosk | rms=1201 | updated_at=1787335302.762729 | frequency_hz=330.6
- [2026-08-22 02:01:42] operator / voice_transcript_partial / voice: the new
  meta: kind=partial | timestamp=1787335302.8316867 | source=vosk | rms=1201 | updated_at=1787335302.762729 | frequency_hz=330.6
- [2026-08-22 02:01:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335303.0231822 | source=vosk | rms=1202 | updated_at=1787335303.0231822 | frequency_hz=330.6
- [2026-08-22 02:01:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335303.5109043 | source=vosk | rms=1202 | updated_at=1787335303.0231822 | frequency_hz=330.6
- [2026-08-22 02:01:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335305.5446255 | source=vosk | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335305.7607913 | source=vosk | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335306.2608886 | source=vosk | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335306.5150394 | source=vosk | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:46] operator / voice_transcript_final / voice: the move
  meta: kind=final | timestamp=1787335306.7641559 | source=final | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335306.800477 | source=vosk | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335310.280311 | source=vosk | rms=274 | updated_at=1787335305.5446255 | frequency_hz=330.6
- [2026-08-22 02:01:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335310.8035553 | source=vosk | rms=1204 | updated_at=1787335310.8035553 | frequency_hz=330.6
- [2026-08-22 02:01:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335311.7648296 | source=vosk | rms=1207 | updated_at=1787335311.3092482 | frequency_hz=330.6
- [2026-08-22 02:02:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335327.5524085 | source=vosk | rms=133 | updated_at=1787335327.5524085 | frequency_hz=330.6
- [2026-08-22 02:02:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335328.2610314 | source=vosk | rms=133 | updated_at=1787335327.5524085 | frequency_hz=330.6
- [2026-08-22 02:02:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335328.7658925 | source=vosk | rms=148 | updated_at=1787335328.7658925 | frequency_hz=330.6
- [2026-08-22 02:02:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335333.0582361 | source=vosk | rms=151 | updated_at=1787335332.2838302 | frequency_hz=330.6
- [2026-08-22 02:02:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335336.5385602 | source=vosk | rms=147 | updated_at=1787335336.5385602 | frequency_hz=330.6
- [2026-08-22 02:02:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335337.5317166 | source=vosk | rms=147 | updated_at=1787335336.5385602 | frequency_hz=330.6
- [2026-08-22 02:02:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335339.0121167 | source=vosk | rms=185 | updated_at=1787335339.0121167 | frequency_hz=330.6
- [2026-08-22 02:02:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335339.5107806 | source=vosk | rms=185 | updated_at=1787335339.0121167 | frequency_hz=330.6
- [2026-08-22 02:02:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335341.0274465 | source=vosk | rms=185 | updated_at=1787335339.0121167 | frequency_hz=330.6
- [2026-08-22 02:02:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335341.666194 | source=vosk | rms=185 | updated_at=1787335339.0121167 | frequency_hz=330.6
- [2026-08-22 02:02:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335345.4576252 | source=vosk | rms=154 | updated_at=1787335345.4576252 | frequency_hz=330.6
- [2026-08-22 02:02:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335348.1607778 | source=vosk | rms=149 | updated_at=1787335346.694075 | frequency_hz=330.6
- [2026-08-22 02:02:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335348.4110134 | source=vosk | rms=149 | updated_at=1787335346.694075 | frequency_hz=330.6
- [2026-08-22 02:02:29] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1787335349.487549 | source=vosk | rms=671 | updated_at=1787335349.430488 | frequency_hz=330.6
- [2026-08-22 02:02:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335349.6620736 | source=vosk | rms=671 | updated_at=1787335349.430488 | frequency_hz=330.6
- [2026-08-22 02:02:29] operator / voice_transcript_partial / voice: he split
  meta: kind=partial | timestamp=1787335349.704646 | source=vosk | rms=671 | updated_at=1787335349.430488 | frequency_hz=330.6
- [2026-08-22 02:02:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335349.9397538 | source=vosk | rms=463 | updated_at=1787335349.9397538 | frequency_hz=330.6
- [2026-08-22 02:02:30] operator / voice_transcript_partial / voice: he split peas
  meta: kind=partial | timestamp=1787335350.028181 | source=vosk | rms=463 | updated_at=1787335349.9397538 | frequency_hz=330.6
- [2026-08-22 02:02:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335350.1749632 | source=vosk | rms=143 | updated_at=1787335350.1749632 | frequency_hz=330.6
- [2026-08-22 02:02:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335350.4243639 | source=vosk | rms=143 | updated_at=1787335350.1749632 | frequency_hz=330.6
- [2026-08-22 02:02:30] operator / voice_transcript_partial / voice: he split his previous
  meta: kind=partial | timestamp=1787335350.4906154 | source=vosk | rms=143 | updated_at=1787335350.1749632 | frequency_hz=330.6
- [2026-08-22 02:02:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335350.9428298 | source=vosk | rms=143 | updated_at=1787335350.1749632 | frequency_hz=330.6
- [2026-08-22 02:02:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335352.9165897 | source=vosk | rms=143 | updated_at=1787335350.1749632 | frequency_hz=330.6
- [2026-08-22 02:02:33] operator / voice_transcript_partial / voice: he split is pretty
  meta: kind=partial | timestamp=1787335353.0068557 | source=vosk | rms=143 | updated_at=1787335350.1749632 | frequency_hz=330.6
- [2026-08-22 02:02:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335353.4118488 | source=vosk | rms=189 | updated_at=1787335353.4118488 | frequency_hz=330.6
- [2026-08-22 02:02:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335353.6845415 | source=vosk | rms=202 | updated_at=1787335353.6845415 | frequency_hz=330.6
- [2026-08-22 02:02:34] operator / voice_transcript_final / voice: he split screen
  meta: kind=final | timestamp=1787335354.1106517 | source=final | rms=202 | updated_at=1787335353.6845415 | frequency_hz=330.6
- [2026-08-22 02:02:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335354.3076766 | source=vosk | rms=202 | updated_at=1787335353.6845415 | frequency_hz=330.6
- [2026-08-22 02:02:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335354.3076766 | source=vosk | rms=257 | updated_at=1787335354.3076766 | frequency_hz=330.6
- [2026-08-22 02:02:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335354.9121962 | source=vosk | rms=134 | updated_at=1787335354.4103081 | frequency_hz=330.6
- [2026-08-22 02:02:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335355.4104476 | source=vosk | rms=183 | updated_at=1787335355.4104476 | frequency_hz=330.6
- [2026-08-22 02:02:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335356.2075763 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335356.4103186 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:36] operator / voice_transcript_partial / voice: blog
  meta: kind=partial | timestamp=1787335356.7018347 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335357.1865025 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:38] operator / voice_transcript_partial / voice: blog book on
  meta: kind=partial | timestamp=1787335358.2415059 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335358.4702613 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335358.6893623 | source=vosk | rms=445 | updated_at=1787335355.6628463 | frequency_hz=330.6
- [2026-08-22 02:02:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335358.9144528 | source=vosk | rms=230 | updated_at=1787335358.9144528 | frequency_hz=330.6
- [2026-08-22 02:02:39] operator / voice_transcript_final / voice: blog book on
  meta: kind=final | timestamp=1787335359.46534 | source=final | rms=230 | updated_at=1787335358.9144528 | frequency_hz=330.6
- [2026-08-22 02:02:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335359.678106 | source=vosk | rms=230 | updated_at=1787335358.9144528 | frequency_hz=330.6
- [2026-08-22 02:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335359.679109 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:39] operator / voice_transcript_partial / voice: good
  meta: kind=partial | timestamp=1787335359.7811048 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:39] operator / voice_transcript_partial / voice: good at it would
  meta: kind=partial | timestamp=1787335359.8525138 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335359.9565103 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:39] operator / voice_transcript_partial / voice: good at it with people
  meta: kind=partial | timestamp=1787335359.9565103 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335360.5396373 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335360.7287264 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:40] operator / voice_transcript_partial / voice: good at it would
  meta: kind=partial | timestamp=1787335360.8046505 | source=vosk | rms=133 | updated_at=1787335359.679109 | frequency_hz=330.6
- [2026-08-22 02:02:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335360.9107788 | source=vosk | rms=182 | updated_at=1787335360.9107788 | frequency_hz=330.6
- [2026-08-22 02:02:41] operator / voice_transcript_final / voice: good at it
  meta: kind=final | timestamp=1787335361.4106696 | source=final | rms=182 | updated_at=1787335360.9107788 | frequency_hz=330.6
- [2026-08-22 02:02:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335361.7652261 | source=vosk | rms=182 | updated_at=1787335360.9107788 | frequency_hz=330.6
- [2026-08-22 02:02:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335361.7652261 | source=vosk | rms=182 | updated_at=1787335360.9107788 | frequency_hz=330.6
- [2026-08-22 02:02:44] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787335364.0164146 | source=vosk | rms=376 | updated_at=1787335363.9291706 | frequency_hz=330.6
- [2026-08-22 02:02:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335364.1887465 | source=vosk | rms=155 | updated_at=1787335364.1887465 | frequency_hz=330.6
- [2026-08-22 02:02:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335364.4181077 | source=vosk | rms=392 | updated_at=1787335364.4181077 | frequency_hz=330.6
- [2026-08-22 02:02:44] operator / voice_transcript_partial / voice: the put
  meta: kind=partial | timestamp=1787335364.497796 | source=vosk | rms=392 | updated_at=1787335364.4181077 | frequency_hz=330.6
- [2026-08-22 02:02:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335364.686698 | source=vosk | rms=238 | updated_at=1787335364.686698 | frequency_hz=330.6
- [2026-08-22 02:02:44] operator / voice_transcript_partial / voice: the put the
  meta: kind=partial | timestamp=1787335364.7596304 | source=vosk | rms=238 | updated_at=1787335364.686698 | frequency_hz=330.6
- [2026-08-22 02:02:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335364.9413505 | source=vosk | rms=376 | updated_at=1787335364.9413505 | frequency_hz=330.6
- [2026-08-22 02:02:45] operator / voice_transcript_partial / voice: the put the putting
  meta: kind=partial | timestamp=1787335365.033763 | source=vosk | rms=376 | updated_at=1787335364.9413505 | frequency_hz=330.6
- [2026-08-22 02:02:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335365.1645947 | source=vosk | rms=296 | updated_at=1787335365.1645947 | frequency_hz=330.6
- [2026-08-22 02:02:45] operator / voice_transcript_partial / voice: the put the putting the
  meta: kind=partial | timestamp=1787335365.2329135 | source=vosk | rms=296 | updated_at=1787335365.1645947 | frequency_hz=330.6
- [2026-08-22 02:02:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335365.462111 | source=vosk | rms=520 | updated_at=1787335365.462111 | frequency_hz=330.6
- [2026-08-22 02:02:45] operator / voice_transcript_partial / voice: the put the putting the blame on
  meta: kind=partial | timestamp=1787335365.547409 | source=vosk | rms=520 | updated_at=1787335365.462111 | frequency_hz=330.6
- [2026-08-22 02:02:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335365.697038 | source=vosk | rms=253 | updated_at=1787335365.697038 | frequency_hz=330.6
- [2026-08-22 02:02:45] operator / voice_transcript_partial / voice: the put the putting the to normandy
  meta: kind=partial | timestamp=1787335365.7648225 | source=vosk | rms=253 | updated_at=1787335365.697038 | frequency_hz=330.6
- [2026-08-22 02:02:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335365.9111779 | source=vosk | rms=141 | updated_at=1787335365.9111779 | frequency_hz=330.6
- [2026-08-22 02:02:45] operator / voice_transcript_partial / voice: the put the putting the to normandy they
  meta: kind=partial | timestamp=1787335365.9994044 | source=vosk | rms=141 | updated_at=1787335365.9111779 | frequency_hz=330.6
- [2026-08-22 02:02:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335366.6609983 | source=vosk | rms=141 | updated_at=1787335365.9111779 | frequency_hz=330.6
- [2026-08-22 02:02:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335368.2025907 | source=vosk | rms=141 | updated_at=1787335365.9111779 | frequency_hz=330.6
- [2026-08-22 02:02:48] operator / voice_transcript_partial / voice: the put the putting the to normandy daylight
  meta: kind=partial | timestamp=1787335368.2995312 | source=vosk | rms=141 | updated_at=1787335365.9111779 | frequency_hz=330.6
- [2026-08-22 02:02:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335368.4124646 | source=vosk | rms=189 | updated_at=1787335368.4124646 | frequency_hz=330.6
- [2026-08-22 02:02:48] operator / voice_transcript_partial / voice: the put the putting the to normandy daily livelihood
  meta: kind=partial | timestamp=1787335368.5639434 | source=vosk | rms=189 | updated_at=1787335368.4124646 | frequency_hz=330.6
- [2026-08-22 02:02:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335368.6611638 | source=vosk | rms=291 | updated_at=1787335368.6611638 | frequency_hz=330.6
- [2026-08-22 02:02:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335368.910162 | source=vosk | rms=267 | updated_at=1787335368.910162 | frequency_hz=330.6
- [2026-08-22 02:02:48] operator / voice_transcript_partial / voice: the put the putting the to normandy daily livelihood good luck somewhere
  meta: kind=partial | timestamp=1787335368.9386435 | source=vosk | rms=267 | updated_at=1787335368.910162 | frequency_hz=330.6
- [2026-08-22 02:02:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335369.1907604 | source=vosk | rms=267 | updated_at=1787335368.910162 | frequency_hz=330.6
- [2026-08-22 02:02:49] operator / voice_transcript_partial / voice: the put the putting the to normandy daily livelihood good luck somewhere between
  meta: kind=partial | timestamp=1787335369.2104046 | source=vosk | rms=267 | updated_at=1787335368.910162 | frequency_hz=330.6
- [2026-08-22 02:02:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335369.4119816 | source=vosk | rms=267 | updated_at=1787335368.910162 | frequency_hz=330.6
- [2026-08-22 02:02:49] operator / voice_transcript_partial / voice: the put the putting the to normandy daily livelihood good luck somewhere big
  meta: kind=partial | timestamp=1787335369.4765596 | source=vosk | rms=267 | updated_at=1787335368.910162 | frequency_hz=330.6
- [2026-08-22 02:02:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335369.660947 | source=vosk | rms=165 | updated_at=1787335369.660947 | frequency_hz=330.6
- [2026-08-22 02:02:49] operator / voice_transcript_partial / voice: the put the putting the to normandy daily livelihood good luck somewhere begun to
  meta: kind=partial | timestamp=1787335369.7183454 | source=vosk | rms=165 | updated_at=1787335369.660947 | frequency_hz=330.6
- [2026-08-22 02:02:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335370.1610122 | source=vosk | rms=165 | updated_at=1787335369.660947 | frequency_hz=330.6
- [2026-08-22 02:02:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335373.4108443 | source=vosk | rms=1204 | updated_at=1787335373.4108443 | frequency_hz=330.6
- [2026-08-22 02:02:53] operator / voice_transcript_partial / voice: the put the putting the to normandy daily livelihood good luck somewhere big the movement
  meta: kind=partial | timestamp=1787335373.450033 | source=vosk | rms=1204 | updated_at=1787335373.4108443 | frequency_hz=330.6
- [2026-08-22 02:02:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335373.664903 | source=vosk | rms=1203 | updated_at=1787335373.664903 | frequency_hz=330.6
- [2026-08-22 02:02:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335373.9359593 | source=vosk | rms=1201 | updated_at=1787335373.9359593 | frequency_hz=330.6
- [2026-08-22 02:02:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335374.4212172 | source=vosk | rms=1201 | updated_at=1787335373.9359593 | frequency_hz=330.6
- [2026-08-22 02:02:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335375.46675 | source=vosk | rms=1201 | updated_at=1787335373.9359593 | frequency_hz=330.6
- [2026-08-22 02:02:55] operator / voice_transcript_final / voice: the to put the putting the to normandy daily livelihood good luck somewhere big the movement
  meta: kind=final | timestamp=1787335375.8771648 | source=final | rms=1201 | updated_at=1787335373.9359593 | frequency_hz=330.6
- [2026-08-22 02:02:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335376.0306768 | source=vosk | rms=1201 | updated_at=1787335373.9359593 | frequency_hz=330.6
- [2026-08-22 02:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335376.08018 | source=vosk | rms=302 | updated_at=1787335376.08018 | frequency_hz=330.6
- [2026-08-22 02:02:56] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787335376.1694376 | source=vosk | rms=292 | updated_at=1787335376.0942543 | frequency_hz=330.6
- [2026-08-22 02:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335376.3222282 | source=vosk | rms=360 | updated_at=1787335376.3222282 | frequency_hz=330.6
- [2026-08-22 02:02:56] operator / voice_transcript_partial / voice: the a lot
  meta: kind=partial | timestamp=1787335376.380195 | source=vosk | rms=360 | updated_at=1787335376.3222282 | frequency_hz=330.6
- [2026-08-22 02:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335376.522377 | source=vosk | rms=391 | updated_at=1787335376.428754 | frequency_hz=330.6
- [2026-08-22 02:02:56] operator / voice_transcript_partial / voice: the end of the
  meta: kind=partial | timestamp=1787335376.522377 | source=vosk | rms=391 | updated_at=1787335376.428754 | frequency_hz=330.6
- [2026-08-22 02:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335376.7440722 | source=vosk | rms=172 | updated_at=1787335376.663057 | frequency_hz=330.6
- [2026-08-22 02:02:56] operator / voice_transcript_partial / voice: the end of the gotten sick
  meta: kind=partial | timestamp=1787335376.7440722 | source=vosk | rms=172 | updated_at=1787335376.663057 | frequency_hz=330.6
- [2026-08-22 02:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335376.9671967 | source=vosk | rms=287 | updated_at=1787335376.9106836 | frequency_hz=330.6
- [2026-08-22 02:02:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335377.1604006 | source=vosk | rms=227 | updated_at=1787335377.1604006 | frequency_hz=330.6
- [2026-08-22 02:02:57] operator / voice_transcript_partial / voice: the end of the gotten sick as long
  meta: kind=partial | timestamp=1787335377.2272854 | source=vosk | rms=227 | updated_at=1787335377.1604006 | frequency_hz=330.6
- [2026-08-22 02:02:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335377.4443 | source=vosk | rms=213 | updated_at=1787335377.4443 | frequency_hz=330.6
- [2026-08-22 02:02:57] operator / voice_transcript_partial / voice: the end of the good guys come on a high
  meta: kind=partial | timestamp=1787335377.5207796 | source=vosk | rms=213 | updated_at=1787335377.4443 | frequency_hz=330.6
- [2026-08-22 02:02:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335377.669686 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:02:57] operator / voice_transcript_partial / voice: the end of the gotta go along the highway
  meta: kind=partial | timestamp=1787335377.7192879 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:02:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335378.1608756 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:02:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335379.6623805 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:02:59] operator / voice_transcript_partial / voice: the end of the gotta go along the highway mean
  meta: kind=partial | timestamp=1787335379.72976 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:02:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335379.950512 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:03:00] operator / voice_transcript_partial / voice: the end of the gotta go along the highway mean yeah
  meta: kind=partial | timestamp=1787335380.019104 | source=vosk | rms=237 | updated_at=1787335377.669686 | frequency_hz=330.6
- [2026-08-22 02:03:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335380.4259896 | source=vosk | rms=261 | updated_at=1787335380.4259896 | frequency_hz=330.6
- [2026-08-22 02:03:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335380.6625082 | source=vosk | rms=215 | updated_at=1787335380.6625082 | frequency_hz=330.6
- [2026-08-22 02:03:01] operator / voice_transcript_final / voice: the end of the gotten sick come on the highway mean yeah
  meta: kind=final | timestamp=1787335381.1659737 | source=final | rms=215 | updated_at=1787335380.6625082 | frequency_hz=330.6
- [2026-08-22 02:03:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335381.309263 | source=vosk | rms=215 | updated_at=1787335380.6625082 | frequency_hz=330.6
- [2026-08-22 02:03:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335381.4109306 | source=vosk | rms=215 | updated_at=1787335380.6625082 | frequency_hz=330.6
- [2026-08-22 02:03:01] operator / voice_transcript_partial / voice: been
  meta: kind=partial | timestamp=1787335381.765951 | source=vosk | rms=229 | updated_at=1787335381.6613755 | frequency_hz=330.6
- [2026-08-22 02:03:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335381.9113107 | source=vosk | rms=170 | updated_at=1787335381.9113107 | frequency_hz=330.6
- [2026-08-22 02:03:01] operator / voice_transcript_partial / voice: by an omelet one
  meta: kind=partial | timestamp=1787335381.9535482 | source=vosk | rms=170 | updated_at=1787335381.9113107 | frequency_hz=330.6
- [2026-08-22 02:03:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335382.1621718 | source=vosk | rms=500 | updated_at=1787335382.1621718 | frequency_hz=330.6
- [2026-08-22 02:03:02] operator / voice_transcript_partial / voice: by an omelet wanna read
  meta: kind=partial | timestamp=1787335382.2284925 | source=vosk | rms=500 | updated_at=1787335382.1621718 | frequency_hz=330.6
- [2026-08-22 02:03:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335382.4683402 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:02] operator / voice_transcript_partial / voice: by an omelet one of the
  meta: kind=partial | timestamp=1787335382.5783982 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335382.682266 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:02] operator / voice_transcript_partial / voice: by an omelet wanna read his
  meta: kind=partial | timestamp=1787335382.792393 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335383.4269383 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335386.4111524 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:06] operator / voice_transcript_partial / voice: by an omelet one of the this moment when
  meta: kind=partial | timestamp=1787335386.4691665 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335386.9174004 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335387.9165173 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:08] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy
  meta: kind=partial | timestamp=1787335388.0080447 | source=vosk | rms=191 | updated_at=1787335382.4683402 | frequency_hz=330.6
- [2026-08-22 02:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335388.1631584 | source=vosk | rms=193 | updated_at=1787335388.1631584 | frequency_hz=330.6
- [2026-08-22 02:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335388.4132817 | source=vosk | rms=504 | updated_at=1787335388.4132817 | frequency_hz=330.6
- [2026-08-22 02:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335388.662762 | source=vosk | rms=504 | updated_at=1787335388.4132817 | frequency_hz=330.6
- [2026-08-22 02:03:08] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy be peace
  meta: kind=partial | timestamp=1787335388.743741 | source=vosk | rms=504 | updated_at=1787335388.4132817 | frequency_hz=330.6
- [2026-08-22 02:03:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335389.1610663 | source=vosk | rms=471 | updated_at=1787335389.1610663 | frequency_hz=330.6
- [2026-08-22 02:03:09] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy bbc
  meta: kind=partial | timestamp=1787335389.1789825 | source=vosk | rms=471 | updated_at=1787335389.1610663 | frequency_hz=330.6
- [2026-08-22 02:03:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335389.4563153 | source=vosk | rms=1103 | updated_at=1787335389.4563153 | frequency_hz=330.6
- [2026-08-22 02:03:09] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy bbc to
  meta: kind=partial | timestamp=1787335389.500422 | source=vosk | rms=1103 | updated_at=1787335389.4563153 | frequency_hz=330.6
- [2026-08-22 02:03:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335389.6805108 | source=vosk | rms=1202 | updated_at=1787335389.6805108 | frequency_hz=330.6
- [2026-08-22 02:03:09] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy bbc to be
  meta: kind=partial | timestamp=1787335389.7486749 | source=vosk | rms=1202 | updated_at=1787335389.6805108 | frequency_hz=330.6
- [2026-08-22 02:03:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335389.9133465 | source=vosk | rms=264 | updated_at=1787335389.9133465 | frequency_hz=330.6
- [2026-08-22 02:03:10] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy bbc it
  meta: kind=partial | timestamp=1787335390.0446644 | source=vosk | rms=264 | updated_at=1787335389.9133465 | frequency_hz=330.6
- [2026-08-22 02:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335390.198871 | source=vosk | rms=166 | updated_at=1787335390.198871 | frequency_hz=330.6
- [2026-08-22 02:03:10] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy bbc to be
  meta: kind=partial | timestamp=1787335390.2897646 | source=vosk | rms=166 | updated_at=1787335390.198871 | frequency_hz=330.6
- [2026-08-22 02:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335390.6617172 | source=vosk | rms=161 | updated_at=1787335390.6617172 | frequency_hz=330.6
- [2026-08-22 02:03:10] operator / voice_transcript_partial / voice: by an omelet one of the this moment when the enemy bbc to be cpc
  meta: kind=partial | timestamp=1787335390.6889298 | source=vosk | rms=161 | updated_at=1787335390.6617172 | frequency_hz=330.6
- [2026-08-22 02:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335390.9362803 | source=vosk | rms=205 | updated_at=1787335390.9362803 | frequency_hz=330.6
- [2026-08-22 02:03:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335391.161161 | source=vosk | rms=205 | updated_at=1787335390.9362803 | frequency_hz=330.6
- [2026-08-22 02:03:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335391.66745 | source=vosk | rms=205 | updated_at=1787335390.9362803 | frequency_hz=330.6
- [2026-08-22 02:03:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335392.9105334 | source=vosk | rms=275 | updated_at=1787335392.9105334 | frequency_hz=330.6
- [2026-08-22 02:03:13] operator / voice_transcript_final / voice: by an not one of the isn t moment when the enemy bbc to be cpc
  meta: kind=final | timestamp=1787335393.660171 | source=final | rms=275 | updated_at=1787335392.9105334 | frequency_hz=330.6
- [2026-08-22 02:03:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335393.9424686 | source=vosk | rms=275 | updated_at=1787335392.9105334 | frequency_hz=330.6
- [2026-08-22 02:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335393.9424686 | source=vosk | rms=436 | updated_at=1787335393.9424686 | frequency_hz=330.6
- [2026-08-22 02:03:14] operator / voice_transcript_partial / voice: i don't
  meta: kind=partial | timestamp=1787335394.0513449 | source=vosk | rms=436 | updated_at=1787335393.9424686 | frequency_hz=330.6
- [2026-08-22 02:03:14] operator / voice_transcript_partial / voice: monogamy
  meta: kind=partial | timestamp=1787335394.1083648 | source=vosk | rms=389 | updated_at=1787335394.0523508 | frequency_hz=330.6
- [2026-08-22 02:03:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335394.153953 | source=vosk | rms=233 | updated_at=1787335394.1093647 | frequency_hz=330.6
- [2026-08-22 02:03:14] operator / voice_transcript_partial / voice: monogamy and
  meta: kind=partial | timestamp=1787335394.2169075 | source=vosk | rms=157 | updated_at=1787335394.162099 | frequency_hz=330.6
- [2026-08-22 02:03:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335394.4110136 | source=vosk | rms=271 | updated_at=1787335394.4110136 | frequency_hz=330.6
- [2026-08-22 02:03:14] operator / voice_transcript_partial / voice: monogamy and get the public
  meta: kind=partial | timestamp=1787335394.4757142 | source=vosk | rms=271 | updated_at=1787335394.4110136 | frequency_hz=330.6
- [2026-08-22 02:03:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335394.6623387 | source=vosk | rms=400 | updated_at=1787335394.6623387 | frequency_hz=330.6
- [2026-08-22 02:03:14] operator / voice_transcript_partial / voice: monogamy and get the public but google
  meta: kind=partial | timestamp=1787335394.6853962 | source=vosk | rms=400 | updated_at=1787335394.6623387 | frequency_hz=330.6
- [2026-08-22 02:03:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335394.9181054 | source=vosk | rms=385 | updated_at=1787335394.9181054 | frequency_hz=330.6
- [2026-08-22 02:03:14] operator / voice_transcript_partial / voice: monogamy and get the public but
  meta: kind=partial | timestamp=1787335394.9773667 | source=vosk | rms=385 | updated_at=1787335394.9181054 | frequency_hz=330.6
- [2026-08-22 02:03:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335395.333177 | source=vosk | rms=1203 | updated_at=1787335395.333177 | frequency_hz=330.6
- [2026-08-22 02:03:15] operator / voice_transcript_partial / voice: monogamy and get the public but going to
  meta: kind=partial | timestamp=1787335395.4037645 | source=vosk | rms=1203 | updated_at=1787335395.333177 | frequency_hz=330.6
- [2026-08-22 02:03:15] operator / voice_transcript_partial / voice: monogamy and get the public but the
  meta: kind=partial | timestamp=1787335395.4346905 | source=vosk | rms=314 | updated_at=1787335395.411136 | frequency_hz=330.6
- [2026-08-22 02:03:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335395.9105713 | source=vosk | rms=314 | updated_at=1787335395.411136 | frequency_hz=330.6
- [2026-08-22 02:03:15] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue
  meta: kind=partial | timestamp=1787335395.9231107 | source=vosk | rms=314 | updated_at=1787335395.411136 | frequency_hz=330.6
- [2026-08-22 02:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335396.163056 | source=vosk | rms=314 | updated_at=1787335395.411136 | frequency_hz=330.6
- [2026-08-22 02:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335396.41929 | source=vosk | rms=226 | updated_at=1787335396.41929 | frequency_hz=330.6
- [2026-08-22 02:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335396.6944304 | source=vosk | rms=714 | updated_at=1787335396.6944304 | frequency_hz=330.6
- [2026-08-22 02:03:16] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of
  meta: kind=partial | timestamp=1787335396.7183518 | source=vosk | rms=714 | updated_at=1787335396.6944304 | frequency_hz=330.6
- [2026-08-22 02:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335396.9180932 | source=vosk | rms=327 | updated_at=1787335396.9180932 | frequency_hz=330.6
- [2026-08-22 02:03:17] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a
  meta: kind=partial | timestamp=1787335397.0022135 | source=vosk | rms=327 | updated_at=1787335396.9180932 | frequency_hz=330.6
- [2026-08-22 02:03:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335397.1611702 | source=vosk | rms=327 | updated_at=1787335396.9180932 | frequency_hz=330.6
- [2026-08-22 02:03:17] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is
  meta: kind=partial | timestamp=1787335397.1857305 | source=vosk | rms=327 | updated_at=1787335396.9180932 | frequency_hz=330.6
- [2026-08-22 02:03:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335397.426906 | source=vosk | rms=305 | updated_at=1787335397.426906 | frequency_hz=330.6
- [2026-08-22 02:03:17] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a little much
  meta: kind=partial | timestamp=1787335397.4491422 | source=vosk | rms=305 | updated_at=1787335397.426906 | frequency_hz=330.6
- [2026-08-22 02:03:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335397.6623924 | source=vosk | rms=371 | updated_at=1787335397.6623924 | frequency_hz=330.6
- [2026-08-22 02:03:17] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a new month but
  meta: kind=partial | timestamp=1787335397.7244928 | source=vosk | rms=371 | updated_at=1787335397.6623924 | frequency_hz=330.6
- [2026-08-22 02:03:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335397.981301 | source=vosk | rms=232 | updated_at=1787335397.981301 | frequency_hz=330.6
- [2026-08-22 02:03:18] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a little much for personal
  meta: kind=partial | timestamp=1787335398.0834615 | source=vosk | rms=232 | updated_at=1787335397.981301 | frequency_hz=330.6
- [2026-08-22 02:03:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335398.1662076 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:18] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a little my boss and only
  meta: kind=partial | timestamp=1787335398.224121 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335398.5136483 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:18] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a little my boss animal
  meta: kind=partial | timestamp=1787335398.615471 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335398.710546 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:18] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a little my boss animal elizabeth
  meta: kind=partial | timestamp=1787335398.710546 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335399.1652317 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:19] operator / voice_transcript_partial / voice: monogamy and get the public but i'm an issue of one is a little my boss animal elizabeth go
  meta: kind=partial | timestamp=1787335399.1777513 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335399.4107566 | source=vosk | rms=354 | updated_at=1787335398.1662076 | frequency_hz=330.6
- [2026-08-22 02:03:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335399.9780495 | source=vosk | rms=177 | updated_at=1787335399.9780495 | frequency_hz=330.6
- [2026-08-22 02:03:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335400.179867 | source=vosk | rms=430 | updated_at=1787335400.179867 | frequency_hz=330.6
- [2026-08-22 02:03:20] operator / voice_transcript_final / voice: monogamy and get the public but i m an issue of one is a little my boss animal elizabeth go
  meta: kind=final | timestamp=1787335400.66225 | source=final | rms=430 | updated_at=1787335400.179867 | frequency_hz=330.6
- [2026-08-22 02:03:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335401.2563448 | source=vosk | rms=430 | updated_at=1787335400.179867 | frequency_hz=330.6
- [2026-08-22 02:03:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335401.2563448 | source=vosk | rms=326 | updated_at=1787335401.2563448 | frequency_hz=330.6
- [2026-08-22 02:03:21] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1787335401.328359 | source=vosk | rms=326 | updated_at=1787335401.2563448 | frequency_hz=330.6
- [2026-08-22 02:03:21] operator / voice_transcript_partial / voice: good as he
  meta: kind=partial | timestamp=1787335401.369282 | source=vosk | rms=488 | updated_at=1787335401.3293614 | frequency_hz=330.6
- [2026-08-22 02:03:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335401.4403386 | source=vosk | rms=290 | updated_at=1787335401.3723166 | frequency_hz=330.6
- [2026-08-22 02:03:21] operator / voice_transcript_partial / voice: good as he would
  meta: kind=partial | timestamp=1787335401.4403386 | source=vosk | rms=290 | updated_at=1787335401.3723166 | frequency_hz=330.6
- [2026-08-22 02:03:21] operator / voice_transcript_partial / voice: good as he would you know they wouldn't
  meta: kind=partial | timestamp=1787335401.602268 | source=vosk | rms=459 | updated_at=1787335401.4403386 | frequency_hz=330.6
- [2026-08-22 02:03:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335401.702492 | source=vosk | rms=423 | updated_at=1787335401.602268 | frequency_hz=330.6
- [2026-08-22 02:03:21] operator / voice_transcript_partial / voice: good as he would you know they wouldn't assume
  meta: kind=partial | timestamp=1787335401.702492 | source=vosk | rms=423 | updated_at=1787335401.602268 | frequency_hz=330.6
- [2026-08-22 02:03:21] operator / voice_transcript_partial / voice: good as he would you know them whenever
  meta: kind=partial | timestamp=1787335401.799304 | source=vosk | rms=597 | updated_at=1787335401.702492 | frequency_hz=330.6
- [2026-08-22 02:03:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335402.413331 | source=vosk | rms=597 | updated_at=1787335401.702492 | frequency_hz=330.6
- [2026-08-22 02:03:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335404.95985 | source=vosk | rms=277 | updated_at=1787335404.95985 | frequency_hz=330.6
- [2026-08-22 02:03:25] operator / voice_transcript_partial / voice: good as he would you know them whenever somebody
  meta: kind=partial | timestamp=1787335405.0247488 | source=vosk | rms=277 | updated_at=1787335404.95985 | frequency_hz=330.6
- [2026-08-22 02:03:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335405.6611342 | source=vosk | rms=277 | updated_at=1787335404.95985 | frequency_hz=330.6
- [2026-08-22 02:03:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335405.911374 | source=vosk | rms=220 | updated_at=1787335405.911374 | frequency_hz=330.6
- [2026-08-22 02:03:25] operator / voice_transcript_partial / voice: good as he would you know they've been a little bumps and
  meta: kind=partial | timestamp=1787335405.9843054 | source=vosk | rms=220 | updated_at=1787335405.911374 | frequency_hz=330.6
- [2026-08-22 02:03:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335406.4123905 | source=vosk | rms=220 | updated_at=1787335405.911374 | frequency_hz=330.6
- [2026-08-22 02:03:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335406.6625762 | source=vosk | rms=220 | updated_at=1787335405.911374 | frequency_hz=330.6
- [2026-08-22 02:03:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335407.1992335 | source=vosk | rms=220 | updated_at=1787335405.911374 | frequency_hz=330.6
- [2026-08-22 02:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335412.1215322 | source=vosk | rms=1202 | updated_at=1787335412.1215322 | frequency_hz=374.0
- [2026-08-22 02:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335412.3821425 | source=vosk | rms=1203 | updated_at=1787335412.3821425 | frequency_hz=374.0
- [2026-08-22 02:03:32] operator / voice_transcript_partial / voice: good as he would you know they've been a little bumps and learn
  meta: kind=partial | timestamp=1787335412.470915 | source=vosk | rms=1203 | updated_at=1787335412.3821425 | frequency_hz=374.0
- [2026-08-22 02:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335412.643555 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335413.1437118 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335414.363445 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:35] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787335415.2786329 | source=state | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335415.472185 | source=state | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335415.472185 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:36] operator / voice_transcript_partial / voice: ones are
  meta: kind=partial | timestamp=1787335416.7157617 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335417.0915549 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:37] operator / voice_transcript_partial / voice: ones are people
  meta: kind=partial | timestamp=1787335417.124619 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335417.6012266 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:38] operator / voice_transcript_final / voice: ones are people
  meta: kind=final | timestamp=1787335418.9178257 | source=final | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335419.621073 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:39] operator / voice_transcript_partial / voice: ones are people
  meta: kind=partial | timestamp=1787335419.649665 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335419.8535836 | source=vosk | rms=1178 | updated_at=1787335412.643555 | frequency_hz=374.0
- [2026-08-22 02:03:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335420.1149507 | source=vosk | rms=311 | updated_at=1787335420.1149507 | frequency_hz=374.0
- [2026-08-22 02:03:40] operator / voice_transcript_final / voice: ones are people
  meta: kind=final | timestamp=1787335420.6503801 | source=final | rms=311 | updated_at=1787335420.1149507 | frequency_hz=374.0
- [2026-08-22 02:03:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335420.956669 | source=vosk | rms=311 | updated_at=1787335420.1149507 | frequency_hz=374.0
- [2026-08-22 02:03:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335420.956669 | source=vosk | rms=311 | updated_at=1787335420.1149507 | frequency_hz=374.0
- [2026-08-22 02:03:40] operator / voice_transcript_partial / voice: cool
  meta: kind=partial | timestamp=1787335420.9862332 | source=vosk | rms=311 | updated_at=1787335420.1149507 | frequency_hz=374.0
- [2026-08-22 02:03:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335421.1412263 | source=vosk | rms=311 | updated_at=1787335420.1149507 | frequency_hz=374.0
- [2026-08-22 02:03:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335421.5913074 | source=vosk | rms=808 | updated_at=1787335421.5913074 | frequency_hz=374.0
- [2026-08-22 02:03:41] operator / voice_transcript_final / voice: cool
  meta: kind=final | timestamp=1787335421.856013 | source=final | rms=808 | updated_at=1787335421.5913074 | frequency_hz=374.0
- [2026-08-22 02:03:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335422.0995398 | source=vosk | rms=808 | updated_at=1787335421.5913074 | frequency_hz=374.0
- [2026-08-22 02:03:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335423.1208987 | source=vosk | rms=808 | updated_at=1787335421.5913074 | frequency_hz=374.0
- [2026-08-22 02:03:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335423.5908692 | source=vosk | rms=808 | updated_at=1787335421.5913074 | frequency_hz=374.0
- [2026-08-22 02:03:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335426.358521 | source=vosk | rms=337 | updated_at=1787335426.3575184 | frequency_hz=374.0
- [2026-08-22 02:03:48] operator / voice_transcript_partial / voice: but it
  meta: kind=partial | timestamp=1787335428.3899758 | source=vosk | rms=204 | updated_at=1787335428.341541 | frequency_hz=374.0
- [2026-08-22 02:03:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335428.591598 | source=vosk | rms=204 | updated_at=1787335428.341541 | frequency_hz=374.0
- [2026-08-22 02:03:48] operator / voice_transcript_partial / voice: but i am a little
  meta: kind=partial | timestamp=1787335428.6378627 | source=vosk | rms=204 | updated_at=1787335428.341541 | frequency_hz=374.0
- [2026-08-22 02:03:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335428.8416092 | source=vosk | rms=204 | updated_at=1787335428.341541 | frequency_hz=374.0
- [2026-08-22 02:03:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335429.342773 | source=vosk | rms=204 | updated_at=1787335428.341541 | frequency_hz=374.0
- [2026-08-22 02:03:49] operator / voice_transcript_partial / voice: but i am a little boy
  meta: kind=partial | timestamp=1787335429.3607054 | source=vosk | rms=204 | updated_at=1787335428.341541 | frequency_hz=374.0
- [2026-08-22 02:03:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335429.5939248 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:49] operator / voice_transcript_partial / voice: but i am a little boy on
  meta: kind=partial | timestamp=1787335429.6139472 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335429.844361 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335430.344413 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335432.3733048 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335433.1478312 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:53] operator / voice_transcript_final / voice: but i am a little boy on berlin
  meta: kind=final | timestamp=1787335433.5813804 | source=final | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335433.8020682 | source=vosk | rms=328 | updated_at=1787335429.5939248 | frequency_hz=374.0
- [2026-08-22 02:03:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335433.8020682 | source=vosk | rms=134 | updated_at=1787335433.8020682 | frequency_hz=374.0
- [2026-08-22 02:03:55] operator / voice_transcript_partial / voice: move along with it
  meta: kind=partial | timestamp=1787335435.1679761 | source=vosk | rms=261 | updated_at=1787335434.8811467 | frequency_hz=374.0
- [2026-08-22 02:03:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335435.5910351 | source=vosk | rms=261 | updated_at=1787335434.8811467 | frequency_hz=374.0
- [2026-08-22 02:03:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335436.6145313 | source=vosk | rms=1204 | updated_at=1787335436.6145313 | frequency_hz=374.0
- [2026-08-22 02:03:56] operator / voice_transcript_partial / voice: with it's the most
  meta: kind=partial | timestamp=1787335436.6907828 | source=vosk | rms=1204 | updated_at=1787335436.6145313 | frequency_hz=374.0
- [2026-08-22 02:03:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335436.841435 | source=vosk | rms=1201 | updated_at=1787335436.841435 | frequency_hz=374.0
- [2026-08-22 02:03:56] operator / voice_transcript_partial / voice: with it's them on
  meta: kind=partial | timestamp=1787335436.900605 | source=vosk | rms=1201 | updated_at=1787335436.841435 | frequency_hz=374.0
- [2026-08-22 02:03:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335437.091083 | source=vosk | rms=1040 | updated_at=1787335437.091083 | frequency_hz=374.0
- [2026-08-22 02:03:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335437.6017804 | source=vosk | rms=1040 | updated_at=1787335437.091083 | frequency_hz=374.0
- [2026-08-22 02:03:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335437.8435304 | source=vosk | rms=206 | updated_at=1787335437.8435304 | frequency_hz=374.0
- [2026-08-22 02:03:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335438.0914626 | source=vosk | rms=167 | updated_at=1787335438.0914626 | frequency_hz=374.0
- [2026-08-22 02:03:58] operator / voice_transcript_partial / voice: with it's the
  meta: kind=partial | timestamp=1787335438.1342366 | source=vosk | rms=167 | updated_at=1787335438.0914626 | frequency_hz=374.0
- [2026-08-22 02:03:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335438.3426793 | source=vosk | rms=171 | updated_at=1787335438.3426793 | frequency_hz=374.0
- [2026-08-22 02:03:58] operator / voice_transcript_partial / voice: move along with his family moved to
  meta: kind=partial | timestamp=1787335438.3808692 | source=vosk | rms=171 | updated_at=1787335438.3426793 | frequency_hz=374.0
- [2026-08-22 02:03:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335438.5972674 | source=vosk | rms=191 | updated_at=1787335438.5972674 | frequency_hz=374.0
- [2026-08-22 02:03:58] operator / voice_transcript_partial / voice: move along with his family moved
  meta: kind=partial | timestamp=1787335438.666279 | source=vosk | rms=191 | updated_at=1787335438.5972674 | frequency_hz=374.0
- [2026-08-22 02:03:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335438.845553 | source=vosk | rms=248 | updated_at=1787335438.845553 | frequency_hz=374.0
- [2026-08-22 02:03:58] operator / voice_transcript_partial / voice: move along with his family moved to
  meta: kind=partial | timestamp=1787335438.9305956 | source=vosk | rms=248 | updated_at=1787335438.845553 | frequency_hz=374.0
- [2026-08-22 02:03:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335439.0974631 | source=vosk | rms=388 | updated_at=1787335439.0974631 | frequency_hz=374.0
- [2026-08-22 02:03:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335439.6448064 | source=vosk | rms=388 | updated_at=1787335439.0974631 | frequency_hz=374.0
- [2026-08-22 02:03:59] operator / voice_transcript_partial / voice: move along with his family moved to allow you
  meta: kind=partial | timestamp=1787335439.752218 | source=vosk | rms=388 | updated_at=1787335439.0974631 | frequency_hz=374.0
- [2026-08-22 02:04:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335440.3971524 | source=vosk | rms=388 | updated_at=1787335439.0974631 | frequency_hz=374.0
- [2026-08-22 02:04:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335443.4061713 | source=vosk | rms=396 | updated_at=1787335443.4061713 | frequency_hz=374.0
- [2026-08-22 02:04:03] operator / voice_transcript_partial / voice: move along with his family moved to a lot of
  meta: kind=partial | timestamp=1787335443.4487357 | source=vosk | rms=396 | updated_at=1787335443.4061713 | frequency_hz=374.0
- [2026-08-22 02:04:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335443.6408594 | source=vosk | rms=448 | updated_at=1787335443.6408594 | frequency_hz=374.0
- [2026-08-22 02:04:03] operator / voice_transcript_partial / voice: move along with his family moved to a lot of people
  meta: kind=partial | timestamp=1787335443.6710665 | source=vosk | rms=448 | updated_at=1787335443.6408594 | frequency_hz=374.0
- [2026-08-22 02:04:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335443.9371903 | source=vosk | rms=361 | updated_at=1787335443.9371903 | frequency_hz=374.0
- [2026-08-22 02:04:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335444.4113128 | source=vosk | rms=361 | updated_at=1787335443.9371903 | frequency_hz=374.0
- [2026-08-22 02:04:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335445.9327612 | source=vosk | rms=317 | updated_at=1787335445.9327612 | frequency_hz=374.0
- [2026-08-22 02:04:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335446.1426172 | source=vosk | rms=317 | updated_at=1787335445.9327612 | frequency_hz=374.0
- [2026-08-22 02:04:06] operator / voice_transcript_partial / voice: move along with his family moved to a lot of people's be
  meta: kind=partial | timestamp=1787335446.1636603 | source=vosk | rms=317 | updated_at=1787335445.9327612 | frequency_hz=374.0
- [2026-08-22 02:04:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335446.6415722 | source=vosk | rms=317 | updated_at=1787335445.9327612 | frequency_hz=374.0
- [2026-08-22 02:04:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335447.6415634 | source=vosk | rms=211 | updated_at=1787335447.6415634 | frequency_hz=374.0
- [2026-08-22 02:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335448.1553817 | source=vosk | rms=1205 | updated_at=1787335448.1553817 | frequency_hz=374.0
- [2026-08-22 02:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335448.3942068 | source=vosk | rms=1204 | updated_at=1787335448.3942068 | frequency_hz=374.0
- [2026-08-22 02:04:09] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787335449.439988 | source=state | rms=1204 | updated_at=1787335448.3942068 | frequency_hz=374.0
- [2026-08-22 02:04:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335449.7983155 | source=state | rms=1204 | updated_at=1787335448.3942068 | frequency_hz=374.0
- [2026-08-22 02:04:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335449.7993193 | source=vosk | rms=1031 | updated_at=1787335449.7993193 | frequency_hz=374.0
- [2026-08-22 02:04:10] operator / voice_transcript_partial / voice: come
  meta: kind=partial | timestamp=1787335450.068025 | source=vosk | rms=207 | updated_at=1787335449.9127045 | frequency_hz=374.0
- [2026-08-22 02:04:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335450.6435568 | source=vosk | rms=540 | updated_at=1787335450.1544938 | frequency_hz=374.0
- [2026-08-22 02:04:11] operator / voice_transcript_final / voice: come
  meta: kind=final | timestamp=1787335451.609643 | source=final | rms=540 | updated_at=1787335450.1544938 | frequency_hz=374.0
- [2026-08-22 02:04:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335452.6564038 | source=vosk | rms=442 | updated_at=1787335452.6564038 | frequency_hz=374.0
- [2026-08-22 02:04:13] operator / voice_transcript_partial / voice: obama
  meta: kind=partial | timestamp=1787335453.4583392 | source=vosk | rms=213 | updated_at=1787335453.3911018 | frequency_hz=374.0
- [2026-08-22 02:04:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335453.891558 | source=vosk | rms=213 | updated_at=1787335453.3911018 | frequency_hz=374.0
- [2026-08-22 02:04:14] operator / voice_transcript_final / voice: obama
  meta: kind=final | timestamp=1787335454.858536 | source=final | rms=213 | updated_at=1787335453.3911018 | frequency_hz=374.0
- [2026-08-22 02:04:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335457.4078572 | source=vosk | rms=213 | updated_at=1787335453.3911018 | frequency_hz=374.0
- [2026-08-22 02:04:17] operator / voice_transcript_partial / voice: all following a little
  meta: kind=partial | timestamp=1787335457.5511897 | source=vosk | rms=213 | updated_at=1787335453.3911018 | frequency_hz=374.0
- [2026-08-22 02:04:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335457.6413114 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:17] operator / voice_transcript_partial / voice: i'm leaving your abdominals of the box
  meta: kind=partial | timestamp=1787335457.6909635 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335458.2210488 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335458.8913672 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:19] operator / voice_transcript_partial / voice: no comment on something oxycodone
  meta: kind=partial | timestamp=1787335459.0326247 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335459.7610748 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335462.659708 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:23] operator / voice_transcript_final / voice: come leaving your abdominals will be box
  meta: kind=final | timestamp=1787335463.1769822 | source=final | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335463.3143635 | source=vosk | rms=215 | updated_at=1787335457.6413114 | frequency_hz=374.0
- [2026-08-22 02:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335463.3143635 | source=vosk | rms=719 | updated_at=1787335463.3143635 | frequency_hz=374.0
- [2026-08-22 02:04:23] operator / voice_transcript_partial / voice: this period
  meta: kind=partial | timestamp=1787335463.5339062 | source=vosk | rms=298 | updated_at=1787335463.3305013 | frequency_hz=374.0
- [2026-08-22 02:04:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335464.1451259 | source=vosk | rms=298 | updated_at=1787335463.3305013 | frequency_hz=374.0
- [2026-08-22 02:04:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335467.892394 | source=vosk | rms=298 | updated_at=1787335463.3305013 | frequency_hz=374.0
- [2026-08-22 02:04:27] operator / voice_transcript_partial / voice: the school
  meta: kind=partial | timestamp=1787335467.9830472 | source=vosk | rms=298 | updated_at=1787335463.3305013 | frequency_hz=374.0
- [2026-08-22 02:04:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335468.1413858 | source=vosk | rms=298 | updated_at=1787335463.3305013 | frequency_hz=374.0
- [2026-08-22 02:04:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335468.646471 | source=vosk | rms=298 | updated_at=1787335463.3305013 | frequency_hz=374.0
- [2026-08-22 02:04:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335469.6411529 | source=vosk | rms=278 | updated_at=1787335469.6411529 | frequency_hz=374.0
- [2026-08-22 02:04:29] operator / voice_transcript_final / voice: the green
  meta: kind=final | timestamp=1787335469.9049635 | source=final | rms=278 | updated_at=1787335469.6411529 | frequency_hz=374.0
- [2026-08-22 02:04:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335470.1437528 | source=vosk | rms=278 | updated_at=1787335469.6411529 | frequency_hz=374.0
- [2026-08-22 02:04:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335470.418505 | source=vosk | rms=244 | updated_at=1787335470.417504 | frequency_hz=374.0
- [2026-08-22 02:04:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335471.656139 | source=vosk | rms=514 | updated_at=1787335470.8918986 | frequency_hz=374.0
- [2026-08-22 02:04:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335472.3966084 | source=vosk | rms=1200 | updated_at=1787335472.3956058 | frequency_hz=374.0
- [2026-08-22 02:04:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335473.3933387 | source=vosk | rms=1203 | updated_at=1787335472.6627228 | frequency_hz=374.0
- [2026-08-22 02:04:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335474.8918173 | source=vosk | rms=366 | updated_at=1787335474.8918173 | frequency_hz=374.0
- [2026-08-22 02:04:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335480.643931 | source=vosk | rms=137 | updated_at=1787335479.148547 | frequency_hz=374.0
- [2026-08-22 02:04:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335480.8949952 | source=vosk | rms=201 | updated_at=1787335480.8949952 | frequency_hz=374.0
- [2026-08-22 02:04:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335481.6426148 | source=vosk | rms=203 | updated_at=1787335481.164914 | frequency_hz=374.0
- [2026-08-22 02:04:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335481.8972566 | source=vosk | rms=203 | updated_at=1787335481.164914 | frequency_hz=374.0
- [2026-08-22 02:04:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335482.6424804 | source=vosk | rms=203 | updated_at=1787335481.164914 | frequency_hz=374.0
- [2026-08-22 02:04:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335484.1419532 | source=vosk | rms=123 | updated_at=1787335484.1419532 | frequency_hz=374.0
- [2026-08-22 02:04:46] operator / voice_transcript_partial / voice: instead
  meta: kind=partial | timestamp=1787335486.4228735 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335486.6778486 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:46] operator / voice_transcript_partial / voice: skinner
  meta: kind=partial | timestamp=1787335486.7611346 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335486.9223013 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335487.4395316 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335487.9053316 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335488.4334426 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335488.696814 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:49] operator / voice_transcript_final / voice: skinner
  meta: kind=final | timestamp=1787335489.0667553 | source=final | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335489.1038089 | source=vosk | rms=185 | updated_at=1787335486.3921394 | frequency_hz=374.0
- [2026-08-22 02:04:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335491.3928494 | source=vosk | rms=177 | updated_at=1787335490.9201324 | frequency_hz=374.0
- [2026-08-22 02:04:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335491.8920732 | source=vosk | rms=177 | updated_at=1787335490.9201324 | frequency_hz=374.0
- [2026-08-22 02:04:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335493.1418948 | source=vosk | rms=144 | updated_at=1787335492.1430552 | frequency_hz=374.0
- [2026-08-22 02:04:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335493.3978775 | source=vosk | rms=144 | updated_at=1787335492.1430552 | frequency_hz=374.0
- [2026-08-22 02:04:55] operator / voice_transcript_partial / voice: don't
  meta: kind=partial | timestamp=1787335495.420927 | source=vosk | rms=154 | updated_at=1787335494.9209805 | frequency_hz=374.0
- [2026-08-22 02:04:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335495.641519 | source=vosk | rms=154 | updated_at=1787335494.9209805 | frequency_hz=374.0
- [2026-08-22 02:04:55] operator / voice_transcript_partial / voice: still
  meta: kind=partial | timestamp=1787335495.712739 | source=vosk | rms=154 | updated_at=1787335494.9209805 | frequency_hz=374.0
- [2026-08-22 02:04:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335495.93029 | source=vosk | rms=277 | updated_at=1787335495.93029 | frequency_hz=374.0
- [2026-08-22 02:04:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335496.1949296 | source=vosk | rms=195 | updated_at=1787335496.1949296 | frequency_hz=374.0
- [2026-08-22 02:04:56] operator / voice_transcript_partial / voice: don't
  meta: kind=partial | timestamp=1787335496.2260058 | source=vosk | rms=195 | updated_at=1787335496.1949296 | frequency_hz=374.0
- [2026-08-22 02:04:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335496.4102285 | source=vosk | rms=162 | updated_at=1787335496.4102285 | frequency_hz=374.0
- [2026-08-22 02:04:56] operator / voice_transcript_partial / voice: don't know
  meta: kind=partial | timestamp=1787335496.4668663 | source=vosk | rms=162 | updated_at=1787335496.4102285 | frequency_hz=374.0
- [2026-08-22 02:04:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335496.669722 | source=vosk | rms=144 | updated_at=1787335496.669722 | frequency_hz=374.0
- [2026-08-22 02:04:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335496.930622 | source=vosk | rms=126 | updated_at=1787335496.930622 | frequency_hz=374.0
- [2026-08-22 02:04:57] operator / voice_transcript_final / voice: still know
  meta: kind=final | timestamp=1787335497.2449794 | source=final | rms=126 | updated_at=1787335496.930622 | frequency_hz=374.0
- [2026-08-22 02:04:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335497.3929513 | source=vosk | rms=126 | updated_at=1787335496.930622 | frequency_hz=374.0
- [2026-08-22 02:04:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335498.4139543 | source=vosk | rms=192 | updated_at=1787335498.4139543 | frequency_hz=374.0
- [2026-08-22 02:04:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335499.9243572 | source=vosk | rms=303 | updated_at=1787335499.391685 | frequency_hz=374.0
- [2026-08-22 02:05:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335500.4149604 | source=vosk | rms=209 | updated_at=1787335500.4149604 | frequency_hz=374.0
- [2026-08-22 02:05:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335500.892034 | source=vosk | rms=209 | updated_at=1787335500.4149604 | frequency_hz=374.0
- [2026-08-22 02:05:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335501.141249 | source=vosk | rms=209 | updated_at=1787335500.4149604 | frequency_hz=374.0
- [2026-08-22 02:05:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335501.6472833 | source=vosk | rms=209 | updated_at=1787335500.4149604 | frequency_hz=374.0
- [2026-08-22 02:05:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335502.5890205 | source=vosk | rms=126 | updated_at=1787335502.5890205 | frequency_hz=374.0
- [2026-08-22 02:05:03] operator / voice_transcript_partial / voice: meanwhile
  meta: kind=partial | timestamp=1787335503.1578405 | source=vosk | rms=145 | updated_at=1787335503.0891745 | frequency_hz=374.0
- [2026-08-22 02:05:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335503.3494885 | source=vosk | rms=145 | updated_at=1787335503.0891745 | frequency_hz=374.0
- [2026-08-22 02:05:03] operator / voice_transcript_partial / voice: mean hombre
  meta: kind=partial | timestamp=1787335503.37913 | source=vosk | rms=145 | updated_at=1787335503.0891745 | frequency_hz=374.0
- [2026-08-22 02:05:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335503.8315253 | source=vosk | rms=145 | updated_at=1787335503.0891745 | frequency_hz=374.0
- [2026-08-22 02:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335504.3319428 | source=vosk | rms=186 | updated_at=1787335504.3319428 | frequency_hz=374.0
- [2026-08-22 02:05:04] operator / voice_transcript_partial / voice: meanwhile
  meta: kind=partial | timestamp=1787335504.412807 | source=vosk | rms=186 | updated_at=1787335504.3319428 | frequency_hz=374.0
- [2026-08-22 02:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335504.6195762 | source=vosk | rms=163 | updated_at=1787335504.6195762 | frequency_hz=374.0
- [2026-08-22 02:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335504.8878171 | source=vosk | rms=163 | updated_at=1787335504.6195762 | frequency_hz=374.0
- [2026-08-22 02:05:05] operator / voice_transcript_final / voice: meanwhile
  meta: kind=final | timestamp=1787335505.4922397 | source=final | rms=163 | updated_at=1787335504.6195762 | frequency_hz=374.0
- [2026-08-22 02:05:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335505.5333223 | source=vosk | rms=163 | updated_at=1787335504.6195762 | frequency_hz=374.0
- [2026-08-22 02:05:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335505.5333223 | source=vosk | rms=144 | updated_at=1787335505.5333223 | frequency_hz=374.0
- [2026-08-22 02:05:06] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1787335506.8347228 | source=vosk | rms=1204 | updated_at=1787335506.7892869 | frequency_hz=374.0
- [2026-08-22 02:05:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335507.255627 | source=vosk | rms=1204 | updated_at=1787335506.7892869 | frequency_hz=374.0
- [2026-08-22 02:05:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335507.4919815 | source=vosk | rms=1204 | updated_at=1787335506.7892869 | frequency_hz=374.0
- [2026-08-22 02:05:07] operator / voice_transcript_partial / voice: don't
  meta: kind=partial | timestamp=1787335507.5165641 | source=vosk | rms=1204 | updated_at=1787335506.7892869 | frequency_hz=374.0
- [2026-08-22 02:05:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335507.7414124 | source=vosk | rms=221 | updated_at=1787335507.7414124 | frequency_hz=374.0
- [2026-08-22 02:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335508.0140388 | source=vosk | rms=237 | updated_at=1787335508.0140388 | frequency_hz=374.0
- [2026-08-22 02:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335508.3030694 | source=vosk | rms=128 | updated_at=1787335508.3030694 | frequency_hz=374.0
- [2026-08-22 02:05:08] operator / voice_transcript_final / voice: don t
  meta: kind=final | timestamp=1787335508.6338937 | source=final | rms=128 | updated_at=1787335508.3030694 | frequency_hz=374.0
- [2026-08-22 02:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335508.6755295 | source=vosk | rms=128 | updated_at=1787335508.3030694 | frequency_hz=374.0
- [2026-08-22 02:05:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335511.741859 | source=vosk | rms=206 | updated_at=1787335511.300113 | frequency_hz=374.0
- [2026-08-22 02:05:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335515.0145051 | source=vosk | rms=206 | updated_at=1787335511.300113 | frequency_hz=374.0
- [2026-08-22 02:05:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335516.4995036 | source=vosk | rms=206 | updated_at=1787335511.300113 | frequency_hz=374.0
- [2026-08-22 02:05:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335516.7841578 | source=vosk | rms=206 | updated_at=1787335511.300113 | frequency_hz=374.0
- [2026-08-22 02:05:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335517.4960222 | source=vosk | rms=206 | updated_at=1787335511.300113 | frequency_hz=374.0
- [2026-08-22 02:05:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335521.9929976 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335522.4979436 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335523.5329587 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335523.9919558 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335525.4923804 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335526.4937663 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335528.2416523 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335528.7462559 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335530.9933834 | source=vosk | rms=227 | updated_at=1787335521.9929976 | frequency_hz=374.0
- [2026-08-22 02:05:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335531.797164 | source=vosk | rms=206 | updated_at=1787335531.2417037 | frequency_hz=374.0
- [2026-08-22 02:05:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335531.992063 | source=vosk | rms=206 | updated_at=1787335531.2417037 | frequency_hz=374.0
- [2026-08-22 02:05:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335532.7479913 | source=vosk | rms=206 | updated_at=1787335531.2417037 | frequency_hz=374.0
- [2026-08-22 02:05:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335546.9924543 | source=vosk | rms=1203 | updated_at=1787335546.9924543 | frequency_hz=374.0
- [2026-08-22 02:05:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335548.0164597 | source=vosk | rms=1202 | updated_at=1787335547.2442813 | frequency_hz=374.0
- [2026-08-22 02:05:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335551.5420725 | source=vosk | rms=182 | updated_at=1787335551.5420725 | frequency_hz=98.0
- [2026-08-22 02:05:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335552.4987211 | source=vosk | rms=1200 | updated_at=1787335552.0271878 | frequency_hz=98.0
- [2026-08-22 02:05:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335554.2921495 | source=vosk | rms=483 | updated_at=1787335554.2921495 | frequency_hz=98.0
- [2026-08-22 02:05:56] operator / voice_transcript_final / voice: spice
  meta: kind=final | timestamp=1787335556.36352 | source=final | rms=190 | updated_at=1787335556.0263784 | frequency_hz=98.0
- [2026-08-22 02:05:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335556.4929364 | source=vosk | rms=190 | updated_at=1787335556.0263784 | frequency_hz=98.0
- [2026-08-22 02:05:58] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1787335558.1109118 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:05:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335558.4931805 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:05:58] operator / voice_transcript_partial / voice: sleep
  meta: kind=partial | timestamp=1787335558.589123 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:05:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335558.763504 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:05:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335559.4924805 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:05:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335559.743814 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:06:00] operator / voice_transcript_final / voice: and i m sleep
  meta: kind=final | timestamp=1787335560.213538 | source=final | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:06:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335560.331167 | source=vosk | rms=228 | updated_at=1787335557.4966173 | frequency_hz=98.0
- [2026-08-22 02:06:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335560.331167 | source=vosk | rms=134 | updated_at=1787335560.331167 | frequency_hz=98.0
- [2026-08-22 02:06:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335564.2484381 | source=vosk | rms=247 | updated_at=1787335561.2623427 | frequency_hz=98.0
- [2026-08-22 02:06:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335565.2428668 | source=vosk | rms=247 | updated_at=1787335561.2623427 | frequency_hz=98.0
- [2026-08-22 02:06:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335565.9944499 | source=vosk | rms=247 | updated_at=1787335561.2623427 | frequency_hz=98.0
- [2026-08-22 02:06:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335580.7696574 | source=vosk | rms=128 | updated_at=1787335580.7690923 | frequency_hz=98.0
- [2026-08-22 02:06:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335581.2961943 | source=vosk | rms=128 | updated_at=1787335580.7690923 | frequency_hz=98.0
- [2026-08-22 02:06:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335582.7984576 | source=vosk | rms=128 | updated_at=1787335580.7690923 | frequency_hz=98.0
- [2026-08-22 02:06:23] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1787335583.6309109 | source=final | rms=128 | updated_at=1787335580.7690923 | frequency_hz=98.0
- [2026-08-22 02:06:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335583.6750767 | source=vosk | rms=128 | updated_at=1787335580.7690923 | frequency_hz=98.0
- [2026-08-22 02:06:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335583.6750767 | source=vosk | rms=128 | updated_at=1787335580.7690923 | frequency_hz=98.0
- [2026-08-22 02:06:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335597.0364032 | source=vosk | rms=162 | updated_at=1787335596.2524269 | frequency_hz=98.0
- [2026-08-22 02:06:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335597.3021622 | source=vosk | rms=162 | updated_at=1787335596.2524269 | frequency_hz=98.0
- [2026-08-22 02:06:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335597.7779229 | source=vosk | rms=162 | updated_at=1787335596.2524269 | frequency_hz=98.0
- [2026-08-22 02:06:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335598.247132 | source=vosk | rms=162 | updated_at=1787335596.2524269 | frequency_hz=98.0
- [2026-08-22 02:06:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335599.778071 | source=vosk | rms=162 | updated_at=1787335596.2524269 | frequency_hz=98.0
- [2026-08-22 02:06:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335600.524412 | source=vosk | rms=162 | updated_at=1787335596.2524269 | frequency_hz=98.0
- [2026-08-22 02:06:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335604.2420106 | source=vosk | rms=1202 | updated_at=1787335603.546162 | frequency_hz=98.0
- [2026-08-22 02:06:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335604.7476773 | source=vosk | rms=203 | updated_at=1787335604.7476773 | frequency_hz=98.0
- [2026-08-22 02:06:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335605.492047 | source=vosk | rms=162 | updated_at=1787335604.9995651 | frequency_hz=98.0
- [2026-08-22 02:06:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335606.0256386 | source=vosk | rms=208 | updated_at=1787335606.0256386 | frequency_hz=98.0
- [2026-08-22 02:06:46] operator / voice_transcript_partial / voice: so
  meta: kind=partial | timestamp=1787335606.756438 | source=vosk | rms=198 | updated_at=1787335606.2644572 | frequency_hz=98.0
- [2026-08-22 02:06:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335606.9921176 | source=vosk | rms=198 | updated_at=1787335606.2644572 | frequency_hz=98.0
- [2026-08-22 02:06:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335607.24279 | source=vosk | rms=198 | updated_at=1787335606.2644572 | frequency_hz=98.0
- [2026-08-22 02:06:47] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1787335607.5088332 | source=final | rms=198 | updated_at=1787335606.2644572 | frequency_hz=98.0
- [2026-08-22 02:06:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335607.7589438 | source=vosk | rms=198 | updated_at=1787335606.2644572 | frequency_hz=98.0
- [2026-08-22 02:06:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335609.015931 | source=vosk | rms=240 | updated_at=1787335609.015931 | frequency_hz=98.0
- [2026-08-22 02:06:49] operator / voice_transcript_partial / voice: so
  meta: kind=partial | timestamp=1787335609.7678103 | source=vosk | rms=240 | updated_at=1787335609.015931 | frequency_hz=98.0
- [2026-08-22 02:06:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335610.2778432 | source=vosk | rms=240 | updated_at=1787335609.015931 | frequency_hz=98.0
- [2026-08-22 02:06:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335610.492835 | source=vosk | rms=240 | updated_at=1787335609.015931 | frequency_hz=98.0
- [2026-08-22 02:06:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335611.0248454 | source=vosk | rms=1201 | updated_at=1787335611.0248454 | frequency_hz=98.0
- [2026-08-22 02:06:51] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1787335611.2398517 | source=final | rms=1201 | updated_at=1787335611.0248454 | frequency_hz=98.0
- [2026-08-22 02:06:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335611.2749276 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335611.7428136 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335614.2479646 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335614.7810583 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335615.542286 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:56] operator / voice_transcript_partial / voice: to be
  meta: kind=partial | timestamp=1787335616.3435018 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335616.535869 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335617.0171456 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335619.5359063 | source=vosk | rms=553 | updated_at=1787335611.2749276 | frequency_hz=98.0
- [2026-08-22 02:06:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335619.7879221 | source=vosk | rms=179 | updated_at=1787335619.7879221 | frequency_hz=98.0
- [2026-08-22 02:06:59] operator / voice_transcript_final / voice: to me
  meta: kind=final | timestamp=1787335619.9990041 | source=final | rms=179 | updated_at=1787335619.7879221 | frequency_hz=98.0
- [2026-08-22 02:07:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335620.2439573 | source=vosk | rms=179 | updated_at=1787335619.7879221 | frequency_hz=98.0
- [2026-08-22 02:07:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335620.7859466 | source=vosk | rms=179 | updated_at=1787335619.7879221 | frequency_hz=98.0
- [2026-08-22 02:07:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335623.4921162 | source=vosk | rms=280 | updated_at=1787335623.4921162 | frequency_hz=98.0
- [2026-08-22 02:07:04] operator / voice_transcript_partial / voice: he took
  meta: kind=partial | timestamp=1787335624.772124 | source=vosk | rms=179 | updated_at=1787335624.751032 | frequency_hz=98.0
- [2026-08-22 02:07:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335625.2583568 | source=vosk | rms=196 | updated_at=1787335625.2583568 | frequency_hz=98.0
- [2026-08-22 02:07:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335625.5081944 | source=vosk | rms=196 | updated_at=1787335625.2583568 | frequency_hz=98.0
- [2026-08-22 02:07:05] operator / voice_transcript_partial / voice: he took really a
  meta: kind=partial | timestamp=1787335625.5545254 | source=vosk | rms=196 | updated_at=1787335625.2583568 | frequency_hz=98.0
- [2026-08-22 02:07:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335625.9924595 | source=vosk | rms=196 | updated_at=1787335625.2583568 | frequency_hz=98.0
- [2026-08-22 02:07:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335627.9968896 | source=vosk | rms=196 | updated_at=1787335625.2583568 | frequency_hz=98.0
- [2026-08-22 02:07:08] operator / voice_transcript_partial / voice: he took really
  meta: kind=partial | timestamp=1787335628.049351 | source=vosk | rms=196 | updated_at=1787335625.2583568 | frequency_hz=98.0
- [2026-08-22 02:07:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335628.2649333 | source=vosk | rms=1202 | updated_at=1787335628.2649333 | frequency_hz=98.0
- [2026-08-22 02:07:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335628.5291753 | source=vosk | rms=1201 | updated_at=1787335628.5291753 | frequency_hz=98.0
- [2026-08-22 02:07:09] operator / voice_transcript_final / voice: he took really
  meta: kind=final | timestamp=1787335629.5679913 | source=final | rms=1201 | updated_at=1787335628.5291753 | frequency_hz=98.0
- [2026-08-22 02:07:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335629.7486165 | source=vosk | rms=1201 | updated_at=1787335628.5291753 | frequency_hz=98.0
- [2026-08-22 02:07:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335629.7486165 | source=vosk | rms=1204 | updated_at=1787335629.7486165 | frequency_hz=98.0
- [2026-08-22 02:07:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335630.272097 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335632.0250037 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335632.5347292 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335635.4936483 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335636.2548892 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335638.0005722 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335638.5050588 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335640.3189793 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335641.0246649 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335642.5110557 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335642.9939852 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335656.2430716 | source=vosk | rms=416 | updated_at=1787335629.7611327 | frequency_hz=98.0
- [2026-08-22 02:07:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335658.2471862 | source=vosk | rms=365 | updated_at=1787335657.765854 | frequency_hz=98.0
- [2026-08-22 02:07:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335659.4982383 | source=vosk | rms=345 | updated_at=1787335659.4982383 | frequency_hz=98.0
- [2026-08-22 02:07:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335660.746209 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335664.5168772 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335665.022006 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335677.7491329 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:58] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1787335678.0320404 | source=final | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335678.2469704 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335678.2469704 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:07:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335678.7568746 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:08:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335683.2623625 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:08:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335684.0126212 | source=vosk | rms=233 | updated_at=1787335659.993992 | frequency_hz=98.0
- [2026-08-22 02:08:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335688.2727349 | source=vosk | rms=167 | updated_at=1787335688.2727349 | frequency_hz=98.0
- [2026-08-22 02:08:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335689.2957299 | source=vosk | rms=1203 | updated_at=1787335688.7514172 | frequency_hz=98.0
- [2026-08-22 02:08:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335689.5397778 | source=vosk | rms=125 | updated_at=1787335689.5397778 | frequency_hz=98.0
- [2026-08-22 02:08:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335690.9925203 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335692.7475405 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335693.4931545 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335695.0075114 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335695.746197 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335697.758987 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335699.0317812 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335700.5287168 | source=vosk | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:21] operator / voice_transcript_final / voice: two
  meta: kind=final | timestamp=1787335701.305778 | source=final | rms=1201 | updated_at=1787335690.495629 | frequency_hz=98.0
- [2026-08-22 02:08:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335701.3452358 | source=vosk | rms=128 | updated_at=1787335701.3452358 | frequency_hz=98.0
- [2026-08-22 02:08:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335702.291835 | source=vosk | rms=309 | updated_at=1787335701.4937186 | frequency_hz=98.0
- [2026-08-22 02:08:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335702.4988108 | source=vosk | rms=256 | updated_at=1787335702.4988108 | frequency_hz=98.0
- [2026-08-22 02:08:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335703.6874893 | source=vosk | rms=440 | updated_at=1787335703.191373 | frequency_hz=98.0
- [2026-08-22 02:08:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335707.1925323 | source=vosk | rms=1203 | updated_at=1787335707.1925323 | frequency_hz=98.0
- [2026-08-22 02:08:27] operator / voice_transcript_partial / voice: do it
  meta: kind=partial | timestamp=1787335707.2914479 | source=vosk | rms=1203 | updated_at=1787335707.1925323 | frequency_hz=98.0
- [2026-08-22 02:08:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335707.4761412 | source=vosk | rms=1202 | updated_at=1787335707.4761412 | frequency_hz=98.0
- [2026-08-22 02:08:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335707.9328787 | source=vosk | rms=1202 | updated_at=1787335707.4761412 | frequency_hz=98.0
- [2026-08-22 02:08:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335713.6835682 | source=vosk | rms=145 | updated_at=1787335713.6835682 | frequency_hz=98.0
- [2026-08-22 02:08:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335714.1881306 | source=vosk | rms=145 | updated_at=1787335713.6835682 | frequency_hz=98.0
- [2026-08-22 02:08:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335716.7380195 | source=vosk | rms=145 | updated_at=1787335713.6835682 | frequency_hz=98.0
- [2026-08-22 02:08:37] operator / voice_transcript_final / voice: do it
  meta: kind=final | timestamp=1787335717.1448164 | source=final | rms=145 | updated_at=1787335713.6835682 | frequency_hz=98.0
- [2026-08-22 02:08:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335717.4019692 | source=vosk | rms=145 | updated_at=1787335713.6835682 | frequency_hz=98.0
- [2026-08-22 02:08:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335717.4019692 | source=vosk | rms=145 | updated_at=1787335713.6835682 | frequency_hz=98.0
- [2026-08-22 02:08:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335719.1835675 | source=vosk | rms=160 | updated_at=1787335718.184364 | frequency_hz=98.0
- [2026-08-22 02:08:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335720.9573178 | source=vosk | rms=160 | updated_at=1787335718.184364 | frequency_hz=98.0
- [2026-08-22 02:08:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335721.4330113 | source=vosk | rms=160 | updated_at=1787335718.184364 | frequency_hz=98.0
- [2026-08-22 02:08:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335721.684247 | source=vosk | rms=160 | updated_at=1787335718.184364 | frequency_hz=98.0
- [2026-08-22 02:08:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335722.6829681 | source=vosk | rms=160 | updated_at=1787335718.184364 | frequency_hz=98.0
- [2026-08-22 02:08:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335722.9417312 | source=vosk | rms=128 | updated_at=1787335722.9417312 | frequency_hz=98.0
- [2026-08-22 02:08:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335723.4336898 | source=vosk | rms=128 | updated_at=1787335722.9417312 | frequency_hz=98.0
- [2026-08-22 02:08:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335724.9336581 | source=vosk | rms=249 | updated_at=1787335724.9336581 | frequency_hz=98.0
- [2026-08-22 02:08:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335725.6836393 | source=vosk | rms=249 | updated_at=1787335724.9336581 | frequency_hz=98.0
- [2026-08-22 02:08:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335726.954554 | source=vosk | rms=249 | updated_at=1787335724.9336581 | frequency_hz=98.0
- [2026-08-22 02:08:47] operator / voice_transcript_partial / voice: people
  meta: kind=partial | timestamp=1787335727.7632542 | source=vosk | rms=302 | updated_at=1787335727.4435117 | frequency_hz=98.0
- [2026-08-22 02:08:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335727.9632006 | source=vosk | rms=232 | updated_at=1787335727.9632006 | frequency_hz=98.0
- [2026-08-22 02:08:48] operator / voice_transcript_partial / voice: people since
  meta: kind=partial | timestamp=1787335728.0118656 | source=vosk | rms=232 | updated_at=1787335727.9632006 | frequency_hz=98.0
- [2026-08-22 02:08:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335728.4485376 | source=vosk | rms=154 | updated_at=1787335728.4485376 | frequency_hz=98.0
- [2026-08-22 02:08:48] operator / voice_transcript_partial / voice: people seem to
  meta: kind=partial | timestamp=1787335728.5185099 | source=vosk | rms=154 | updated_at=1787335728.4485376 | frequency_hz=98.0
- [2026-08-22 02:08:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335729.185451 | source=vosk | rms=154 | updated_at=1787335728.4485376 | frequency_hz=98.0
- [2026-08-22 02:08:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335729.9329598 | source=vosk | rms=125 | updated_at=1787335729.9329598 | frequency_hz=98.0
- [2026-08-22 02:08:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335730.4368703 | source=vosk | rms=125 | updated_at=1787335729.9329598 | frequency_hz=98.0
- [2026-08-22 02:08:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335730.6864758 | source=vosk | rms=194 | updated_at=1787335730.6864758 | frequency_hz=98.0
- [2026-08-22 02:08:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335730.9346101 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335731.2366157 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335731.4567723 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:51] operator / voice_transcript_partial / voice: people seem to just go
  meta: kind=partial | timestamp=1787335731.5281398 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335732.2057161 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335734.4333148 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:54] operator / voice_transcript_partial / voice: people seem to change group of
  meta: kind=partial | timestamp=1787335734.47844 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335734.6832387 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:54] operator / voice_transcript_partial / voice: people seem to just go
  meta: kind=partial | timestamp=1787335734.7721047 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335734.9855046 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:55] operator / voice_transcript_partial / voice: people seem to june school
  meta: kind=partial | timestamp=1787335735.033417 | source=vosk | rms=148 | updated_at=1787335730.9346101 | frequency_hz=98.0
- [2026-08-22 02:08:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335735.1994727 | source=vosk | rms=250 | updated_at=1787335735.1994727 | frequency_hz=98.0
- [2026-08-22 02:08:55] operator / voice_transcript_final / voice: people seem to june school teacher
  meta: kind=final | timestamp=1787335735.783141 | source=final | rms=250 | updated_at=1787335735.1994727 | frequency_hz=98.0
- [2026-08-22 02:08:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335735.9816437 | source=vosk | rms=250 | updated_at=1787335735.1994727 | frequency_hz=98.0
- [2026-08-22 02:08:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335735.983147 | source=vosk | rms=811 | updated_at=1787335735.983147 | frequency_hz=98.0
- [2026-08-22 02:08:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335736.4407606 | source=vosk | rms=811 | updated_at=1787335735.983147 | frequency_hz=98.0
- [2026-08-22 02:08:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335737.1914654 | source=vosk | rms=166 | updated_at=1787335737.1914654 | frequency_hz=98.0
- [2026-08-22 02:08:57] operator / voice_transcript_partial / voice: good smile
  meta: kind=partial | timestamp=1787335737.8033235 | source=vosk | rms=173 | updated_at=1787335737.7214925 | frequency_hz=98.0
- [2026-08-22 02:08:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335738.4336653 | source=vosk | rms=173 | updated_at=1787335737.7214925 | frequency_hz=98.0
- [2026-08-22 02:08:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335739.6848514 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:08:59] operator / voice_transcript_partial / voice: slowly
  meta: kind=partial | timestamp=1787335739.7113187 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335740.2056901 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335740.9834352 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335741.4389358 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335744.4376583 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:04] operator / voice_transcript_final / voice: slowly
  meta: kind=final | timestamp=1787335744.837984 | source=final | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335744.8870783 | source=vosk | rms=347 | updated_at=1787335739.6848514 | frequency_hz=98.0
- [2026-08-22 02:09:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335744.8870783 | source=vosk | rms=336 | updated_at=1787335744.8870783 | frequency_hz=98.0
- [2026-08-22 02:09:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335745.686613 | source=vosk | rms=156 | updated_at=1787335745.2173312 | frequency_hz=98.0
- [2026-08-22 02:09:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335745.9404507 | source=vosk | rms=156 | updated_at=1787335745.2173312 | frequency_hz=98.0
- [2026-08-22 02:09:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335747.6836462 | source=vosk | rms=146 | updated_at=1787335746.9470131 | frequency_hz=98.0
- [2026-08-22 02:09:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335748.9468167 | source=vosk | rms=206 | updated_at=1787335748.9468167 | frequency_hz=98.0
- [2026-08-22 02:09:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335749.7140675 | source=vosk | rms=128 | updated_at=1787335749.2079744 | frequency_hz=98.0
- [2026-08-22 02:09:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335751.433685 | source=vosk | rms=284 | updated_at=1787335751.433685 | frequency_hz=98.0
- [2026-08-22 02:09:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335752.1846213 | source=vosk | rms=400 | updated_at=1787335751.6885643 | frequency_hz=98.0
- [2026-08-22 02:09:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335752.7220836 | source=vosk | rms=400 | updated_at=1787335751.6885643 | frequency_hz=98.0
- [2026-08-22 02:09:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335753.2193248 | source=vosk | rms=400 | updated_at=1787335751.6885643 | frequency_hz=98.0
- [2026-08-22 02:09:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335754.198077 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:14] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787335754.2219894 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335754.7182553 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335755.2150126 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335756.1837015 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335756.734983 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:17] operator / voice_transcript_final / voice: it s safe
  meta: kind=final | timestamp=1787335757.654281 | source=final | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335757.8045547 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335761.2246306 | source=vosk | rms=306 | updated_at=1787335754.198077 | frequency_hz=98.0
- [2026-08-22 02:09:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335761.9513903 | source=vosk | rms=144 | updated_at=1787335761.4651244 | frequency_hz=98.0
- [2026-08-22 02:09:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335763.94063 | source=vosk | rms=144 | updated_at=1787335761.4651244 | frequency_hz=98.0
- [2026-08-22 02:09:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335764.4982057 | source=vosk | rms=144 | updated_at=1787335761.4651244 | frequency_hz=98.0
- [2026-08-22 02:09:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335764.6868482 | source=vosk | rms=330 | updated_at=1787335764.6868482 | frequency_hz=98.0
- [2026-08-22 02:09:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335765.239182 | source=vosk | rms=330 | updated_at=1787335764.6868482 | frequency_hz=98.0
- [2026-08-22 02:09:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335766.1896822 | source=vosk | rms=330 | updated_at=1787335764.6868482 | frequency_hz=98.0
- [2026-08-22 02:09:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335766.7124228 | source=vosk | rms=330 | updated_at=1787335764.6868482 | frequency_hz=98.0
- [2026-08-22 02:09:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335767.4623058 | source=vosk | rms=330 | updated_at=1787335764.6868482 | frequency_hz=98.0
- [2026-08-22 02:09:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335767.9473705 | source=vosk | rms=330 | updated_at=1787335764.6868482 | frequency_hz=98.0
- [2026-08-22 02:09:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335768.7710009 | source=vosk | rms=137 | updated_at=1787335768.769999 | frequency_hz=98.0
- [2026-08-22 02:09:28] operator / voice_transcript_partial / voice: that's
  meta: kind=partial | timestamp=1787335768.8178542 | source=vosk | rms=137 | updated_at=1787335768.769999 | frequency_hz=98.0
- [2026-08-22 02:09:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335769.1916387 | source=vosk | rms=137 | updated_at=1787335768.769999 | frequency_hz=98.0
- [2026-08-22 02:09:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335769.442527 | source=vosk | rms=139 | updated_at=1787335769.442527 | frequency_hz=98.0
- [2026-08-22 02:09:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335769.9337528 | source=vosk | rms=144 | updated_at=1787335769.9337528 | frequency_hz=98.0
- [2026-08-22 02:09:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335770.1838012 | source=vosk | rms=144 | updated_at=1787335769.9337528 | frequency_hz=98.0
- [2026-08-22 02:09:30] operator / voice_transcript_final / voice: happy
  meta: kind=final | timestamp=1787335770.4122632 | source=final | rms=144 | updated_at=1787335769.9337528 | frequency_hz=98.0
- [2026-08-22 02:09:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335770.6189015 | source=vosk | rms=144 | updated_at=1787335769.9337528 | frequency_hz=98.0
- [2026-08-22 02:09:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335770.6189015 | source=vosk | rms=260 | updated_at=1787335770.6189015 | frequency_hz=98.0
- [2026-08-22 02:09:30] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787335770.7002895 | source=vosk | rms=260 | updated_at=1787335770.6189015 | frequency_hz=98.0
- [2026-08-22 02:09:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335770.9790885 | source=vosk | rms=164 | updated_at=1787335770.9790885 | frequency_hz=98.0
- [2026-08-22 02:09:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335771.2266002 | source=vosk | rms=164 | updated_at=1787335770.9790885 | frequency_hz=98.0
- [2026-08-22 02:09:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335771.6999428 | source=vosk | rms=164 | updated_at=1787335770.9790885 | frequency_hz=98.0
- [2026-08-22 02:09:31] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1787335771.9679527 | source=final | rms=164 | updated_at=1787335770.9790885 | frequency_hz=98.0
- [2026-08-22 02:09:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335772.0089788 | source=vosk | rms=269 | updated_at=1787335772.0089788 | frequency_hz=98.0
- [2026-08-22 02:09:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335774.4422882 | source=vosk | rms=247 | updated_at=1787335773.9341538 | frequency_hz=98.0
- [2026-08-22 02:09:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335776.6938415 | source=vosk | rms=247 | updated_at=1787335773.9341538 | frequency_hz=98.0
- [2026-08-22 02:09:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335779.4426665 | source=vosk | rms=261 | updated_at=1787335779.0148325 | frequency_hz=98.0
- [2026-08-22 02:09:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335781.2250688 | source=vosk | rms=261 | updated_at=1787335779.0148325 | frequency_hz=98.0
- [2026-08-22 02:09:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335781.6961155 | source=vosk | rms=261 | updated_at=1787335779.0148325 | frequency_hz=98.0
- [2026-08-22 02:09:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335784.5088673 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335784.943916 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335785.201543 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:45] operator / voice_transcript_partial / voice: that's
  meta: kind=partial | timestamp=1787335785.2272558 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335785.7208297 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335787.9628823 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335788.4442694 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335788.6941514 | source=vosk | rms=735 | updated_at=1787335784.5088673 | frequency_hz=98.0
- [2026-08-22 02:09:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787335788.9470766 | source=vosk | rms=172 | updated_at=1787335788.9470766 | frequency_hz=98.0
- [2026-08-22 02:09:49] operator / voice_transcript_final / voice: that s
  meta: kind=final | timestamp=1787335789.2027833 | source=final | rms=172 | updated_at=1787335788.9470766 | frequency_hz=98.0
- [2026-08-22 02:09:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787335789.4492338 | source=vosk | rms=172 | updated_at=1787335788.9470766 | frequency_hz=98.0

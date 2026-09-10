# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-18 23:06:21
- Entries: 975
- Roles: {'assistant': 11, 'system': 797, 'operator': 167}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 797, 'spoken_confirmation': 9, 'voice_transcript_partial': 133, 'voice_transcript_final': 26, 'voice_command': 8}
- Channels: {'text': 2, 'voice': 973}
- Latest operator request: close the app
- Latest assistant message: Engagement speed is already 100 percent.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-18 22:47:40] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-18 22:47:40] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-18 22:47:43] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787064463.2629635 | source=vosk
- [2026-08-18 22:47:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064463.5729303 | source=vosk
- [2026-08-18 22:47:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064464.07983 | source=vosk
- [2026-08-18 22:47:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064465.770942 | source=vosk
- [2026-08-18 22:47:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064466.5216212 | source=vosk
- [2026-08-18 22:47:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064470.583573 | source=vosk
- [2026-08-18 22:48:17] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-18 22:47:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064477.6313956 | source=vosk
- [2026-08-18 22:47:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064477.8818738 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:47:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064478.3813899 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:47:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064479.6319592 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064481.3818214 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064481.6310773 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064482.631833 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064486.381334 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064486.8811758 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064487.631581 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064488.1317036 | source=vosk | rms=453 | updated_at=1787064477.8818738
- [2026-08-18 22:48:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064489.6315591 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064490.1315284 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064490.882585 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064491.3816543 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064492.3819396 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064494.1320803 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064495.3814135 | source=vosk | rms=231 | updated_at=1787064489.6315591
- [2026-08-18 22:48:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064496.1317403 | source=vosk | rms=136 | updated_at=1787064495.631841
- [2026-08-18 22:48:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064498.6315649 | source=vosk | rms=136 | updated_at=1787064495.631841
- [2026-08-18 22:48:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064499.3821013 | source=vosk | rms=136 | updated_at=1787064495.631841
- [2026-08-18 22:48:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064499.8816006 | source=vosk | rms=552 | updated_at=1787064499.8816006
- [2026-08-18 22:48:20] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787064500.6917877 | source=vosk | rms=565 | updated_at=1787064500.6327698
- [2026-08-18 22:48:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064500.8828027 | source=vosk | rms=926 | updated_at=1787064500.8828027
- [2026-08-18 22:48:20] operator / voice_transcript_partial / voice: smart century
  meta: kind=partial | timestamp=1787064500.9636862 | source=vosk | rms=926 | updated_at=1787064500.8828027
- [2026-08-18 22:48:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064501.1537235 | source=vosk | rms=378 | updated_at=1787064501.1537235
- [2026-08-18 22:48:21] operator / voice_transcript_partial / voice: smart century as
  meta: kind=partial | timestamp=1787064501.2242768 | source=vosk | rms=378 | updated_at=1787064501.1537235
- [2026-08-18 22:48:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064501.88123 | source=vosk | rms=378 | updated_at=1787064501.1537235
- [2026-08-18 22:48:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064503.632096 | source=vosk | rms=147 | updated_at=1787064503.632096
- [2026-08-18 22:48:23] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1787064503.6792595 | source=vosk | rms=147 | updated_at=1787064503.632096
- [2026-08-18 22:48:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064503.9381716 | source=vosk | rms=643 | updated_at=1787064503.9381716
- [2026-08-18 22:48:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064504.1578765 | source=vosk | rms=302 | updated_at=1787064504.1578765
- [2026-08-18 22:48:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064504.6330123 | source=vosk | rms=302 | updated_at=1787064504.1578765
- [2026-08-18 22:48:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064505.1322594 | source=vosk | rms=578 | updated_at=1787064505.1322594
- [2026-08-18 22:48:25] operator / voice_transcript_partial / voice: smart century is ready billion
  meta: kind=partial | timestamp=1787064505.1795235 | source=vosk | rms=578 | updated_at=1787064505.1322594
- [2026-08-18 22:48:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064505.381932 | source=vosk | rms=708 | updated_at=1787064505.381932
- [2026-08-18 22:48:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064505.6341693 | source=vosk | rms=568 | updated_at=1787064505.6341693
- [2026-08-18 22:48:25] operator / voice_transcript_partial / voice: smart century is ready billion run this
  meta: kind=partial | timestamp=1787064505.7018254 | source=vosk | rms=568 | updated_at=1787064505.6341693
- [2026-08-18 22:48:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064505.8844411 | source=vosk | rms=271 | updated_at=1787064505.8844411
- [2026-08-18 22:48:25] operator / voice_transcript_partial / voice: smart century is ready billion run the
  meta: kind=partial | timestamp=1787064505.9059303 | source=vosk | rms=271 | updated_at=1787064505.8844411
- [2026-08-18 22:48:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064506.1339862 | source=vosk | rms=224 | updated_at=1787064506.1339862
- [2026-08-18 22:48:26] operator / voice_transcript_partial / voice: smart century is ready billion run the smarts and
  meta: kind=partial | timestamp=1787064506.1496 | source=vosk | rms=224 | updated_at=1787064506.1339862
- [2026-08-18 22:48:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064506.631826 | source=vosk | rms=224 | updated_at=1787064506.1339862
- [2026-08-18 22:48:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064511.881725 | source=vosk | rms=445 | updated_at=1787064511.881725
- [2026-08-18 22:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064512.136576 | source=vosk | rms=853 | updated_at=1787064512.136576
- [2026-08-18 22:48:32] operator / voice_transcript_partial / voice: smart century is ready billion run the smart sentry
  meta: kind=partial | timestamp=1787064512.1617486 | source=vosk | rms=853 | updated_at=1787064512.136576
- [2026-08-18 22:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064512.3813958 | source=vosk | rms=491 | updated_at=1787064512.3813958
- [2026-08-18 22:48:32] operator / voice_transcript_partial / voice: smart century is ready billion run the smart sentry run
  meta: kind=partial | timestamp=1787064512.4223242 | source=vosk | rms=491 | updated_at=1787064512.3813958
- [2026-08-18 22:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064512.6434941 | source=vosk | rms=680 | updated_at=1787064512.6434941
- [2026-08-18 22:48:32] operator / voice_transcript_partial / voice: smart century is ready billion run the smart sentry run the
  meta: kind=partial | timestamp=1787064512.6805463 | source=vosk | rms=680 | updated_at=1787064512.6434941
- [2026-08-18 22:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064512.8831565 | source=vosk | rms=350 | updated_at=1787064512.8831565
- [2026-08-18 22:48:32] operator / voice_transcript_partial / voice: smart century is ready billion run the smart sentry run the smarts and
  meta: kind=partial | timestamp=1787064512.9027708 | source=vosk | rms=350 | updated_at=1787064512.8831565
- [2026-08-18 22:48:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064513.3821173 | source=vosk | rms=350 | updated_at=1787064512.8831565
- [2026-08-18 22:48:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064518.3814175 | source=vosk | rms=266 | updated_at=1787064518.3814175
- [2026-08-18 22:48:38] operator / voice_transcript_partial / voice: smart century is ready billion run the smart sentry run the smarts and three
  meta: kind=partial | timestamp=1787064518.4113612 | source=vosk | rms=266 | updated_at=1787064518.3814175
- [2026-08-18 22:48:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064518.6314292 | source=vosk | rms=281 | updated_at=1787064518.6314292
- [2026-08-18 22:48:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064519.164946 | source=vosk | rms=281 | updated_at=1787064518.6314292
- [2026-08-18 22:48:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064523.1902006 | source=vosk | rms=162 | updated_at=1787064523.1902006
- [2026-08-18 22:48:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064523.3828635 | source=vosk | rms=162 | updated_at=1787064523.1902006
- [2026-08-18 22:48:43] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787064523.4020813 | source=final | rms=162 | updated_at=1787064523.1902006
- [2026-08-18 22:48:43] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064523.446872 | source=state | rms=162 | updated_at=1787064523.1902006
- [2026-08-18 22:48:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064523.446872 | source=state | rms=162 | updated_at=1787064523.1902006
- [2026-08-18 22:48:43] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-18 22:48:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064523.632246 | source=vosk | rms=162 | updated_at=1787064523.1902006
- [2026-08-18 22:48:43] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:48:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064524.3872573 | source=vosk | rms=1201 | updated_at=1787064523.8817863
- [2026-08-18 22:48:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064525.63137 | source=vosk | rms=854 | updated_at=1787064525.63137
- [2026-08-18 22:48:46] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1787064526.1840203 | source=vosk | rms=989 | updated_at=1787064526.1659856
- [2026-08-18 22:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064526.3820682 | source=vosk | rms=447 | updated_at=1787064526.3820682
- [2026-08-18 22:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064526.674902 | source=vosk | rms=453 | updated_at=1787064526.674902
- [2026-08-18 22:48:46] operator / voice_transcript_partial / voice: running smart
  meta: kind=partial | timestamp=1787064526.702136 | source=vosk | rms=453 | updated_at=1787064526.674902
- [2026-08-18 22:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064526.881971 | source=vosk | rms=330 | updated_at=1787064526.881971
- [2026-08-18 22:48:46] operator / voice_transcript_partial / voice: running smart century
  meta: kind=partial | timestamp=1787064526.8950684 | source=vosk | rms=330 | updated_at=1787064526.881971
- [2026-08-18 22:48:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064527.3843172 | source=vosk | rms=485 | updated_at=1787064527.3843172
- [2026-08-18 22:48:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064527.6752124 | source=vosk | rms=1120 | updated_at=1787064527.6752124
- [2026-08-18 22:48:47] operator / voice_transcript_partial / voice: running smart century now
  meta: kind=partial | timestamp=1787064527.7030635 | source=vosk | rms=1120 | updated_at=1787064527.6752124
- [2026-08-18 22:48:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064527.8856604 | source=vosk | rms=1063 | updated_at=1787064527.8856604
- [2026-08-18 22:48:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064528.1316292 | source=vosk | rms=1095 | updated_at=1787064528.1316292
- [2026-08-18 22:48:48] operator / voice_transcript_partial / voice: running smart century now connecting
  meta: kind=partial | timestamp=1787064528.1544898 | source=vosk | rms=1095 | updated_at=1787064528.1316292
- [2026-08-18 22:48:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064528.3830788 | source=vosk | rms=591 | updated_at=1787064528.3830788
- [2026-08-18 22:48:48] operator / voice_transcript_partial / voice: running smart century now connecting the
  meta: kind=partial | timestamp=1787064528.4108956 | source=vosk | rms=591 | updated_at=1787064528.3830788
- [2026-08-18 22:48:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064528.631507 | source=vosk | rms=395 | updated_at=1787064528.631507
- [2026-08-18 22:48:48] operator / voice_transcript_partial / voice: running smart century now connecting the smart
  meta: kind=partial | timestamp=1787064528.650049 | source=vosk | rms=395 | updated_at=1787064528.631507
- [2026-08-18 22:48:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064528.8816254 | source=vosk | rms=845 | updated_at=1787064528.8816254
- [2026-08-18 22:48:48] operator / voice_transcript_partial / voice: running smart century now connecting the smart century
  meta: kind=partial | timestamp=1787064528.9042094 | source=vosk | rms=845 | updated_at=1787064528.8816254
- [2026-08-18 22:48:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064529.1783335 | source=vosk | rms=674 | updated_at=1787064529.1783335
- [2026-08-18 22:48:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064529.3833442 | source=vosk | rms=696 | updated_at=1787064529.3833442
- [2026-08-18 22:48:49] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards for
  meta: kind=partial | timestamp=1787064529.4088547 | source=vosk | rms=696 | updated_at=1787064529.3833442
- [2026-08-18 22:48:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064529.8843083 | source=vosk | rms=696 | updated_at=1787064529.3833442
- [2026-08-18 22:48:51] operator / voice_transcript_final / voice: running smart sentry now connecting the smart sentry boards for
  meta: kind=final | timestamp=1787064531.165062 | source=final | rms=696 | updated_at=1787064529.3833442
- [2026-08-18 22:48:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064532.4049435 | source=vosk | rms=246 | updated_at=1787064532.4049435
- [2026-08-18 22:48:52] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first
  meta: kind=partial | timestamp=1787064532.4759629 | source=vosk | rms=246 | updated_at=1787064532.4049435
- [2026-08-18 22:48:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064532.641688 | source=vosk | rms=1201 | updated_at=1787064532.641688
- [2026-08-18 22:48:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064532.8818698 | source=vosk | rms=961 | updated_at=1787064532.8818698
- [2026-08-18 22:48:52] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smartphone
  meta: kind=partial | timestamp=1787064532.9018989 | source=vosk | rms=961 | updated_at=1787064532.8818698
- [2026-08-18 22:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064533.3855724 | source=vosk | rms=650 | updated_at=1787064533.3855724
- [2026-08-18 22:48:53] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart
  meta: kind=partial | timestamp=1787064533.419874 | source=vosk | rms=650 | updated_at=1787064533.3855724
- [2026-08-18 22:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064533.7007353 | source=vosk | rms=885 | updated_at=1787064533.7007353
- [2026-08-18 22:48:53] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart centripetal
  meta: kind=partial | timestamp=1787064533.713865 | source=vosk | rms=885 | updated_at=1787064533.7007353
- [2026-08-18 22:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064533.8836281 | source=vosk | rms=567 | updated_at=1787064533.8836281
- [2026-08-18 22:48:53] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are
  meta: kind=partial | timestamp=1787064533.9732606 | source=vosk | rms=567 | updated_at=1787064533.8836281
- [2026-08-18 22:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064534.131416 | source=vosk | rms=624 | updated_at=1787064534.131416
- [2026-08-18 22:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064534.3819213 | source=vosk | rms=414 | updated_at=1787064534.3819213
- [2026-08-18 22:48:54] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected
  meta: kind=partial | timestamp=1787064534.3919547 | source=vosk | rms=414 | updated_at=1787064534.3819213
- [2026-08-18 22:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064534.635016 | source=vosk | rms=1205 | updated_at=1787064534.635016
- [2026-08-18 22:48:54] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on
  meta: kind=partial | timestamp=1787064534.6940067 | source=vosk | rms=1205 | updated_at=1787064534.635016
- [2026-08-18 22:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064534.8819437 | source=vosk | rms=739 | updated_at=1787064534.8819437
- [2026-08-18 22:48:54] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the
  meta: kind=partial | timestamp=1787064534.904428 | source=vosk | rms=739 | updated_at=1787064534.8819437
- [2026-08-18 22:48:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064535.1740522 | source=vosk | rms=561 | updated_at=1787064535.1740522
- [2026-08-18 22:48:55] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o
  meta: kind=partial | timestamp=1787064535.2063644 | source=vosk | rms=561 | updated_at=1787064535.1740522
- [2026-08-18 22:48:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064535.382911 | source=vosk | rms=204 | updated_at=1787064535.382911
- [2026-08-18 22:48:55] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m
  meta: kind=partial | timestamp=1787064535.3934982 | source=vosk | rms=204 | updated_at=1787064535.382911
- [2026-08-18 22:48:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064535.6322496 | source=vosk | rms=159 | updated_at=1787064535.6322496
- [2026-08-18 22:48:55] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m lange
  meta: kind=partial | timestamp=1787064535.6608596 | source=vosk | rms=159 | updated_at=1787064535.6322496
- [2026-08-18 22:48:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064535.8815942 | source=vosk | rms=361 | updated_at=1787064535.8815942
- [2026-08-18 22:48:55] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m
  meta: kind=partial | timestamp=1787064535.9049785 | source=vosk | rms=361 | updated_at=1787064535.8815942
- [2026-08-18 22:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064536.131826 | source=vosk | rms=1204 | updated_at=1787064536.131826
- [2026-08-18 22:48:56] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and
  meta: kind=partial | timestamp=1787064536.156717 | source=vosk | rms=1204 | updated_at=1787064536.131826
- [2026-08-18 22:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064536.3872151 | source=vosk | rms=780 | updated_at=1787064536.3872151
- [2026-08-18 22:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064536.6323302 | source=vosk | rms=547 | updated_at=1787064536.6323302
- [2026-08-18 22:48:56] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart
  meta: kind=partial | timestamp=1787064536.6484523 | source=vosk | rms=547 | updated_at=1787064536.6323302
- [2026-08-18 22:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064536.8835523 | source=vosk | rms=512 | updated_at=1787064536.8835523
- [2026-08-18 22:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064537.131983 | source=vosk | rms=308 | updated_at=1787064537.131983
- [2026-08-18 22:48:57] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century
  meta: kind=partial | timestamp=1787064537.1404898 | source=vosk | rms=308 | updated_at=1787064537.131983
- [2026-08-18 22:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064537.3820019 | source=vosk | rms=253 | updated_at=1787064537.3820019
- [2026-08-18 22:48:57] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is an
  meta: kind=partial | timestamp=1787064537.415185 | source=vosk | rms=253 | updated_at=1787064537.3820019
- [2026-08-18 22:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064537.8822904 | source=vosk | rms=624 | updated_at=1787064537.8822904
- [2026-08-18 22:48:57] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is
  meta: kind=partial | timestamp=1787064537.9081957 | source=vosk | rms=624 | updated_at=1787064537.8822904
- [2026-08-18 22:48:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064538.1359427 | source=vosk | rms=1203 | updated_at=1787064538.1359427
- [2026-08-18 22:48:58] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to
  meta: kind=partial | timestamp=1787064538.1598804 | source=vosk | rms=1203 | updated_at=1787064538.1359427
- [2026-08-18 22:48:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064538.3816967 | source=vosk | rms=959 | updated_at=1787064538.3816967
- [2026-08-18 22:48:58] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is enabled
  meta: kind=partial | timestamp=1787064538.4017413 | source=vosk | rms=959 | updated_at=1787064538.3816967
- [2026-08-18 22:48:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064538.6318889 | source=vosk | rms=904 | updated_at=1787064538.6318889
- [2026-08-18 22:48:58] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask
  meta: kind=partial | timestamp=1787064538.6500716 | source=vosk | rms=904 | updated_at=1787064538.6318889
- [2026-08-18 22:48:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064538.881886 | source=vosk | rms=1201 | updated_at=1787064538.881886
- [2026-08-18 22:48:58] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question
  meta: kind=partial | timestamp=1787064538.9523706 | source=vosk | rms=1201 | updated_at=1787064538.881886
- [2026-08-18 22:48:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064539.1315713 | source=vosk | rms=925 | updated_at=1787064539.1315713
- [2026-08-18 22:48:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064539.6320665 | source=vosk | rms=844 | updated_at=1787064539.6320665
- [2026-08-18 22:48:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064539.883029 | source=vosk | rms=837 | updated_at=1787064539.883029
- [2026-08-18 22:48:59] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question or
  meta: kind=partial | timestamp=1787064539.9101665 | source=vosk | rms=837 | updated_at=1787064539.883029
- [2026-08-18 22:49:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064540.1322863 | source=vosk | rms=791 | updated_at=1787064540.1322863
- [2026-08-18 22:49:00] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question or given
  meta: kind=partial | timestamp=1787064540.1707754 | source=vosk | rms=791 | updated_at=1787064540.1322863
- [2026-08-18 22:49:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064540.3824174 | source=vosk | rms=488 | updated_at=1787064540.3824174
- [2026-08-18 22:49:00] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question or give another
  meta: kind=partial | timestamp=1787064540.4055393 | source=vosk | rms=488 | updated_at=1787064540.3824174
- [2026-08-18 22:49:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064540.6331232 | source=vosk | rms=380 | updated_at=1787064540.6331232
- [2026-08-18 22:49:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064540.8842397 | source=vosk | rms=509 | updated_at=1787064540.8842397
- [2026-08-18 22:49:00] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question or give another command
  meta: kind=partial | timestamp=1787064540.9104688 | source=vosk | rms=509 | updated_at=1787064540.8842397
- [2026-08-18 22:49:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064541.3814654 | source=vosk | rms=509 | updated_at=1787064540.8842397
- [2026-08-18 22:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064546.6607904 | source=vosk | rms=509 | updated_at=1787064540.8842397
- [2026-08-18 22:49:06] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question or give another command when
  meta: kind=partial | timestamp=1787064546.7044451 | source=vosk | rms=509 | updated_at=1787064540.8842397
- [2026-08-18 22:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064546.8822203 | source=vosk | rms=858 | updated_at=1787064546.8822203
- [2026-08-18 22:49:06] operator / voice_transcript_partial / voice: running smart century now connecting the smart century boards first smart century pets are connected on the c o m link and smart century is unable to ask another question or give another command when read
  meta: kind=partial | timestamp=1787064546.9074063 | source=vosk | rms=858 | updated_at=1787064546.8822203
- [2026-08-18 22:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064547.1321797 | source=vosk | rms=1204 | updated_at=1787064547.1321797
- [2026-08-18 22:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064547.3821914 | source=vosk | rms=828 | updated_at=1787064547.3821914
- [2026-08-18 22:49:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064547.8822763 | source=vosk | rms=828 | updated_at=1787064547.3821914
- [2026-08-18 22:49:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064564.8828027 | source=vosk | rms=443 | updated_at=1787064564.8828027
- [2026-08-18 22:49:24] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1787064564.9039965 | source=final | rms=443 | updated_at=1787064564.8828027
- [2026-08-18 22:49:24] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064564.943235 | source=state | rms=443 | updated_at=1787064564.8828027
- [2026-08-18 22:49:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064564.943235 | source=state | rms=443 | updated_at=1787064564.8828027
- [2026-08-18 22:49:25] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-08-18 22:49:25] assistant / spoken_confirmation / voice: Smart Sentry is already connected and enabled.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:49:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064565.382094 | source=vosk | rms=1200 | updated_at=1787064565.382094
- [2026-08-18 22:49:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064565.881985 | source=vosk | rms=1200 | updated_at=1787064565.382094
- [2026-08-18 22:49:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064566.1371348 | source=vosk | rms=1206 | updated_at=1787064566.1371348
- [2026-08-18 22:49:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064566.882297 | source=vosk | rms=1206 | updated_at=1787064566.3817847
- [2026-08-18 22:49:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064567.137959 | source=vosk | rms=189 | updated_at=1787064567.137959
- [2026-08-18 22:49:27] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787064567.8919022 | source=vosk | rms=609 | updated_at=1787064567.88328
- [2026-08-18 22:49:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064568.3819342 | source=vosk | rms=1203 | updated_at=1787064568.3819342
- [2026-08-18 22:49:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064568.6313894 | source=vosk | rms=711 | updated_at=1787064568.6313894
- [2026-08-18 22:49:28] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1787064568.6429315 | source=vosk | rms=711 | updated_at=1787064568.6313894
- [2026-08-18 22:49:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064568.8824258 | source=vosk | rms=524 | updated_at=1787064568.8824258
- [2026-08-18 22:49:28] operator / voice_transcript_partial / voice: smart century is already
  meta: kind=partial | timestamp=1787064568.8934853 | source=vosk | rms=524 | updated_at=1787064568.8824258
- [2026-08-18 22:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064569.1319199 | source=vosk | rms=567 | updated_at=1787064569.1319199
- [2026-08-18 22:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064569.3825395 | source=vosk | rms=305 | updated_at=1787064569.3825395
- [2026-08-18 22:49:29] operator / voice_transcript_partial / voice: smart century is already connected
  meta: kind=partial | timestamp=1787064569.4042013 | source=vosk | rms=305 | updated_at=1787064569.3825395
- [2026-08-18 22:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064569.634599 | source=vosk | rms=396 | updated_at=1787064569.634599
- [2026-08-18 22:49:29] operator / voice_transcript_partial / voice: smart century is already connected and
  meta: kind=partial | timestamp=1787064569.664922 | source=vosk | rms=396 | updated_at=1787064569.634599
- [2026-08-18 22:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064569.8816776 | source=vosk | rms=251 | updated_at=1787064569.8816776
- [2026-08-18 22:49:29] operator / voice_transcript_partial / voice: smart century is already connected and unable
  meta: kind=partial | timestamp=1787064569.9108317 | source=vosk | rms=251 | updated_at=1787064569.8816776
- [2026-08-18 22:49:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064570.3821573 | source=vosk | rms=251 | updated_at=1787064569.8816776
- [2026-08-18 22:49:31] operator / voice_transcript_final / voice: smart sentry is already connect and unable
  meta: kind=final | timestamp=1787064571.4386518 | source=final | rms=251 | updated_at=1787064569.8816776
- [2026-08-18 22:49:31] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064571.8044214 | source=state | rms=251 | updated_at=1787064569.8816776
- [2026-08-18 22:49:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064571.8044214 | source=state | rms=251 | updated_at=1787064569.8816776
- [2026-08-18 22:49:32] operator / voice_command / voice: smart sentry is already connect and unable
  meta: normalized=True
- [2026-08-18 22:49:32] assistant / spoken_confirmation / voice: I did not catch a clear question or command. Please try again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:49:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064573.142603 | source=vosk | rms=1200 | updated_at=1787064573.142603
- [2026-08-18 22:49:33] operator / voice_transcript_partial / voice: smart century is already connected and enabled
  meta: kind=partial | timestamp=1787064573.1591635 | source=vosk | rms=1200 | updated_at=1787064573.142603
- [2026-08-18 22:49:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064573.3918998 | source=vosk | rms=1205 | updated_at=1787064573.3918998
- [2026-08-18 22:49:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064573.893381 | source=vosk | rms=755 | updated_at=1787064573.893381
- [2026-08-18 22:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064574.1933272 | source=vosk | rms=872 | updated_at=1787064574.1933272
- [2026-08-18 22:49:34] operator / voice_transcript_partial / voice: smart century is already connected and enabled i
  meta: kind=partial | timestamp=1787064574.2149644 | source=vosk | rms=872 | updated_at=1787064574.1933272
- [2026-08-18 22:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064574.3917913 | source=vosk | rms=1204 | updated_at=1787064574.3917913
- [2026-08-18 22:49:34] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not
  meta: kind=partial | timestamp=1787064574.4284503 | source=vosk | rms=1204 | updated_at=1787064574.3917913
- [2026-08-18 22:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064574.6418803 | source=vosk | rms=744 | updated_at=1787064574.6418803
- [2026-08-18 22:49:34] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch
  meta: kind=partial | timestamp=1787064574.6665766 | source=vosk | rms=744 | updated_at=1787064574.6418803
- [2026-08-18 22:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064574.892818 | source=vosk | rms=655 | updated_at=1787064574.892818
- [2026-08-18 22:49:34] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a
  meta: kind=partial | timestamp=1787064574.9214275 | source=vosk | rms=655 | updated_at=1787064574.892818
- [2026-08-18 22:49:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064575.1836398 | source=vosk | rms=1188 | updated_at=1787064575.1836398
- [2026-08-18 22:49:35] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear
  meta: kind=partial | timestamp=1787064575.2062378 | source=vosk | rms=1188 | updated_at=1787064575.1836398
- [2026-08-18 22:49:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064575.392067 | source=vosk | rms=370 | updated_at=1787064575.392067
- [2026-08-18 22:49:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064575.678515 | source=vosk | rms=319 | updated_at=1787064575.678515
- [2026-08-18 22:49:35] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or
  meta: kind=partial | timestamp=1787064575.698399 | source=vosk | rms=319 | updated_at=1787064575.678515
- [2026-08-18 22:49:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064575.8941777 | source=vosk | rms=345 | updated_at=1787064575.8941777
- [2026-08-18 22:49:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064576.391939 | source=vosk | rms=689 | updated_at=1787064576.391939
- [2026-08-18 22:49:36] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command
  meta: kind=partial | timestamp=1787064576.404793 | source=vosk | rms=689 | updated_at=1787064576.391939
- [2026-08-18 22:49:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064576.6923642 | source=vosk | rms=1200 | updated_at=1787064576.6923642
- [2026-08-18 22:49:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064577.2294402 | source=vosk | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:37] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please
  meta: kind=partial | timestamp=1787064577.2989106 | source=vosk | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064577.7225494 | source=vosk | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:37] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try
  meta: kind=partial | timestamp=1787064577.7391524 | source=vosk | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:39] operator / voice_transcript_final / voice: smart sentry is already connect and enable i did not catch a clear question or command please try
  meta: kind=final | timestamp=1787064579.2906446 | source=final | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:39] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064579.7878945 | source=state | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064579.7878945 | source=state | rms=922 | updated_at=1787064577.2294402
- [2026-08-18 22:49:39] operator / voice_command / voice: smart sentry is already connect and enable i did not catch a clear question or command please try
  meta: normalized=True
- [2026-08-18 22:49:40] assistant / spoken_confirmation / voice: I did not catch a clear question or command. Please try again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:49:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064582.476671 | source=vosk | rms=733 | updated_at=1787064582.476671
- [2026-08-18 22:49:44] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787064584.6071918 | source=state | rms=366 | updated_at=1787064584.472127
- [2026-08-18 22:49:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064584.472127 | source=vosk | rms=366 | updated_at=1787064584.472127
- [2026-08-18 22:49:44] assistant / spoken_confirmation / voice: Guarding continues. Say the wake word when you need me again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:49:44] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command
  meta: kind=partial | timestamp=1787064584.9965196 | source=vosk | rms=584 | updated_at=1787064584.9733498
- [2026-08-18 22:49:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064585.2518153 | source=vosk | rms=1206 | updated_at=1787064585.2518153
- [2026-08-18 22:49:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064585.474568 | source=vosk | rms=981 | updated_at=1787064585.474568
- [2026-08-18 22:49:45] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please
  meta: kind=partial | timestamp=1787064585.493259 | source=vosk | rms=981 | updated_at=1787064585.474568
- [2026-08-18 22:49:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064585.7236974 | source=vosk | rms=450 | updated_at=1787064585.7236974
- [2026-08-18 22:49:45] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again
  meta: kind=partial | timestamp=1787064585.7462456 | source=vosk | rms=450 | updated_at=1787064585.7236974
- [2026-08-18 22:49:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064586.223872 | source=vosk | rms=1131 | updated_at=1787064586.223872
- [2026-08-18 22:49:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064586.4735394 | source=vosk | rms=1092 | updated_at=1787064586.4735394
- [2026-08-18 22:49:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064586.721979 | source=vosk | rms=1206 | updated_at=1787064586.721979
- [2026-08-18 22:49:46] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding
  meta: kind=partial | timestamp=1787064586.7647603 | source=vosk | rms=1206 | updated_at=1787064586.721979
- [2026-08-18 22:49:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064586.9721866 | source=vosk | rms=465 | updated_at=1787064586.9721866
- [2026-08-18 22:49:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064587.2418303 | source=vosk | rms=1200 | updated_at=1787064587.2418303
- [2026-08-18 22:49:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064587.7257738 | source=vosk | rms=1035 | updated_at=1787064587.7257738
- [2026-08-18 22:49:47] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuously
  meta: kind=partial | timestamp=1787064587.778335 | source=vosk | rms=1035 | updated_at=1787064587.7257738
- [2026-08-18 22:49:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064587.971879 | source=vosk | rms=802 | updated_at=1787064587.971879
- [2026-08-18 22:49:47] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous
  meta: kind=partial | timestamp=1787064587.99764 | source=vosk | rms=802 | updated_at=1787064587.971879
- [2026-08-18 22:49:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064588.2219887 | source=vosk | rms=462 | updated_at=1787064588.2219887
- [2026-08-18 22:49:48] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the
  meta: kind=partial | timestamp=1787064588.2510793 | source=vosk | rms=462 | updated_at=1787064588.2219887
- [2026-08-18 22:49:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064588.4727511 | source=vosk | rms=635 | updated_at=1787064588.4727511
- [2026-08-18 22:49:48] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake
  meta: kind=partial | timestamp=1787064588.5321696 | source=vosk | rms=635 | updated_at=1787064588.4727511
- [2026-08-18 22:49:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064588.7634783 | source=vosk | rms=635 | updated_at=1787064588.4727511
- [2026-08-18 22:49:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064588.974044 | source=vosk | rms=456 | updated_at=1787064588.974044
- [2026-08-18 22:49:49] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake word when
  meta: kind=partial | timestamp=1787064589.0132349 | source=vosk | rms=456 | updated_at=1787064588.974044
- [2026-08-18 22:49:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064589.2295544 | source=vosk | rms=615 | updated_at=1787064589.2295544
- [2026-08-18 22:49:49] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake word when you need
  meta: kind=partial | timestamp=1787064589.277511 | source=vosk | rms=615 | updated_at=1787064589.2295544
- [2026-08-18 22:49:51] operator / voice_transcript_final / voice: smart sentry is already connect and enable i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake word when you need
  meta: kind=final | timestamp=1787064591.6470528 | source=final | rms=615 | updated_at=1787064589.2295544
- [2026-08-18 22:49:53] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064593.6434584 | source=state | rms=615 | updated_at=1787064589.2295544
- [2026-08-18 22:49:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064593.6444626 | source=state | rms=615 | updated_at=1787064589.2295544
- [2026-08-18 22:50:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064600.682496 | source=vosk | rms=897 | updated_at=1787064600.682496
- [2026-08-18 22:50:00] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake word when you need me
  meta: kind=partial | timestamp=1787064600.735446 | source=vosk | rms=897 | updated_at=1787064600.682496
- [2026-08-18 22:50:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064600.8830175 | source=vosk | rms=1206 | updated_at=1787064600.8830175
- [2026-08-18 22:50:00] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake word when you need me a gap
  meta: kind=partial | timestamp=1787064600.9135756 | source=vosk | rms=1206 | updated_at=1787064600.8830175
- [2026-08-18 22:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064601.1328375 | source=vosk | rms=830 | updated_at=1787064601.1328375
- [2026-08-18 22:50:01] operator / voice_transcript_partial / voice: smart century is already connected and enabled i did not catch a clear question or command please try again i did not catch a clear question or command please try again guarding continuous say the wake word when you need me again
  meta: kind=partial | timestamp=1787064601.1544118 | source=vosk | rms=830 | updated_at=1787064601.1328375
- [2026-08-18 22:50:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064601.6366062 | source=vosk | rms=830 | updated_at=1787064601.1328375
- [2026-08-18 22:50:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064611.3835533 | source=vosk | rms=1207 | updated_at=1787064611.3835533
- [2026-08-18 22:50:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064613.1448581 | source=vosk | rms=756 | updated_at=1787064612.6335857
- [2026-08-18 22:50:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064613.387835 | source=vosk | rms=1101 | updated_at=1787064613.387835
- [2026-08-18 22:50:13] operator / voice_transcript_partial / voice: reset profile set to cost a smart
  meta: kind=partial | timestamp=1787064613.9138613 | source=vosk | rms=756 | updated_at=1787064613.8872094
- [2026-08-18 22:50:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064614.1624892 | source=vosk | rms=670 | updated_at=1787064614.1624892
- [2026-08-18 22:50:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064614.396242 | source=vosk | rms=611 | updated_at=1787064614.396242
- [2026-08-18 22:50:14] operator / voice_transcript_partial / voice: reset profile set to cost a smart century
  meta: kind=partial | timestamp=1787064614.4177768 | source=vosk | rms=611 | updated_at=1787064614.396242
- [2026-08-18 22:50:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064614.6516416 | source=vosk | rms=465 | updated_at=1787064614.6516416
- [2026-08-18 22:50:14] operator / voice_transcript_partial / voice: reset profile set to cost a smart century speed
  meta: kind=partial | timestamp=1787064614.6794667 | source=vosk | rms=465 | updated_at=1787064614.6516416
- [2026-08-18 22:50:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064615.1334925 | source=vosk | rms=465 | updated_at=1787064614.6516416
- [2026-08-18 22:50:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064622.882369 | source=vosk | rms=212 | updated_at=1787064622.882369
- [2026-08-18 22:50:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064623.1321385 | source=vosk | rms=504 | updated_at=1787064623.1321385
- [2026-08-18 22:50:23] operator / voice_transcript_partial / voice: reset profile set to cost a smart century speed five
  meta: kind=partial | timestamp=1787064623.1985247 | source=vosk | rms=504 | updated_at=1787064623.1321385
- [2026-08-18 22:50:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064623.382436 | source=vosk | rms=294 | updated_at=1787064623.382436
- [2026-08-18 22:50:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064623.631999 | source=vosk | rms=330 | updated_at=1787064623.631999
- [2026-08-18 22:50:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064623.8824515 | source=vosk | rms=299 | updated_at=1787064623.8824515
- [2026-08-18 22:50:24] operator / voice_transcript_final / voice: rest profile set to cost a smart sentry speed five
  meta: kind=final | timestamp=1787064624.1745574 | source=final | rms=299 | updated_at=1787064623.8824515
- [2026-08-18 22:50:24] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064624.2820573 | source=state | rms=299 | updated_at=1787064623.8824515
- [2026-08-18 22:50:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064624.2820573 | source=state | rms=299 | updated_at=1787064623.8824515
- [2026-08-18 22:50:24] operator / voice_command / voice: rest profile set to cost a smart sentry speed five
  meta: normalized=True
- [2026-08-18 22:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064624.2820573 | source=vosk | rms=376 | updated_at=1787064624.2820573
- [2026-08-18 22:50:24] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:50:26] operator / voice_transcript_partial / voice: going
  meta: kind=partial | timestamp=1787064626.5275617 | source=vosk | rms=1152 | updated_at=1787064626.132314
- [2026-08-18 22:50:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064626.5275617 | source=vosk | rms=535 | updated_at=1787064626.5275617
- [2026-08-18 22:50:26] operator / voice_transcript_partial / voice: going to rest position
  meta: kind=partial | timestamp=1787064626.9958465 | source=vosk | rms=429 | updated_at=1787064626.9547904
- [2026-08-18 22:50:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064627.1469138 | source=vosk | rms=535 | updated_at=1787064627.13377
- [2026-08-18 22:50:27] operator / voice_transcript_partial / voice: going to rest position now
  meta: kind=partial | timestamp=1787064627.1469138 | source=vosk | rms=535 | updated_at=1787064627.13377
- [2026-08-18 22:50:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064627.754578 | source=vosk | rms=490 | updated_at=1787064627.754578
- [2026-08-18 22:50:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064628.2535808 | source=vosk | rms=490 | updated_at=1787064627.754578
- [2026-08-18 22:50:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064628.7520616 | source=vosk | rms=269 | updated_at=1787064628.7520616
- [2026-08-18 22:50:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064629.25283 | source=vosk | rms=269 | updated_at=1787064628.7520616
- [2026-08-18 22:50:30] operator / voice_transcript_final / voice: going to rest position now
  meta: kind=final | timestamp=1787064630.329122 | source=final | rms=269 | updated_at=1787064628.7520616
- [2026-08-18 22:50:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064630.7552068 | source=vosk | rms=541 | updated_at=1787064630.7552068
- [2026-08-18 22:50:30] operator / voice_transcript_partial / voice: going to rest position now
  meta: kind=partial | timestamp=1787064630.7737985 | source=vosk | rms=541 | updated_at=1787064630.7552068
- [2026-08-18 22:50:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064631.0025475 | source=vosk | rms=541 | updated_at=1787064630.7552068
- [2026-08-18 22:50:31] operator / voice_transcript_final / voice: going to rest position now
  meta: kind=final | timestamp=1787064631.3504317 | source=final | rms=541 | updated_at=1787064630.7552068
- [2026-08-18 22:50:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064631.4923303 | source=vosk | rms=541 | updated_at=1787064630.7552068
- [2026-08-18 22:50:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064631.4923303 | source=vosk | rms=305 | updated_at=1787064631.4923303
- [2026-08-18 22:50:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064634.0022767 | source=vosk | rms=283 | updated_at=1787064633.5031912
- [2026-08-18 22:50:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064650.5030704 | source=vosk | rms=219 | updated_at=1787064650.5030704
- [2026-08-18 22:50:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064651.0024803 | source=vosk | rms=219 | updated_at=1787064650.5030704
- [2026-08-18 22:50:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064654.2561932 | source=vosk | rms=219 | updated_at=1787064650.5030704
- [2026-08-18 22:50:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064654.7780747 | source=vosk | rms=219 | updated_at=1787064650.5030704
- [2026-08-18 22:50:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064655.003132 | source=vosk | rms=167 | updated_at=1787064655.003132
- [2026-08-18 22:50:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064655.5038507 | source=vosk | rms=167 | updated_at=1787064655.003132
- [2026-08-18 22:50:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064655.7541084 | source=vosk | rms=257 | updated_at=1787064655.7541084
- [2026-08-18 22:50:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064656.2541225 | source=vosk | rms=257 | updated_at=1787064655.7541084
- [2026-08-18 22:50:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064659.0028024 | source=vosk | rms=257 | updated_at=1787064655.7541084
- [2026-08-18 22:51:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064678.2527745 | source=vosk | rms=132 | updated_at=1787064676.2524176 | frequency_hz=328.0
- [2026-08-18 22:51:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064692.6530259 | source=vosk | rms=132 | updated_at=1787064676.2524176 | frequency_hz=328.0
- [2026-08-18 22:51:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064693.4042094 | source=vosk | rms=209 | updated_at=1787064692.9162123 | frequency_hz=328.0
- [2026-08-18 22:51:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064696.4074593 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064696.9030156 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064700.078301 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064700.5743325 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064713.0732543 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064713.5750976 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064714.3233793 | source=vosk | rms=221 | updated_at=1787064696.4074593 | frequency_hz=328.0
- [2026-08-18 22:51:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064716.073041 | source=vosk | rms=143 | updated_at=1787064715.573589 | frequency_hz=328.0
- [2026-08-18 22:51:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064716.5735164 | source=vosk | rms=143 | updated_at=1787064715.573589 | frequency_hz=328.0
- [2026-08-18 22:51:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064717.323409 | source=vosk | rms=143 | updated_at=1787064715.573589 | frequency_hz=328.0
- [2026-08-18 22:52:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064728.894031 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064729.3936865 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064733.643484 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064734.143741 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064735.395054 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064735.8937778 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064737.3938506 | source=vosk | rms=411 | updated_at=1787064728.894031 | frequency_hz=328.0
- [2026-08-18 22:52:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064738.8934612 | source=vosk | rms=161 | updated_at=1787064738.3938239 | frequency_hz=328.0
- [2026-08-18 22:52:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064740.14371 | source=vosk | rms=161 | updated_at=1787064738.3938239 | frequency_hz=328.0
- [2026-08-18 22:52:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064740.643465 | source=vosk | rms=161 | updated_at=1787064738.3938239 | frequency_hz=328.0
- [2026-08-18 22:52:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064744.1444788 | source=vosk | rms=161 | updated_at=1787064738.3938239 | frequency_hz=328.0
- [2026-08-18 22:52:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064745.3935373 | source=vosk | rms=161 | updated_at=1787064738.3938239 | frequency_hz=328.0
- [2026-08-18 22:52:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064746.6442165 | source=vosk | rms=161 | updated_at=1787064738.3938239 | frequency_hz=328.0
- [2026-08-18 22:52:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064749.6438386 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064752.6438575 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064753.1444457 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064753.8935428 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064754.393955 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064755.6437337 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064756.3939602 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064759.145418 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064760.1986308 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064761.8942633 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064762.8782372 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064763.1261506 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064763.8738546 | source=vosk | rms=302 | updated_at=1787064748.8938131 | frequency_hz=328.0
- [2026-08-18 22:52:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064765.3740678 | source=vosk | rms=264 | updated_at=1787064765.3740678 | frequency_hz=328.0
- [2026-08-18 22:52:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064767.8738964 | source=vosk | rms=175 | updated_at=1787064766.3758245 | frequency_hz=328.0
- [2026-08-18 22:52:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064768.374116 | source=vosk | rms=175 | updated_at=1787064766.3758245 | frequency_hz=328.0
- [2026-08-18 22:52:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064768.8739276 | source=vosk | rms=175 | updated_at=1787064766.3758245 | frequency_hz=328.0
- [2026-08-18 22:52:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064769.8727953 | source=vosk | rms=175 | updated_at=1787064766.3758245 | frequency_hz=328.0
- [2026-08-18 22:52:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064771.3744075 | source=vosk | rms=175 | updated_at=1787064766.3758245 | frequency_hz=328.0
- [2026-08-18 22:52:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064771.8732684 | source=vosk | rms=436 | updated_at=1787064771.8732684 | frequency_hz=328.0
- [2026-08-18 22:52:52] operator / voice_transcript_partial / voice: earlier
  meta: kind=partial | timestamp=1787064772.4227338 | source=vosk | rms=218 | updated_at=1787064772.3730733 | frequency_hz=328.0
- [2026-08-18 22:52:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064772.8729677 | source=vosk | rms=218 | updated_at=1787064772.3730733 | frequency_hz=328.0
- [2026-08-18 22:52:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064773.1243322 | source=vosk | rms=218 | updated_at=1787064772.3730733 | frequency_hz=328.0
- [2026-08-18 22:52:53] operator / voice_transcript_partial / voice: earlier in
  meta: kind=partial | timestamp=1787064773.1454525 | source=vosk | rms=218 | updated_at=1787064772.3730733 | frequency_hz=328.0
- [2026-08-18 22:52:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064773.6864114 | source=vosk | rms=218 | updated_at=1787064772.3730733 | frequency_hz=328.0
- [2026-08-18 22:52:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064776.1136408 | source=vosk | rms=218 | updated_at=1787064772.3730733 | frequency_hz=328.0
- [2026-08-18 22:52:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064776.6164925 | source=vosk | rms=304 | updated_at=1787064776.6164925 | frequency_hz=328.0
- [2026-08-18 22:52:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064776.8645284 | source=vosk | rms=600 | updated_at=1787064776.8645284 | frequency_hz=328.0
- [2026-08-18 22:52:57] operator / voice_transcript_final / voice: earlier
  meta: kind=final | timestamp=1787064777.521788 | source=final | rms=600 | updated_at=1787064776.8645284 | frequency_hz=328.0
- [2026-08-18 22:52:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064777.5568895 | source=vosk | rms=600 | updated_at=1787064776.8645284 | frequency_hz=328.0
- [2026-08-18 22:52:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064777.5568895 | source=vosk | rms=413 | updated_at=1787064777.5568895 | frequency_hz=328.0
- [2026-08-18 22:52:57] operator / voice_transcript_partial / voice: tell me
  meta: kind=partial | timestamp=1787064777.6299272 | source=vosk | rms=214 | updated_at=1787064777.59534 | frequency_hz=328.0
- [2026-08-18 22:52:57] operator / voice_transcript_partial / voice: tell me what you
  meta: kind=partial | timestamp=1787064777.6476388 | source=vosk | rms=541 | updated_at=1787064777.6299272 | frequency_hz=328.0
- [2026-08-18 22:52:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064777.9102502 | source=vosk | rms=838 | updated_at=1787064777.9102502 | frequency_hz=328.0
- [2026-08-18 22:52:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064778.113322 | source=vosk | rms=208 | updated_at=1787064778.113322 | frequency_hz=328.0
- [2026-08-18 22:52:58] operator / voice_transcript_partial / voice: tell me what you consider
  meta: kind=partial | timestamp=1787064778.1318629 | source=vosk | rms=208 | updated_at=1787064778.113322 | frequency_hz=328.0
- [2026-08-18 22:52:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064778.3647437 | source=vosk | rms=243 | updated_at=1787064778.3647437 | frequency_hz=328.0
- [2026-08-18 22:52:58] operator / voice_transcript_partial / voice: tell me what you can see from
  meta: kind=partial | timestamp=1787064778.376771 | source=vosk | rms=243 | updated_at=1787064778.3647437 | frequency_hz=328.0
- [2026-08-18 22:52:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064778.612927 | source=vosk | rms=232 | updated_at=1787064778.612927 | frequency_hz=328.0
- [2026-08-18 22:52:58] operator / voice_transcript_partial / voice: tell me what you can see from the
  meta: kind=partial | timestamp=1787064778.642974 | source=vosk | rms=232 | updated_at=1787064778.612927 | frequency_hz=328.0
- [2026-08-18 22:52:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064779.114173 | source=vosk | rms=232 | updated_at=1787064778.612927 | frequency_hz=328.0
- [2026-08-18 22:52:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064779.613309 | source=vosk | rms=232 | updated_at=1787064778.612927 | frequency_hz=328.0
- [2026-08-18 22:53:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064785.4144614 | source=vosk | rms=1082 | updated_at=1787064785.4144614 | frequency_hz=328.0
- [2026-08-18 22:53:05] operator / voice_transcript_partial / voice: tell me what you can see from the cameras
  meta: kind=partial | timestamp=1787064785.447041 | source=vosk | rms=1082 | updated_at=1787064785.4144614 | frequency_hz=328.0
- [2026-08-18 22:53:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064785.6142557 | source=vosk | rms=447 | updated_at=1787064785.6127465 | frequency_hz=328.0
- [2026-08-18 22:53:05] operator / voice_transcript_partial / voice: tell me what you can see from the cameras in
  meta: kind=partial | timestamp=1787064785.6333528 | source=vosk | rms=447 | updated_at=1787064785.6127465 | frequency_hz=328.0
- [2026-08-18 22:53:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064786.113889 | source=vosk | rms=447 | updated_at=1787064785.6127465 | frequency_hz=328.0
- [2026-08-18 22:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064788.1130643 | source=vosk | rms=1201 | updated_at=1787064788.1130643 | frequency_hz=328.0
- [2026-08-18 22:53:08] operator / voice_transcript_partial / voice: tell me what you can see from the cameras in your
  meta: kind=partial | timestamp=1787064788.15281 | source=vosk | rms=1201 | updated_at=1787064788.1130643 | frequency_hz=328.0
- [2026-08-18 22:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064788.3636837 | source=vosk | rms=1200 | updated_at=1787064788.3636837 | frequency_hz=328.0
- [2026-08-18 22:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064788.6145718 | source=vosk | rms=882 | updated_at=1787064788.6145718 | frequency_hz=328.0
- [2026-08-18 22:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064788.8974917 | source=vosk | rms=1204 | updated_at=1787064788.8974917 | frequency_hz=328.0
- [2026-08-18 22:53:09] operator / voice_transcript_final / voice: tell me what you can see from the camera earlier
  meta: kind=final | timestamp=1787064789.241594 | source=final | rms=1204 | updated_at=1787064788.8974917 | frequency_hz=328.0
- [2026-08-18 22:53:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064789.3817527 | source=vosk | rms=1204 | updated_at=1787064788.8974917 | frequency_hz=328.0
- [2026-08-18 22:53:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064789.3817527 | source=vosk | rms=1201 | updated_at=1787064789.3817527 | frequency_hz=328.0
- [2026-08-18 22:53:12] operator / voice_transcript_partial / voice: ilya
  meta: kind=partial | timestamp=1787064792.630197 | source=vosk | rms=1201 | updated_at=1787064792.613672 | frequency_hz=207.8
- [2026-08-18 22:53:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064792.8634925 | source=vosk | rms=686 | updated_at=1787064792.8634925 | frequency_hz=182.0
- [2026-08-18 22:53:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064793.1130655 | source=vosk | rms=674 | updated_at=1787064793.1130655 | frequency_hz=171.5
- [2026-08-18 22:53:13] operator / voice_transcript_final / voice: ilya
  meta: kind=final | timestamp=1787064793.3198946 | source=final | rms=674 | updated_at=1787064793.1130655 | frequency_hz=171.5
- [2026-08-18 22:53:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064793.3695314 | source=vosk | rms=607 | updated_at=1787064793.3695314 | frequency_hz=203.9
- [2026-08-18 22:53:14] operator / voice_transcript_partial / voice: earlier
  meta: kind=partial | timestamp=1787064794.8785186 | source=vosk | rms=347 | updated_at=1787064794.8637798 | frequency_hz=201.4
- [2026-08-18 22:53:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064795.1132886 | source=vosk | rms=388 | updated_at=1787064795.1132886 | frequency_hz=172.9
- [2026-08-18 22:53:15] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787064795.12181 | source=vosk | rms=388 | updated_at=1787064795.1132886 | frequency_hz=172.9
- [2026-08-18 22:53:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064795.8635497 | source=vosk | rms=624 | updated_at=1787064795.8635497 | frequency_hz=139.0
- [2026-08-18 22:53:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064796.1425955 | source=vosk | rms=986 | updated_at=1787064796.1425955 | frequency_hz=172.9
- [2026-08-18 22:53:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064796.3649366 | source=vosk | rms=955 | updated_at=1787064796.3649366 | frequency_hz=174.0
- [2026-08-18 22:53:16] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1787064796.958129 | source=final | rms=955 | updated_at=1787064796.3649366 | frequency_hz=174.0
- [2026-08-18 22:53:17] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-08-18 22:53:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064796.9591322 | source=vosk | rms=1203 | updated_at=1787064796.9591322 | frequency_hz=174.0
- [2026-08-18 22:53:17] assistant / spoken_confirmation / voice: I am listening. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:53:18] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064798.963396 | source=state | rms=542 | updated_at=1787064798.9533687 | frequency_hz=94.3
- [2026-08-18 22:53:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064798.963396 | source=state | rms=542 | updated_at=1787064798.9533687 | frequency_hz=94.3
- [2026-08-18 22:53:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064799.2037244 | source=vosk | rms=514 | updated_at=1787064799.2037244 | frequency_hz=94.3
- [2026-08-18 22:53:20] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787064800.3206236 | source=state | rms=1203 | updated_at=1787064800.2048397 | frequency_hz=205.5
- [2026-08-18 22:53:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064800.2048397 | source=vosk | rms=1203 | updated_at=1787064800.2048397 | frequency_hz=205.5
- [2026-08-18 22:53:21] operator / voice_transcript_partial / voice: tell
  meta: kind=partial | timestamp=1787064801.288606 | source=vosk | rms=1229 | updated_at=1787064801.2037566 | frequency_hz=227.4
- [2026-08-18 22:53:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064801.4532003 | source=vosk | rms=1133 | updated_at=1787064801.4532003 | frequency_hz=227.4
- [2026-08-18 22:53:21] operator / voice_transcript_partial / voice: tell me
  meta: kind=partial | timestamp=1787064801.471724 | source=vosk | rms=1133 | updated_at=1787064801.4532003 | frequency_hz=227.4
- [2026-08-18 22:53:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064801.729034 | source=vosk | rms=1200 | updated_at=1787064801.729034 | frequency_hz=227.4
- [2026-08-18 22:53:21] operator / voice_transcript_partial / voice: tell me what you
  meta: kind=partial | timestamp=1787064801.749171 | source=vosk | rms=1200 | updated_at=1787064801.729034 | frequency_hz=227.4
- [2026-08-18 22:53:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064801.9537616 | source=vosk | rms=1219 | updated_at=1787064801.9537616 | frequency_hz=227.4
- [2026-08-18 22:53:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064802.2039616 | source=vosk | rms=1200 | updated_at=1787064802.2039616 | frequency_hz=227.4
- [2026-08-18 22:53:22] operator / voice_transcript_partial / voice: tell me what you can see
  meta: kind=partial | timestamp=1787064802.2125776 | source=vosk | rms=1200 | updated_at=1787064802.2039616 | frequency_hz=227.4
- [2026-08-18 22:53:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064802.4531362 | source=vosk | rms=1200 | updated_at=1787064802.4531362 | frequency_hz=227.4
- [2026-08-18 22:53:22] operator / voice_transcript_partial / voice: tell me what you can see from
  meta: kind=partial | timestamp=1787064802.4621446 | source=vosk | rms=1200 | updated_at=1787064802.4531362 | frequency_hz=227.4
- [2026-08-18 22:53:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064802.704388 | source=vosk | rms=1200 | updated_at=1787064802.703385 | frequency_hz=227.4
- [2026-08-18 22:53:22] operator / voice_transcript_partial / voice: tell me what you can see from the
  meta: kind=partial | timestamp=1787064802.7179189 | source=vosk | rms=1200 | updated_at=1787064802.703385 | frequency_hz=227.4
- [2026-08-18 22:53:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064802.9545386 | source=vosk | rms=1205 | updated_at=1787064802.9545386 | frequency_hz=279.4
- [2026-08-18 22:53:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064803.953891 | source=vosk | rms=701 | updated_at=1787064803.953891 | frequency_hz=279.4
- [2026-08-18 22:53:23] operator / voice_transcript_partial / voice: tell me what you can see from the camera
  meta: kind=partial | timestamp=1787064803.965406 | source=vosk | rms=701 | updated_at=1787064803.953891 | frequency_hz=279.4
- [2026-08-18 22:53:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064804.2033033 | source=vosk | rms=411 | updated_at=1787064804.2033033 | frequency_hz=202.6
- [2026-08-18 22:53:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064805.2032607 | source=vosk | rms=411 | updated_at=1787064804.2033033 | frequency_hz=202.6
- [2026-08-18 22:53:25] operator / voice_transcript_final / voice: tell me what you can see from the camera
  meta: kind=final | timestamp=1787064805.4817345 | source=final | rms=411 | updated_at=1787064804.2033033 | frequency_hz=202.6
- [2026-08-18 22:53:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064805.6356468 | source=vosk | rms=734 | updated_at=1787064805.6356468 | frequency_hz=218.0
- [2026-08-18 22:53:26] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787064806.236303 | source=vosk | rms=734 | updated_at=1787064805.6356468 | frequency_hz=218.0
- [2026-08-18 22:53:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064811.4539607 | source=vosk | rms=734 | updated_at=1787064805.6356468 | frequency_hz=218.0
- [2026-08-18 22:53:35] operator / voice_transcript_partial / voice: what's
  meta: kind=partial | timestamp=1787064815.4858458 | source=vosk | rms=1200 | updated_at=1787064815.45479 | frequency_hz=156.0
- [2026-08-18 22:53:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064815.7043548 | source=vosk | rms=1622 | updated_at=1787064815.7043548 | frequency_hz=156.0
- [2026-08-18 22:53:35] operator / voice_transcript_partial / voice: what's the
  meta: kind=partial | timestamp=1787064815.7173796 | source=vosk | rms=1622 | updated_at=1787064815.7043548 | frequency_hz=156.0
- [2026-08-18 22:53:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064815.9538798 | source=vosk | rms=1509 | updated_at=1787064815.9538798 | frequency_hz=156.0
- [2026-08-18 22:53:35] operator / voice_transcript_partial / voice: what's the status
  meta: kind=partial | timestamp=1787064815.9709296 | source=vosk | rms=1509 | updated_at=1787064815.9538798 | frequency_hz=156.0
- [2026-08-18 22:53:36] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064816.360919 | source=state | rms=1509 | updated_at=1787064815.9538798 | frequency_hz=156.0
- [2026-08-18 22:53:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064816.3694308 | source=state | rms=1509 | updated_at=1787064815.9538798 | frequency_hz=156.0
- [2026-08-18 22:53:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064816.3694308 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064816.9536695 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064817.4539607 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064817.7045062 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064817.954803 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:38] operator / voice_transcript_final / voice: what s the status
  meta: kind=final | timestamp=1787064818.2873108 | source=final | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064818.4440064 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064818.4440064 | source=vosk | rms=1200 | updated_at=1787064816.3694308 | frequency_hz=156.0
- [2026-08-18 22:53:49] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787064829.3219447 | source=vosk | rms=1203 | updated_at=1787064829.2938988 | frequency_hz=141.8
- [2026-08-18 22:53:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064829.5433993 | source=vosk | rms=1200 | updated_at=1787064829.5433993 | frequency_hz=132.1
- [2026-08-18 22:53:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064830.0705276 | source=vosk | rms=1092 | updated_at=1787064830.0705276 | frequency_hz=172.0
- [2026-08-18 22:53:51] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1787064831.4734335 | source=final | rms=1092 | updated_at=1787064830.0705276 | frequency_hz=172.0
- [2026-08-18 22:53:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-08-18 22:53:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064831.5438256 | source=vosk | rms=1092 | updated_at=1787064830.0705276 | frequency_hz=172.0
- [2026-08-18 22:53:51] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787064831.5528688 | source=vosk | rms=1092 | updated_at=1787064830.0705276 | frequency_hz=172.0
- [2026-08-18 22:53:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064831.7942977 | source=vosk | rms=820 | updated_at=1787064831.7942977 | frequency_hz=212.0
- [2026-08-18 22:53:52] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1787064832.517323 | source=final | rms=820 | updated_at=1787064831.7942977 | frequency_hz=212.0
- [2026-08-18 22:53:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064832.5183275 | source=vosk | rms=820 | updated_at=1787064831.7942977 | frequency_hz=212.0
- [2026-08-18 22:53:54] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064834.3061655 | source=state | rms=1203 | updated_at=1787064834.3000813 | frequency_hz=97.2
- [2026-08-18 22:53:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064834.3061655 | source=state | rms=1203 | updated_at=1787064834.3000813 | frequency_hz=97.2
- [2026-08-18 22:53:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064834.5516403 | source=vosk | rms=976 | updated_at=1787064834.5516403 | frequency_hz=94.7
- [2026-08-18 22:53:55] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787064835.4361632 | source=state | rms=1200 | updated_at=1787064835.2938626 | frequency_hz=166.3
- [2026-08-18 22:53:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064835.2938626 | source=vosk | rms=1200 | updated_at=1787064835.2938626 | frequency_hz=166.3
- [2026-08-18 22:53:56] operator / voice_transcript_partial / voice: increase the
  meta: kind=partial | timestamp=1787064836.0795484 | source=vosk | rms=1200 | updated_at=1787064836.052517 | frequency_hz=166.3
- [2026-08-18 22:53:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064836.3362455 | source=vosk | rms=1200 | updated_at=1787064836.3362455 | frequency_hz=166.3
- [2026-08-18 22:53:56] operator / voice_transcript_partial / voice: increase the truck
  meta: kind=partial | timestamp=1787064836.3590467 | source=vosk | rms=1200 | updated_at=1787064836.3362455 | frequency_hz=166.3
- [2026-08-18 22:53:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064836.544098 | source=vosk | rms=1202 | updated_at=1787064836.544098 | frequency_hz=166.3
- [2026-08-18 22:53:56] operator / voice_transcript_partial / voice: increase the trucking
  meta: kind=partial | timestamp=1787064836.5581415 | source=vosk | rms=1202 | updated_at=1787064836.544098 | frequency_hz=166.3
- [2026-08-18 22:53:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064836.7938988 | source=vosk | rms=915 | updated_at=1787064836.7938988 | frequency_hz=166.3
- [2026-08-18 22:53:56] operator / voice_transcript_partial / voice: increase the trucking speed
  meta: kind=partial | timestamp=1787064836.8066611 | source=vosk | rms=915 | updated_at=1787064836.7938988 | frequency_hz=166.3
- [2026-08-18 22:53:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064837.0774314 | source=vosk | rms=1300 | updated_at=1787064837.0774314 | frequency_hz=137.5
- [2026-08-18 22:53:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064838.0440276 | source=vosk | rms=1300 | updated_at=1787064837.0774314 | frequency_hz=137.5
- [2026-08-18 22:53:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064838.2943614 | source=vosk | rms=1300 | updated_at=1787064837.0774314 | frequency_hz=137.5
- [2026-08-18 22:53:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064838.54443 | source=vosk | rms=1201 | updated_at=1787064838.54443 | frequency_hz=70.0
- [2026-08-18 22:53:58] operator / voice_transcript_final / voice: increase the tracking speed
  meta: kind=final | timestamp=1787064838.8859508 | source=final | rms=1201 | updated_at=1787064838.54443 | frequency_hz=70.0
- [2026-08-18 22:53:59] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787064839.7675867 | source=state | rms=1201 | updated_at=1787064838.54443 | frequency_hz=70.0
- [2026-08-18 22:53:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064839.7732701 | source=state | rms=1201 | updated_at=1787064838.54443 | frequency_hz=70.0
- [2026-08-18 22:54:00] operator / voice_command / voice: increase the tracking speed
  meta: normalized=True
- [2026-08-18 22:53:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064839.7738059 | source=vosk | rms=1204 | updated_at=1787064839.7738059 | frequency_hz=67.2
- [2026-08-18 22:54:01] assistant / spoken_confirmation / voice: Engagement speed is already 100 percent.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-18 22:54:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064840.9636512 | source=vosk | rms=1204 | updated_at=1787064839.7738059 | frequency_hz=67.2
- [2026-08-18 22:54:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064841.2138195 | source=vosk | rms=642 | updated_at=1787064841.2138195 | frequency_hz=68.0
- [2026-08-18 22:54:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064841.7044852 | source=vosk | rms=642 | updated_at=1787064841.2138195 | frequency_hz=68.0
- [2026-08-18 22:54:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064842.025908 | source=vosk | rms=642 | updated_at=1787064841.2138195 | frequency_hz=68.0
- [2026-08-18 22:54:04] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1787064844.2684274 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064844.4539068 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:04] operator / voice_transcript_partial / voice: is already one
  meta: kind=partial | timestamp=1787064844.5107334 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064844.7039208 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064844.9541974 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:04] operator / voice_transcript_partial / voice: is already one hundred percent
  meta: kind=partial | timestamp=1787064844.9701214 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064845.2056 | source=vosk | rms=723 | updated_at=1787064844.245335 | frequency_hz=184.8
- [2026-08-18 22:54:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064845.568802 | source=vosk | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064846.204013 | source=vosk | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:07] operator / voice_transcript_final / voice: is already one hundred percent
  meta: kind=final | timestamp=1787064847.0687013 | source=final | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064847.2155745 | source=vosk | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:07] operator / voice_transcript_partial / voice: is already one hundred percent
  meta: kind=partial | timestamp=1787064847.23978 | source=vosk | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064847.453754 | source=vosk | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:07] operator / voice_transcript_final / voice: gage is already one hundred percent
  meta: kind=final | timestamp=1787064847.7318351 | source=final | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064847.8384411 | source=vosk | rms=1200 | updated_at=1787064845.568802 | frequency_hz=141.1
- [2026-08-18 22:54:13] operator / voice_transcript_partial / voice: good
  meta: kind=partial | timestamp=1787064853.7236662 | source=vosk | rms=1201 | updated_at=1787064853.7046263 | frequency_hz=79.2
- [2026-08-18 22:54:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064853.9554112 | source=vosk | rms=1201 | updated_at=1787064853.9554112 | frequency_hz=79.2
- [2026-08-18 22:54:13] operator / voice_transcript_partial / voice: did you
  meta: kind=partial | timestamp=1787064853.9814632 | source=vosk | rms=1201 | updated_at=1787064853.9554112 | frequency_hz=79.2
- [2026-08-18 22:54:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064854.2052426 | source=vosk | rms=1200 | updated_at=1787064854.2052426 | frequency_hz=79.2
- [2026-08-18 22:54:14] operator / voice_transcript_partial / voice: good you strongly
  meta: kind=partial | timestamp=1787064854.2307866 | source=vosk | rms=1200 | updated_at=1787064854.2052426 | frequency_hz=79.2
- [2026-08-18 22:54:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064854.7036617 | source=vosk | rms=1201 | updated_at=1787064854.7036617 | frequency_hz=79.2
- [2026-08-18 22:54:14] operator / voice_transcript_partial / voice: could you show me the
  meta: kind=partial | timestamp=1787064854.7317286 | source=vosk | rms=1201 | updated_at=1787064854.7036617 | frequency_hz=79.2
- [2026-08-18 22:54:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064854.9739351 | source=vosk | rms=1201 | updated_at=1787064854.9739351 | frequency_hz=79.2
- [2026-08-18 22:54:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064855.2039804 | source=vosk | rms=1200 | updated_at=1787064855.2039804 | frequency_hz=79.2
- [2026-08-18 22:54:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064855.4584658 | source=vosk | rms=1201 | updated_at=1787064855.4584658 | frequency_hz=79.2
- [2026-08-18 22:54:15] operator / voice_transcript_partial / voice: could you show me the presets
  meta: kind=partial | timestamp=1787064855.4840038 | source=vosk | rms=1201 | updated_at=1787064855.4584658 | frequency_hz=79.2
- [2026-08-18 22:54:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064855.704185 | source=vosk | rms=1201 | updated_at=1787064855.704185 | frequency_hz=108.9
- [2026-08-18 22:54:15] operator / voice_transcript_partial / voice: could you show me the presets the
  meta: kind=partial | timestamp=1787064855.731883 | source=vosk | rms=1201 | updated_at=1787064855.704185 | frequency_hz=108.9
- [2026-08-18 22:54:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064855.9553745 | source=vosk | rms=1200 | updated_at=1787064855.9553745 | frequency_hz=97.4
- [2026-08-18 22:54:15] operator / voice_transcript_partial / voice: could you show me the preset stab
  meta: kind=partial | timestamp=1787064855.974404 | source=vosk | rms=1200 | updated_at=1787064855.9553745 | frequency_hz=97.4
- [2026-08-18 22:54:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064856.3977983 | source=vosk | rms=1200 | updated_at=1787064855.9553745 | frequency_hz=97.4
- [2026-08-18 22:54:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064858.7044282 | source=vosk | rms=1207 | updated_at=1787064858.7044282 | frequency_hz=97.4
- [2026-08-18 22:54:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064859.2035708 | source=vosk | rms=1207 | updated_at=1787064858.7044282 | frequency_hz=97.4
- [2026-08-18 22:54:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064860.7050471 | source=vosk | rms=1201 | updated_at=1787064860.7050471 | frequency_hz=274.0
- [2026-08-18 22:54:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064860.9545786 | source=vosk | rms=1079 | updated_at=1787064860.9545786 | frequency_hz=229.9
- [2026-08-18 22:54:21] operator / voice_transcript_final / voice: could you show me the presets tab
  meta: kind=final | timestamp=1787064861.2133355 | source=final | rms=1079 | updated_at=1787064860.9545786 | frequency_hz=229.9
- [2026-08-18 22:54:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064861.317692 | source=vosk | rms=1066 | updated_at=1787064861.317692 | frequency_hz=192.8
- [2026-08-18 22:54:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064862.8486261 | source=vosk | rms=1204 | updated_at=1787064861.703869 | frequency_hz=151.9
- [2026-08-18 22:54:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064863.3435457 | source=vosk | rms=1204 | updated_at=1787064861.703869 | frequency_hz=151.9
- [2026-08-18 22:54:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064868.595429 | source=vosk | rms=1167 | updated_at=1787064867.8442576 | frequency_hz=266.4
- [2026-08-18 22:54:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064891.345004 | source=vosk | rms=346 | updated_at=1787064891.345004 | frequency_hz=266.4
- [2026-08-18 22:54:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064891.8439243 | source=vosk | rms=346 | updated_at=1787064891.345004 | frequency_hz=266.4
- [2026-08-18 22:54:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064896.5945458 | source=vosk | rms=388 | updated_at=1787064896.5945458 | frequency_hz=266.4
- [2026-08-18 22:54:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064897.0936675 | source=vosk | rms=388 | updated_at=1787064896.5945458 | frequency_hz=266.4
- [2026-08-18 22:54:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064897.3576336 | source=vosk | rms=401 | updated_at=1787064897.3576336 | frequency_hz=266.4
- [2026-08-18 22:54:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064897.9112127 | source=vosk | rms=401 | updated_at=1787064897.3576336 | frequency_hz=266.4
- [2026-08-18 22:55:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064900.844941 | source=vosk | rms=401 | updated_at=1787064897.3576336 | frequency_hz=266.4
- [2026-08-18 22:55:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064901.3440166 | source=vosk | rms=401 | updated_at=1787064897.3576336 | frequency_hz=266.4
- [2026-08-18 22:55:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064901.8445365 | source=vosk | rms=249 | updated_at=1787064901.8445365 | frequency_hz=266.4
- [2026-08-18 22:55:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064903.3503163 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064904.0948546 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064904.5945232 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064905.8446803 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064906.3447714 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064907.5945625 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064908.594678 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064909.844606 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064910.5946963 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064911.59479 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064912.3441966 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064912.8441553 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064913.8458345 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064914.343925 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064914.8443244 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064915.5941567 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064916.0946765 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064917.8480973 | source=vosk | rms=256 | updated_at=1787064902.5950127 | frequency_hz=266.4
- [2026-08-18 22:55:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064919.513978 | source=vosk | rms=163 | updated_at=1787064919.0207667 | frequency_hz=266.4
- [2026-08-18 22:55:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064920.2645812 | source=vosk | rms=163 | updated_at=1787064919.0207667 | frequency_hz=266.4
- [2026-08-18 22:55:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064921.7733781 | source=vosk | rms=163 | updated_at=1787064919.0207667 | frequency_hz=266.4
- [2026-08-18 22:55:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064922.0278847 | source=vosk | rms=163 | updated_at=1787064919.0207667 | frequency_hz=266.4
- [2026-08-18 22:55:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064922.7646677 | source=vosk | rms=163 | updated_at=1787064919.0207667 | frequency_hz=266.4
- [2026-08-18 22:55:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064923.2646244 | source=vosk | rms=255 | updated_at=1787064923.2646244 | frequency_hz=266.4
- [2026-08-18 22:55:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064924.514712 | source=vosk | rms=126 | updated_at=1787064923.764478 | frequency_hz=266.4
- [2026-08-18 22:55:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064925.7644205 | source=vosk | rms=126 | updated_at=1787064923.764478 | frequency_hz=266.4
- [2026-08-18 22:55:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064926.2680705 | source=vosk | rms=126 | updated_at=1787064923.764478 | frequency_hz=266.4
- [2026-08-18 22:55:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064926.5140877 | source=vosk | rms=191 | updated_at=1787064926.5140877 | frequency_hz=266.4
- [2026-08-18 22:55:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064928.5141723 | source=vosk | rms=487 | updated_at=1787064927.8026657 | frequency_hz=266.4
- [2026-08-18 22:55:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064929.5147047 | source=vosk | rms=487 | updated_at=1787064927.8026657 | frequency_hz=266.4
- [2026-08-18 22:55:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064930.513991 | source=vosk | rms=487 | updated_at=1787064927.8026657 | frequency_hz=266.4
- [2026-08-18 22:55:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064931.5144737 | source=vosk | rms=487 | updated_at=1787064927.8026657 | frequency_hz=266.4
- [2026-08-18 22:55:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064932.5146494 | source=vosk | rms=487 | updated_at=1787064927.8026657 | frequency_hz=266.4
- [2026-08-18 22:55:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064933.020928 | source=vosk | rms=487 | updated_at=1787064927.8026657 | frequency_hz=266.4
- [2026-08-18 22:55:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064936.5145786 | source=vosk | rms=1207 | updated_at=1787064935.0334659 | frequency_hz=266.4
- [2026-08-18 22:55:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064936.8010862 | source=vosk | rms=1207 | updated_at=1787064935.0334659 | frequency_hz=266.4
- [2026-08-18 22:55:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064937.519619 | source=vosk | rms=147 | updated_at=1787064937.015855 | frequency_hz=266.4
- [2026-08-18 22:55:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064938.2646635 | source=vosk | rms=486 | updated_at=1787064938.2646635 | frequency_hz=266.4
- [2026-08-18 22:55:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064938.7645614 | source=vosk | rms=486 | updated_at=1787064938.2646635 | frequency_hz=266.4
- [2026-08-18 22:55:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064939.5180671 | source=vosk | rms=186 | updated_at=1787064939.5180671 | frequency_hz=266.4
- [2026-08-18 22:55:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064945.51458 | source=vosk | rms=156 | updated_at=1787064944.7724457 | frequency_hz=266.4
- [2026-08-18 22:55:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064945.764212 | source=vosk | rms=507 | updated_at=1787064945.764212 | frequency_hz=266.4
- [2026-08-18 22:55:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064948.514494 | source=vosk | rms=158 | updated_at=1787064947.514745 | frequency_hz=266.4
- [2026-08-18 22:55:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064949.2641037 | source=vosk | rms=158 | updated_at=1787064947.514745 | frequency_hz=266.4
- [2026-08-18 22:55:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064950.5142496 | source=vosk | rms=939 | updated_at=1787064950.0146704 | frequency_hz=266.4
- [2026-08-18 22:55:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064951.0144274 | source=vosk | rms=939 | updated_at=1787064950.0146704 | frequency_hz=266.4
- [2026-08-18 22:55:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064952.5149171 | source=vosk | rms=939 | updated_at=1787064950.0146704 | frequency_hz=266.4
- [2026-08-18 22:55:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064953.5150306 | source=vosk | rms=939 | updated_at=1787064950.0146704 | frequency_hz=266.4
- [2026-08-18 22:55:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064956.7647052 | source=vosk | rms=163 | updated_at=1787064956.2638803 | frequency_hz=266.4
- [2026-08-18 22:55:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064957.764654 | source=vosk | rms=163 | updated_at=1787064956.2638803 | frequency_hz=266.4
- [2026-08-18 22:55:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064959.189761 | source=vosk | rms=310 | updated_at=1787064958.7646148 | frequency_hz=266.4
- [2026-08-18 22:56:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064960.5148919 | source=vosk | rms=329 | updated_at=1787064960.5148919 | frequency_hz=266.4
- [2026-08-18 22:56:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064961.7650774 | source=vosk | rms=329 | updated_at=1787064960.5148919 | frequency_hz=266.4
- [2026-08-18 22:56:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064962.2984655 | source=vosk | rms=260 | updated_at=1787064962.2984655 | frequency_hz=266.4
- [2026-08-18 22:56:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064962.7646177 | source=vosk | rms=260 | updated_at=1787064962.2984655 | frequency_hz=266.4
- [2026-08-18 22:56:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064963.0160086 | source=vosk | rms=193 | updated_at=1787064963.0160086 | frequency_hz=266.4
- [2026-08-18 22:56:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064965.5151372 | source=vosk | rms=242 | updated_at=1787064965.0144908 | frequency_hz=266.4
- [2026-08-18 22:56:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064965.7644153 | source=vosk | rms=242 | updated_at=1787064965.0144908 | frequency_hz=266.4
- [2026-08-18 22:56:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064967.040513 | source=vosk | rms=205 | updated_at=1787064966.5147624 | frequency_hz=266.4
- [2026-08-18 22:56:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064967.2652407 | source=vosk | rms=205 | updated_at=1787064966.5147624 | frequency_hz=266.4
- [2026-08-18 22:56:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064968.2651823 | source=vosk | rms=205 | updated_at=1787064966.5147624 | frequency_hz=266.4
- [2026-08-18 22:56:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064968.5152547 | source=vosk | rms=907 | updated_at=1787064968.5152547 | frequency_hz=266.4
- [2026-08-18 22:56:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064969.2651904 | source=vosk | rms=642 | updated_at=1787064968.764719 | frequency_hz=266.4
- [2026-08-18 22:56:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064969.764558 | source=vosk | rms=395 | updated_at=1787064969.764558 | frequency_hz=266.4
- [2026-08-18 22:56:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064974.5150206 | source=vosk | rms=161 | updated_at=1787064974.0239842 | frequency_hz=266.4
- [2026-08-18 22:56:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064978.7645981 | source=vosk | rms=161 | updated_at=1787064974.0239842 | frequency_hz=266.4
- [2026-08-18 22:56:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064979.2651424 | source=vosk | rms=161 | updated_at=1787064974.0239842 | frequency_hz=266.4
- [2026-08-18 22:56:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064979.764639 | source=vosk | rms=161 | updated_at=1787064974.0239842 | frequency_hz=266.4
- [2026-08-18 22:56:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064981.078763 | source=vosk | rms=836 | updated_at=1787064980.514255 | frequency_hz=266.4
- [2026-08-18 22:56:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064981.575161 | source=vosk | rms=836 | updated_at=1787064980.514255 | frequency_hz=266.4
- [2026-08-18 22:56:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064984.8252711 | source=vosk | rms=167 | updated_at=1787064984.326133 | frequency_hz=266.4
- [2026-08-18 22:56:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064985.5745833 | source=vosk | rms=215 | updated_at=1787064985.5745833 | frequency_hz=266.4
- [2026-08-18 22:56:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064986.0754764 | source=vosk | rms=215 | updated_at=1787064985.5745833 | frequency_hz=266.4
- [2026-08-18 22:56:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064986.325101 | source=vosk | rms=215 | updated_at=1787064985.5745833 | frequency_hz=266.4
- [2026-08-18 22:56:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064989.0745616 | source=vosk | rms=323 | updated_at=1787064988.0751483 | frequency_hz=266.4
- [2026-08-18 22:56:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064989.32472 | source=vosk | rms=330 | updated_at=1787064989.32472 | frequency_hz=266.4
- [2026-08-18 22:56:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787064989.8245168 | source=vosk | rms=330 | updated_at=1787064989.32472 | frequency_hz=266.4
- [2026-08-18 22:56:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787064990.0744588 | source=vosk | rms=184 | updated_at=1787064990.0744588 | frequency_hz=266.4
- [2026-08-18 22:56:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065000.5750802 | source=vosk | rms=209 | updated_at=1787065000.0751061 | frequency_hz=266.4
- [2026-08-18 22:56:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065000.8539746 | source=vosk | rms=227 | updated_at=1787065000.8539746 | frequency_hz=266.4
- [2026-08-18 22:56:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065001.5761142 | source=vosk | rms=227 | updated_at=1787065000.8539746 | frequency_hz=266.4
- [2026-08-18 22:56:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065002.8327627 | source=vosk | rms=721 | updated_at=1787065002.8327627 | frequency_hz=266.4
- [2026-08-18 22:56:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065004.8263803 | source=vosk | rms=160 | updated_at=1787065004.3249714 | frequency_hz=266.4
- [2026-08-18 22:56:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065005.5762877 | source=vosk | rms=523 | updated_at=1787065005.5762877 | frequency_hz=266.4
- [2026-08-18 22:56:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065006.0747821 | source=vosk | rms=523 | updated_at=1787065005.5762877 | frequency_hz=266.4
- [2026-08-18 22:56:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065006.5753047 | source=vosk | rms=523 | updated_at=1787065005.5762877 | frequency_hz=266.4
- [2026-08-18 22:56:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065010.8264618 | source=vosk | rms=1206 | updated_at=1787065010.3253841 | frequency_hz=266.4
- [2026-08-18 22:56:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065011.825063 | source=vosk | rms=464 | updated_at=1787065011.825063 | frequency_hz=266.4
- [2026-08-18 22:56:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065012.325291 | source=vosk | rms=464 | updated_at=1787065011.825063 | frequency_hz=266.4
- [2026-08-18 22:56:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065012.8470771 | source=vosk | rms=464 | updated_at=1787065011.825063 | frequency_hz=266.4
- [2026-08-18 22:56:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065015.0754054 | source=vosk | rms=299 | updated_at=1787065013.8261378 | frequency_hz=266.4
- [2026-08-18 22:56:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065016.5820405 | source=vosk | rms=299 | updated_at=1787065013.8261378 | frequency_hz=266.4
- [2026-08-18 22:56:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065017.0746987 | source=vosk | rms=299 | updated_at=1787065013.8261378 | frequency_hz=266.4
- [2026-08-18 22:56:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065017.575395 | source=vosk | rms=722 | updated_at=1787065017.575395 | frequency_hz=266.4
- [2026-08-18 22:56:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065018.0746875 | source=vosk | rms=722 | updated_at=1787065017.575395 | frequency_hz=266.4
- [2026-08-18 22:57:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065020.575297 | source=vosk | rms=722 | updated_at=1787065017.575395 | frequency_hz=266.4
- [2026-08-18 22:57:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065022.5750263 | source=vosk | rms=484 | updated_at=1787065022.0752056 | frequency_hz=266.4
- [2026-08-18 22:57:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065023.075651 | source=vosk | rms=288 | updated_at=1787065023.075651 | frequency_hz=266.4
- [2026-08-18 22:57:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065024.5811093 | source=vosk | rms=458 | updated_at=1787065023.83388 | frequency_hz=266.4
- [2026-08-18 22:57:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065024.824322 | source=vosk | rms=458 | updated_at=1787065023.83388 | frequency_hz=266.4
- [2026-08-18 22:57:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065027.3263018 | source=vosk | rms=219 | updated_at=1787065026.8450015 | frequency_hz=266.4
- [2026-08-18 22:57:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065028.0751255 | source=vosk | rms=219 | updated_at=1787065026.8450015 | frequency_hz=266.4
- [2026-08-18 22:57:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065033.3255215 | source=vosk | rms=1059 | updated_at=1787065032.8258698 | frequency_hz=266.4
- [2026-08-18 22:57:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065034.8406267 | source=vosk | rms=1204 | updated_at=1787065034.8406267 | frequency_hz=266.4
- [2026-08-18 22:57:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065035.3272204 | source=vosk | rms=1204 | updated_at=1787065034.8406267 | frequency_hz=266.4
- [2026-08-18 22:57:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065036.826415 | source=vosk | rms=1204 | updated_at=1787065034.8406267 | frequency_hz=266.4
- [2026-08-18 22:57:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065037.3249407 | source=vosk | rms=1204 | updated_at=1787065034.8406267 | frequency_hz=266.4
- [2026-08-18 22:57:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065037.574676 | source=vosk | rms=231 | updated_at=1787065037.574676 | frequency_hz=266.4
- [2026-08-18 22:57:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065038.8254027 | source=vosk | rms=269 | updated_at=1787065038.3255868 | frequency_hz=266.4
- [2026-08-18 22:57:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065039.3256552 | source=vosk | rms=220 | updated_at=1787065039.3256552 | frequency_hz=266.4
- [2026-08-18 22:57:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065040.0765765 | source=vosk | rms=220 | updated_at=1787065039.3256552 | frequency_hz=266.4
- [2026-08-18 22:57:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065043.0750775 | source=vosk | rms=220 | updated_at=1787065039.3256552 | frequency_hz=266.4
- [2026-08-18 22:57:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065044.825304 | source=vosk | rms=246 | updated_at=1787065044.3251023 | frequency_hz=266.4
- [2026-08-18 22:57:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065045.324885 | source=vosk | rms=837 | updated_at=1787065045.324885 | frequency_hz=266.4
- [2026-08-18 22:57:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065045.8563905 | source=vosk | rms=837 | updated_at=1787065045.324885 | frequency_hz=266.4
- [2026-08-18 22:57:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065046.3250642 | source=vosk | rms=863 | updated_at=1787065046.3250642 | frequency_hz=266.4
- [2026-08-18 22:57:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065047.3247793 | source=vosk | rms=863 | updated_at=1787065046.3250642 | frequency_hz=266.4
- [2026-08-18 22:57:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065047.8253765 | source=vosk | rms=863 | updated_at=1787065046.3250642 | frequency_hz=266.4
- [2026-08-18 22:57:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065048.3256562 | source=vosk | rms=863 | updated_at=1787065046.3250642 | frequency_hz=266.4
- [2026-08-18 22:57:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065049.8267784 | source=vosk | rms=575 | updated_at=1787065049.8267784 | frequency_hz=266.4
- [2026-08-18 22:57:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065051.0756094 | source=vosk | rms=220 | updated_at=1787065050.5755847 | frequency_hz=266.4
- [2026-08-18 22:57:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065051.5804713 | source=vosk | rms=220 | updated_at=1787065050.5755847 | frequency_hz=266.4
- [2026-08-18 22:57:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065052.5749497 | source=vosk | rms=267 | updated_at=1787065052.0756216 | frequency_hz=266.4
- [2026-08-18 22:57:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065054.075417 | source=vosk | rms=191 | updated_at=1787065054.075417 | frequency_hz=266.4
- [2026-08-18 22:57:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065055.84005 | source=vosk | rms=371 | updated_at=1787065055.0754902 | frequency_hz=266.4
- [2026-08-18 22:57:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065056.0754814 | source=vosk | rms=337 | updated_at=1787065056.0754814 | frequency_hz=266.4
- [2026-08-18 22:57:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065057.075495 | source=vosk | rms=337 | updated_at=1787065056.0754814 | frequency_hz=266.4
- [2026-08-18 22:57:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065057.3266602 | source=vosk | rms=302 | updated_at=1787065057.3266602 | frequency_hz=266.4
- [2026-08-18 22:57:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065057.8266711 | source=vosk | rms=302 | updated_at=1787065057.3266602 | frequency_hz=266.4
- [2026-08-18 22:57:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065058.5753584 | source=vosk | rms=302 | updated_at=1787065057.3266602 | frequency_hz=266.4
- [2026-08-18 22:57:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065059.5749748 | source=vosk | rms=302 | updated_at=1787065057.3266602 | frequency_hz=266.4
- [2026-08-18 22:57:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065060.077366 | source=vosk | rms=786 | updated_at=1787065060.077366 | frequency_hz=266.4
- [2026-08-18 22:57:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065060.8274226 | source=vosk | rms=786 | updated_at=1787065060.077366 | frequency_hz=266.4
- [2026-08-18 22:57:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065061.0777628 | source=vosk | rms=214 | updated_at=1787065061.0777628 | frequency_hz=266.4
- [2026-08-18 22:57:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065064.9729104 | source=vosk | rms=161 | updated_at=1787065064.3250113 | frequency_hz=266.4
- [2026-08-18 22:57:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065065.575147 | source=vosk | rms=199 | updated_at=1787065065.575147 | frequency_hz=266.4
- [2026-08-18 22:57:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065073.075695 | source=vosk | rms=337 | updated_at=1787065072.575403 | frequency_hz=266.4
- [2026-08-18 22:57:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065073.5753887 | source=vosk | rms=271 | updated_at=1787065073.5753887 | frequency_hz=266.4
- [2026-08-18 22:57:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065074.3399243 | source=vosk | rms=271 | updated_at=1787065073.5753887 | frequency_hz=266.4
- [2026-08-18 22:57:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065075.0857532 | source=vosk | rms=271 | updated_at=1787065073.5753887 | frequency_hz=266.4
- [2026-08-18 22:57:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065076.3356671 | source=vosk | rms=271 | updated_at=1787065073.5753887 | frequency_hz=266.4
- [2026-08-18 22:57:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065076.835287 | source=vosk | rms=309 | updated_at=1787065076.835287 | frequency_hz=266.4
- [2026-08-18 22:57:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065077.3356864 | source=vosk | rms=309 | updated_at=1787065076.835287 | frequency_hz=266.4
- [2026-08-18 22:57:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065078.0853634 | source=vosk | rms=418 | updated_at=1787065078.0853634 | frequency_hz=266.4
- [2026-08-18 22:57:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065078.586015 | source=vosk | rms=418 | updated_at=1787065078.0853634 | frequency_hz=266.4
- [2026-08-18 22:57:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065078.8354821 | source=vosk | rms=672 | updated_at=1787065078.8354821 | frequency_hz=266.4
- [2026-08-18 22:57:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065079.586907 | source=vosk | rms=522 | updated_at=1787065079.1070116 | frequency_hz=266.4
- [2026-08-18 22:57:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065079.835804 | source=vosk | rms=541 | updated_at=1787065079.835804 | frequency_hz=266.4
- [2026-08-18 22:58:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065080.3350108 | source=vosk | rms=541 | updated_at=1787065079.835804 | frequency_hz=266.4
- [2026-08-18 22:58:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065082.3355343 | source=vosk | rms=541 | updated_at=1787065079.835804 | frequency_hz=266.4
- [2026-08-18 22:58:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065083.0943134 | source=vosk | rms=236 | updated_at=1787065082.5868096 | frequency_hz=266.4
- [2026-08-18 22:58:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065083.8370595 | source=vosk | rms=236 | updated_at=1787065082.5868096 | frequency_hz=266.4
- [2026-08-18 22:58:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065084.5857208 | source=vosk | rms=236 | updated_at=1787065082.5868096 | frequency_hz=266.4
- [2026-08-18 22:58:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065098.3771152 | source=vosk | rms=721 | updated_at=1787065098.3771152 | frequency_hz=266.4
- [2026-08-18 22:58:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065099.627878 | source=vosk | rms=160 | updated_at=1787065098.627335 | frequency_hz=266.4
- [2026-08-18 22:58:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065102.6275938 | source=vosk | rms=160 | updated_at=1787065098.627335 | frequency_hz=266.4
- [2026-08-18 22:58:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065103.1331487 | source=vosk | rms=160 | updated_at=1787065098.627335 | frequency_hz=266.4
- [2026-08-18 22:58:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065103.8773005 | source=vosk | rms=160 | updated_at=1787065098.627335 | frequency_hz=266.4
- [2026-08-18 22:58:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065104.6273055 | source=vosk | rms=169 | updated_at=1787065104.1280618 | frequency_hz=266.4
- [2026-08-18 22:58:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065104.8773994 | source=vosk | rms=169 | updated_at=1787065104.1280618 | frequency_hz=266.4
- [2026-08-18 22:58:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065105.3776028 | source=vosk | rms=169 | updated_at=1787065104.1280618 | frequency_hz=266.4
- [2026-08-18 22:58:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065108.3777792 | source=vosk | rms=169 | updated_at=1787065104.1280618 | frequency_hz=266.4
- [2026-08-18 22:58:30] operator / voice_transcript_final / voice: truth
  meta: kind=final | timestamp=1787065110.8026268 | source=final | rms=150 | updated_at=1787065109.6551712 | frequency_hz=266.4
- [2026-08-18 22:58:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065110.850471 | source=vosk | rms=150 | updated_at=1787065109.6551712 | frequency_hz=266.4
- [2026-08-18 22:58:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065110.850471 | source=vosk | rms=150 | updated_at=1787065109.6551712 | frequency_hz=266.4
- [2026-08-18 22:58:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065111.6479096 | source=vosk | rms=150 | updated_at=1787065109.6551712 | frequency_hz=266.4
- [2026-08-18 22:58:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065111.8973749 | source=vosk | rms=120 | updated_at=1787065111.8973749 | frequency_hz=266.4
- [2026-08-18 22:58:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065112.6487935 | source=vosk | rms=120 | updated_at=1787065111.8973749 | frequency_hz=266.4
- [2026-08-18 22:58:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065113.6490498 | source=vosk | rms=120 | updated_at=1787065111.8973749 | frequency_hz=266.4
- [2026-08-18 22:58:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065114.1479769 | source=vosk | rms=120 | updated_at=1787065111.8973749 | frequency_hz=266.4
- [2026-08-18 22:58:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065114.681792 | source=vosk | rms=120 | updated_at=1787065111.8973749 | frequency_hz=266.4
- [2026-08-18 22:58:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065116.397383 | source=vosk | rms=140 | updated_at=1787065115.8975713 | frequency_hz=266.4
- [2026-08-18 22:58:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065116.656501 | source=vosk | rms=140 | updated_at=1787065115.8975713 | frequency_hz=266.4
- [2026-08-18 22:58:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065118.1477492 | source=vosk | rms=140 | updated_at=1787065115.8975713 | frequency_hz=266.4
- [2026-08-18 22:58:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065118.399186 | source=vosk | rms=140 | updated_at=1787065115.8975713 | frequency_hz=266.4
- [2026-08-18 22:58:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065119.1504123 | source=vosk | rms=140 | updated_at=1787065115.8975713 | frequency_hz=266.4
- [2026-08-18 22:58:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065119.6493485 | source=vosk | rms=999 | updated_at=1787065119.6493485 | frequency_hz=266.4
- [2026-08-18 22:58:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065121.1472826 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065121.4387922 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065122.6490312 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065124.148028 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065124.7056699 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065125.6489913 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065126.148341 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065129.648192 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065131.3980982 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065131.649503 | source=vosk | rms=316 | updated_at=1787065120.3974762 | frequency_hz=266.4
- [2026-08-18 22:58:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065134.9114614 | source=vosk | rms=168 | updated_at=1787065133.8981328 | frequency_hz=266.4
- [2026-08-18 22:58:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065136.3976605 | source=vosk | rms=168 | updated_at=1787065133.8981328 | frequency_hz=266.4
- [2026-08-18 22:58:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065136.8977115 | source=vosk | rms=168 | updated_at=1787065133.8981328 | frequency_hz=266.4
- [2026-08-18 22:58:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065138.3974717 | source=vosk | rms=328 | updated_at=1787065138.3974717 | frequency_hz=266.4
- [2026-08-18 22:58:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065139.8979607 | source=vosk | rms=140 | updated_at=1787065139.3980458 | frequency_hz=266.4
- [2026-08-18 22:59:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065140.148074 | source=vosk | rms=140 | updated_at=1787065139.3980458 | frequency_hz=266.4
- [2026-08-18 22:59:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065141.1481447 | source=vosk | rms=140 | updated_at=1787065139.3980458 | frequency_hz=266.4
- [2026-08-18 22:59:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065141.6476078 | source=vosk | rms=166 | updated_at=1787065141.6476078 | frequency_hz=266.4
- [2026-08-18 22:59:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065142.1471498 | source=vosk | rms=166 | updated_at=1787065141.6476078 | frequency_hz=266.4
- [2026-08-18 22:59:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065145.1477036 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065146.399874 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065146.8994298 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065147.897913 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065148.3979213 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065148.8983755 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065155.1483796 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065156.397925 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065160.8986835 | source=vosk | rms=277 | updated_at=1787065145.1477036 | frequency_hz=266.4
- [2026-08-18 22:59:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065161.647874 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065162.6490986 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065163.1519344 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065168.3986685 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065169.1479445 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065169.3992805 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065169.9093053 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065171.4000945 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065171.949093 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065174.9112275 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065175.3978803 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065178.3992872 | source=vosk | rms=145 | updated_at=1787065161.147998 | frequency_hz=266.4
- [2026-08-18 22:59:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065179.148197 | source=vosk | rms=200 | updated_at=1787065178.648234 | frequency_hz=266.4
- [2026-08-18 22:59:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065188.398826 | source=vosk | rms=1200 | updated_at=1787065188.398826 | frequency_hz=266.4
- [2026-08-18 22:59:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065190.6918652 | source=vosk | rms=134 | updated_at=1787065190.1486902 | frequency_hz=266.4
- [2026-08-18 22:59:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065192.1477365 | source=vosk | rms=134 | updated_at=1787065190.1486902 | frequency_hz=266.4
- [2026-08-18 22:59:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065192.649274 | source=vosk | rms=134 | updated_at=1787065190.1486902 | frequency_hz=266.4
- [2026-08-18 22:59:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065192.8985896 | source=vosk | rms=134 | updated_at=1787065190.1486902 | frequency_hz=266.4
- [2026-08-18 22:59:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065193.6548848 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065202.6483357 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065203.1486044 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065206.3997102 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065206.8978524 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065210.6482112 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065211.1486924 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065212.6494725 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065220.3985648 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065222.1493802 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065223.648871 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065224.6483574 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065225.1496987 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065227.1486835 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065228.1805112 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065228.897976 | source=vosk | rms=173 | updated_at=1787065193.148271 | frequency_hz=266.4
- [2026-08-18 23:00:30] operator / voice_transcript_final / voice: top
  meta: kind=final | timestamp=1787065230.6307456 | source=final | rms=128 | updated_at=1787065229.8994496 | frequency_hz=266.4
- [2026-08-18 23:00:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065230.6647527 | source=vosk | rms=139 | updated_at=1787065230.6647527 | frequency_hz=266.4
- [2026-08-18 23:00:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065232.172973 | source=vosk | rms=125 | updated_at=1787065231.1653988 | frequency_hz=266.4
- [2026-08-18 23:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065232.3983457 | source=vosk | rms=125 | updated_at=1787065231.1653988 | frequency_hz=266.4
- [2026-08-18 23:00:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065233.8983085 | source=vosk | rms=125 | updated_at=1787065231.1653988 | frequency_hz=266.4
- [2026-08-18 23:00:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065237.3983948 | source=vosk | rms=125 | updated_at=1787065231.1653988 | frequency_hz=266.4
- [2026-08-18 23:00:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065245.8981998 | source=vosk | rms=207 | updated_at=1787065245.3984332 | frequency_hz=266.4
- [2026-08-18 23:00:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065246.8986151 | source=vosk | rms=145 | updated_at=1787065246.8986151 | frequency_hz=266.4
- [2026-08-18 23:00:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065247.656856 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065248.8990164 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065249.399689 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065249.6488695 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065250.4698193 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065251.8985813 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065252.3985097 | source=vosk | rms=134 | updated_at=1787065247.1634076 | frequency_hz=266.4
- [2026-08-18 23:00:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065255.3981256 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:00:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065256.1303656 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065274.6388328 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065275.149107 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065275.9007006 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065276.9200497 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065277.3988178 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065278.3984659 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065281.1486976 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065281.9061184 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065291.3994312 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065291.8992076 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065293.4024475 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065293.9069648 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065297.1537228 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065298.1484118 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065298.6488984 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065299.1486504 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065301.3992043 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065303.648942 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065304.1486757 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065305.1857796 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065305.3994036 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065306.1490366 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065306.9002557 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:01:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065309.149298 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065320.1492255 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065320.6484869 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065325.1494515 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065325.6486745 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065328.8994803 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065329.6490827 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065334.4428167 | source=vosk | rms=1202 | updated_at=1787065255.3981256 | frequency_hz=266.4
- [2026-08-18 23:02:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065335.1486387 | source=vosk | rms=130 | updated_at=1787065334.6491125 | frequency_hz=266.4
- [2026-08-18 23:02:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065336.6488273 | source=vosk | rms=130 | updated_at=1787065334.6491125 | frequency_hz=266.4
- [2026-08-18 23:02:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065337.1857061 | source=vosk | rms=130 | updated_at=1787065334.6491125 | frequency_hz=266.4
- [2026-08-18 23:02:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065338.3989878 | source=vosk | rms=130 | updated_at=1787065334.6491125 | frequency_hz=266.4
- [2026-08-18 23:02:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065339.8108056 | source=vosk | rms=130 | updated_at=1787065334.6491125 | frequency_hz=266.4
- [2026-08-18 23:02:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065348.034665 | source=vosk | rms=130 | updated_at=1787065334.6491125 | frequency_hz=266.4
- [2026-08-18 23:02:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065348.784634 | source=vosk | rms=186 | updated_at=1787065348.2847035 | frequency_hz=266.4
- [2026-08-18 23:02:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065350.3418822 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065350.784896 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065360.784653 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065363.7834017 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065364.7834866 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065365.286381 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065368.7840362 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065369.2854524 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065370.0335279 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065370.5346677 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065372.0347188 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065372.7835903 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065375.0341425 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065376.0336347 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065376.784716 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065377.7852852 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:02:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065378.534866 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065380.2842233 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065380.535255 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065381.7897174 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065382.0349 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065384.1238217 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065390.05314 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065391.0535815 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065391.3021865 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065392.5521164 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065393.0526767 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065393.5537994 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065393.8126903 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065398.3025963 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065398.8025064 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065401.552748 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065406.0556736 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065407.5522428 | source=vosk | rms=202 | updated_at=1787065350.3418822 | frequency_hz=266.4
- [2026-08-18 23:03:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065413.0526938 | source=vosk | rms=189 | updated_at=1787065413.0526938 | frequency_hz=266.4
- [2026-08-18 23:03:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065415.3020873 | source=vosk | rms=205 | updated_at=1787065414.8028662 | frequency_hz=266.4
- [2026-08-18 23:03:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065416.3025093 | source=vosk | rms=205 | updated_at=1787065414.8028662 | frequency_hz=266.4
- [2026-08-18 23:03:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065416.8058116 | source=vosk | rms=205 | updated_at=1787065414.8028662 | frequency_hz=266.4
- [2026-08-18 23:03:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065419.0529914 | source=vosk | rms=205 | updated_at=1787065414.8028662 | frequency_hz=266.4
- [2026-08-18 23:03:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065420.352466 | source=vosk | rms=205 | updated_at=1787065414.8028662 | frequency_hz=266.4
- [2026-08-18 23:03:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065421.852722 | source=vosk | rms=180 | updated_at=1787065421.852722 | frequency_hz=266.4
- [2026-08-18 23:03:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065423.1347735 | source=vosk | rms=180 | updated_at=1787065421.852722 | frequency_hz=266.4
- [2026-08-18 23:03:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065432.1049218 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:03:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065432.852796 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:03:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065433.106637 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:03:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065433.602457 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:03:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065439.6026301 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:04:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065440.1050212 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:04:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065441.8529346 | source=vosk | rms=158 | updated_at=1787065432.1049218 | frequency_hz=266.4
- [2026-08-18 23:04:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065442.853081 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065444.9896011 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065445.5172884 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065445.7329555 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065446.2436101 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065446.7596102 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065448.1643627 | source=vosk | rms=184 | updated_at=1787065442.1026404 | frequency_hz=266.4
- [2026-08-18 23:04:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065461.532116 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065462.031433 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065462.2823315 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065463.2830138 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065471.8916385 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065472.392136 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065472.6424427 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065473.1445968 | source=vosk | rms=184 | updated_at=1787065461.532116 | frequency_hz=266.4
- [2026-08-18 23:04:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065473.8954434 | source=vosk | rms=176 | updated_at=1787065473.8954434 | frequency_hz=266.4
- [2026-08-18 23:04:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065476.9725711 | source=vosk | rms=182 | updated_at=1787065476.227958 | frequency_hz=266.4
- [2026-08-18 23:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065477.722391 | source=vosk | rms=182 | updated_at=1787065476.227958 | frequency_hz=266.4
- [2026-08-18 23:04:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065480.9717312 | source=vosk | rms=154 | updated_at=1787065480.4850135 | frequency_hz=266.4
- [2026-08-18 23:04:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065481.472016 | source=vosk | rms=445 | updated_at=1787065481.472016 | frequency_hz=266.4
- [2026-08-18 23:04:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065484.4715881 | source=vosk | rms=364 | updated_at=1787065483.7219486 | frequency_hz=266.4
- [2026-08-18 23:04:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065486.2235165 | source=vosk | rms=364 | updated_at=1787065483.7219486 | frequency_hz=266.4
- [2026-08-18 23:04:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065494.723183 | source=vosk | rms=453 | updated_at=1787065493.222135 | frequency_hz=266.4
- [2026-08-18 23:04:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065494.9973574 | source=vosk | rms=453 | updated_at=1787065493.222135 | frequency_hz=266.4
- [2026-08-18 23:04:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065496.4719136 | source=vosk | rms=120 | updated_at=1787065495.972081 | frequency_hz=266.4
- [2026-08-18 23:04:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065497.4718904 | source=vosk | rms=187 | updated_at=1787065497.4718904 | frequency_hz=266.4
- [2026-08-18 23:04:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065497.9723444 | source=vosk | rms=187 | updated_at=1787065497.4718904 | frequency_hz=266.4
- [2026-08-18 23:04:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065498.2222984 | source=vosk | rms=293 | updated_at=1787065498.2222984 | frequency_hz=266.4
- [2026-08-18 23:04:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065498.7232609 | source=vosk | rms=293 | updated_at=1787065498.2222984 | frequency_hz=266.4
- [2026-08-18 23:04:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065499.471703 | source=vosk | rms=293 | updated_at=1787065498.2222984 | frequency_hz=266.4
- [2026-08-18 23:05:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065503.2232246 | source=vosk | rms=181 | updated_at=1787065502.7219987 | frequency_hz=266.4
- [2026-08-18 23:05:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065503.7301478 | source=vosk | rms=263 | updated_at=1787065503.7301478 | frequency_hz=266.4
- [2026-08-18 23:05:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065504.2232883 | source=vosk | rms=263 | updated_at=1787065503.7301478 | frequency_hz=266.4
- [2026-08-18 23:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065504.4724095 | source=vosk | rms=345 | updated_at=1787065504.4724095 | frequency_hz=266.4
- [2026-08-18 23:05:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065504.972814 | source=vosk | rms=345 | updated_at=1787065504.4724095 | frequency_hz=266.4
- [2026-08-18 23:05:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065506.9726467 | source=vosk | rms=163 | updated_at=1787065506.9726467 | frequency_hz=266.4
- [2026-08-18 23:05:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065507.7234507 | source=vosk | rms=175 | updated_at=1787065507.222049 | frequency_hz=266.4
- [2026-08-18 23:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065508.9724438 | source=vosk | rms=175 | updated_at=1787065507.222049 | frequency_hz=266.4
- [2026-08-18 23:05:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065510.4718049 | source=vosk | rms=228 | updated_at=1787065509.7226949 | frequency_hz=266.4
- [2026-08-18 23:05:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065513.7235012 | source=vosk | rms=328 | updated_at=1787065513.7235012 | frequency_hz=266.4
- [2026-08-18 23:05:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065514.2248464 | source=vosk | rms=328 | updated_at=1787065513.7235012 | frequency_hz=266.4
- [2026-08-18 23:05:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065514.4726005 | source=vosk | rms=328 | updated_at=1787065513.7235012 | frequency_hz=266.4
- [2026-08-18 23:05:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065518.3007631 | source=vosk | rms=156 | updated_at=1787065517.7942033 | frequency_hz=266.4
- [2026-08-18 23:05:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065518.8010294 | source=vosk | rms=137 | updated_at=1787065518.8010294 | frequency_hz=266.4
- [2026-08-18 23:05:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065519.8112228 | source=vosk | rms=326 | updated_at=1787065519.0510113 | frequency_hz=266.4
- [2026-08-18 23:05:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065520.0523057 | source=vosk | rms=163 | updated_at=1787065520.0523057 | frequency_hz=266.4
- [2026-08-18 23:05:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065520.5515459 | source=vosk | rms=163 | updated_at=1787065520.0523057 | frequency_hz=266.4
- [2026-08-18 23:05:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065522.3196642 | source=vosk | rms=224 | updated_at=1787065522.3196642 | frequency_hz=266.4
- [2026-08-18 23:05:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065523.8014061 | source=vosk | rms=232 | updated_at=1787065523.301075 | frequency_hz=266.4
- [2026-08-18 23:05:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065524.6160328 | source=vosk | rms=232 | updated_at=1787065523.301075 | frequency_hz=266.4
- [2026-08-18 23:05:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065525.1280067 | source=vosk | rms=232 | updated_at=1787065523.301075 | frequency_hz=266.4
- [2026-08-18 23:05:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065525.62843 | source=vosk | rms=232 | updated_at=1787065523.301075 | frequency_hz=266.4
- [2026-08-18 23:05:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065526.1287446 | source=vosk | rms=232 | updated_at=1787065523.301075 | frequency_hz=266.4
- [2026-08-18 23:05:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065527.3784785 | source=vosk | rms=185 | updated_at=1787065527.3784785 | frequency_hz=266.4
- [2026-08-18 23:05:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065531.628754 | source=vosk | rms=839 | updated_at=1787065531.1286128 | frequency_hz=266.4
- [2026-08-18 23:05:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065532.1284997 | source=vosk | rms=839 | updated_at=1787065531.1286128 | frequency_hz=266.4
- [2026-08-18 23:05:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065534.138512 | source=vosk | rms=138 | updated_at=1787065533.638797 | frequency_hz=266.4
- [2026-08-18 23:05:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065534.3887184 | source=vosk | rms=138 | updated_at=1787065533.638797 | frequency_hz=266.4
- [2026-08-18 23:05:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065536.1388514 | source=vosk | rms=444 | updated_at=1787065535.6403902 | frequency_hz=266.4
- [2026-08-18 23:05:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065536.393473 | source=vosk | rms=444 | updated_at=1787065535.6403902 | frequency_hz=266.4
- [2026-08-18 23:05:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065539.1386874 | source=vosk | rms=458 | updated_at=1787065538.1515563 | frequency_hz=266.4
- [2026-08-18 23:05:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065539.3887267 | source=vosk | rms=213 | updated_at=1787065539.3887267 | frequency_hz=266.4
- [2026-08-18 23:05:42] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787065542.653826 | source=vosk | rms=212 | updated_at=1787065542.6392274 | frequency_hz=266.4
- [2026-08-18 23:05:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065543.138891 | source=vosk | rms=185 | updated_at=1787065543.138891 | frequency_hz=266.4
- [2026-08-18 23:05:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065543.3888166 | source=vosk | rms=185 | updated_at=1787065543.138891 | frequency_hz=266.4
- [2026-08-18 23:05:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065543.8886864 | source=vosk | rms=185 | updated_at=1787065543.138891 | frequency_hz=266.4
- [2026-08-18 23:05:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065544.1383324 | source=vosk | rms=280 | updated_at=1787065544.1383324 | frequency_hz=266.4
- [2026-08-18 23:05:44] operator / voice_transcript_final / voice: thanks
  meta: kind=final | timestamp=1787065544.3169017 | source=final | rms=280 | updated_at=1787065544.1383324 | frequency_hz=266.4
- [2026-08-18 23:05:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065544.6387799 | source=vosk | rms=280 | updated_at=1787065544.1383324 | frequency_hz=266.4
- [2026-08-18 23:05:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065545.1381683 | source=vosk | rms=408 | updated_at=1787065545.1381683 | frequency_hz=266.4
- [2026-08-18 23:05:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065545.8880355 | source=vosk | rms=408 | updated_at=1787065545.1381683 | frequency_hz=266.4
- [2026-08-18 23:05:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065546.1418543 | source=vosk | rms=433 | updated_at=1787065546.1418543 | frequency_hz=266.4
- [2026-08-18 23:05:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065546.8886907 | source=vosk | rms=172 | updated_at=1787065546.3888226 | frequency_hz=266.4
- [2026-08-18 23:05:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065550.398206 | source=vosk | rms=756 | updated_at=1787065550.398206 | frequency_hz=266.4
- [2026-08-18 23:05:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065550.8983953 | source=vosk | rms=756 | updated_at=1787065550.398206 | frequency_hz=266.4
- [2026-08-18 23:05:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065557.1495388 | source=vosk | rms=1200 | updated_at=1787065557.1495388 | frequency_hz=266.4
- [2026-08-18 23:05:59] operator / voice_transcript_partial / voice: earlier
  meta: kind=partial | timestamp=1787065559.665119 | source=vosk | rms=2809 | updated_at=1787065559.6487417 | frequency_hz=249.3
- [2026-08-18 23:05:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065559.8982956 | source=vosk | rms=1165 | updated_at=1787065559.8982956 | frequency_hz=220.8
- [2026-08-18 23:06:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065560.148235 | source=vosk | rms=1200 | updated_at=1787065560.148235 | frequency_hz=178.5
- [2026-08-18 23:06:00] operator / voice_transcript_final / voice: earlier
  meta: kind=final | timestamp=1787065560.3881955 | source=final | rms=1200 | updated_at=1787065560.148235 | frequency_hz=178.5
- [2026-08-18 23:06:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065560.4339352 | source=vosk | rms=737 | updated_at=1787065560.4339352 | frequency_hz=149.6
- [2026-08-18 23:06:02] operator / voice_transcript_partial / voice: close
  meta: kind=partial | timestamp=1787065562.9238245 | source=vosk | rms=3008 | updated_at=1787065562.8980632 | frequency_hz=205.9
- [2026-08-18 23:06:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065563.1480932 | source=vosk | rms=1201 | updated_at=1787065563.1480932 | frequency_hz=205.9
- [2026-08-18 23:06:03] operator / voice_transcript_partial / voice: close to
  meta: kind=partial | timestamp=1787065563.162167 | source=vosk | rms=1201 | updated_at=1787065563.1480932 | frequency_hz=205.9
- [2026-08-18 23:06:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065563.398196 | source=vosk | rms=1200 | updated_at=1787065563.398196 | frequency_hz=205.9
- [2026-08-18 23:06:03] operator / voice_transcript_partial / voice: close the
  meta: kind=partial | timestamp=1787065563.4097812 | source=vosk | rms=1200 | updated_at=1787065563.398196 | frequency_hz=205.9
- [2026-08-18 23:06:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065563.649646 | source=vosk | rms=1324 | updated_at=1787065563.6480367 | frequency_hz=205.9
- [2026-08-18 23:06:03] operator / voice_transcript_partial / voice: close the smart
  meta: kind=partial | timestamp=1787065563.6584244 | source=vosk | rms=1324 | updated_at=1787065563.6480367 | frequency_hz=205.9
- [2026-08-18 23:06:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065563.8988643 | source=vosk | rms=1572 | updated_at=1787065563.8988643 | frequency_hz=201.7
- [2026-08-18 23:06:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065564.1482093 | source=vosk | rms=1201 | updated_at=1787065564.1482093 | frequency_hz=182.9
- [2026-08-18 23:06:04] operator / voice_transcript_partial / voice: close the smart sentry
  meta: kind=partial | timestamp=1787065564.1558187 | source=vosk | rms=1201 | updated_at=1787065564.1482093 | frequency_hz=182.9
- [2026-08-18 23:06:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065564.399549 | source=vosk | rms=1147 | updated_at=1787065564.399549 | frequency_hz=145.5
- [2026-08-18 23:06:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065564.6558259 | source=vosk | rms=580 | updated_at=1787065564.6558259 | frequency_hz=115.6
- [2026-08-18 23:06:04] operator / voice_transcript_final / voice: close the app
  meta: kind=final | timestamp=1787065564.6743867 | source=final | rms=580 | updated_at=1787065564.6558259 | frequency_hz=115.6
- [2026-08-18 23:06:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065564.9173121 | source=vosk | rms=750 | updated_at=1787065564.9173121 | frequency_hz=104.5
- [2026-08-18 23:06:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065573.4402869 | source=vosk | rms=633 | updated_at=1787065572.6737356 | frequency_hz=253.8
- [2026-08-18 23:06:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065573.923669 | source=vosk | rms=633 | updated_at=1787065572.6737356 | frequency_hz=253.8
- [2026-08-18 23:06:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787065575.0683613 | source=vosk | rms=609 | updated_at=1787065574.5482895 | frequency_hz=253.8
- [2026-08-18 23:06:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787065575.818255 | source=vosk | rms=609 | updated_at=1787065574.5482895 | frequency_hz=253.8

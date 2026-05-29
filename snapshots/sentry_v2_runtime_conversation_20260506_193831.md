# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 19:38:31
- Entries: 250
- Roles: {'assistant': 14, 'system': 1, 'operator': 235}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 2, 'voice_status': 1, 'spoken_confirmation': 9, 'voice_transcript_final': 25, 'voice_transcript_partial': 188, 'voice_command': 22, 'spoken_reply': 1}
- Channels: {'text': 4, 'voice': 246}
- Latest operator request: elion
- Latest assistant message: Yes? I am listening.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 19:30:12] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 19:30:12] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 19:30:13] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778067013.4908364 | source=vosk
- [2026-05-06 19:30:51] assistant / spoken_confirmation / voice: Good to go. Ask your question naturally, or say Elion first if you want a dedicated conversation window.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:30:58] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1778067058.819335 | source=final
- [2026-05-06 19:30:58] operator / voice_transcript_partial / voice: want to
  meta: kind=partial | timestamp=1778067058.83737 | source=vosk
- [2026-05-06 19:30:59] operator / voice_transcript_partial / voice: want to detection
  meta: kind=partial | timestamp=1778067059.0731232 | source=vosk
- [2026-05-06 19:30:59] operator / voice_transcript_partial / voice: want to
  meta: kind=partial | timestamp=1778067059.3267345 | source=vosk
- [2026-05-06 19:30:59] operator / voice_transcript_partial / voice: want to rest
  meta: kind=partial | timestamp=1778067059.572799 | source=vosk
- [2026-05-06 19:30:59] operator / voice_transcript_partial / voice: conversation
  meta: kind=partial | timestamp=1778067059.8226395 | source=vosk
- [2026-05-06 19:31:00] operator / voice_transcript_partial / voice: conversation window
  meta: kind=partial | timestamp=1778067060.0749888 | source=vosk
- [2026-05-06 19:31:00] operator / voice_transcript_partial / voice: conversation window shortcuts
  meta: kind=partial | timestamp=1778067060.3239093 | source=vosk
- [2026-05-06 19:31:01] operator / voice_transcript_partial / voice: conversation window who are you
  meta: kind=partial | timestamp=1778067061.3213935 | source=vosk
- [2026-05-06 19:31:02] operator / voice_transcript_final / voice: want to conversation window who are you
  meta: kind=final | timestamp=1778067062.2129521 | source=final
- [2026-05-06 19:31:02] operator / voice_command / voice: want to conversation window who are you
  meta: normalized=True
- [2026-05-06 19:31:02] assistant / assistant_prompt / text: I am Elion Mesk, or Elion for short, the AI assistant voice for Smart Sentry. I can talk with you normally, help with Smart Sentry questions, and switch into diagnostics when you ask.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 19:31:02] assistant / spoken_reply / voice: I am Elion Mesk, or Elion for short, the AI assistant voice for Smart Sentry. I can talk with you normally, help with Smart Sentry questions, and switch into diagnostics when you ask.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-06 19:31:14] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry
  meta: kind=partial | timestamp=1778067074.3837023 | source=vosk
- [2026-05-06 19:31:14] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question
  meta: kind=partial | timestamp=1778067074.883483 | source=vosk
- [2026-05-06 19:31:15] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question in switching
  meta: kind=partial | timestamp=1778067075.6390007 | source=vosk
- [2026-05-06 19:31:15] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question in switching disabled
  meta: kind=partial | timestamp=1778067075.8808932 | source=vosk
- [2026-05-06 19:31:16] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question in switching to
  meta: kind=partial | timestamp=1778067076.130769 | source=vosk
- [2026-05-06 19:31:16] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question in switching to diagnostics
  meta: kind=partial | timestamp=1778067076.381427 | source=vosk
- [2026-05-06 19:31:17] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question in switching to diagnostics a lion
  meta: kind=partial | timestamp=1778067077.3892217 | source=vosk
- [2026-05-06 19:31:17] operator / voice_transcript_partial / voice: aileen turn overlay help smart sentry question in switching to diagnostics microphone anomaly
  meta: kind=partial | timestamp=1778067077.641577 | source=vosk
- [2026-05-06 19:31:18] operator / voice_transcript_final / voice: ai turn overlay help smart sentry question in switching to diagnostics on
  meta: kind=final | timestamp=1778067078.3134296 | source=final
- [2026-05-06 19:31:22] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1778067082.1517248 | source=vosk
- [2026-05-06 19:31:22] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1778067082.4004436 | source=vosk
- [2026-05-06 19:31:23] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778067083.4106548 | source=final
- [2026-05-06 19:31:23] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 19:31:24] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:31:38] operator / voice_transcript_partial / voice: ask another question manual inversion
  meta: kind=partial | timestamp=1778067098.3181813 | source=vosk
- [2026-05-06 19:31:38] operator / voice_transcript_partial / voice: ask another question manual hey
  meta: kind=partial | timestamp=1778067098.5544665 | source=vosk
- [2026-05-06 19:31:39] operator / voice_transcript_final / voice: ask another question manual inversion
  meta: kind=final | timestamp=1778067099.506516 | source=final
- [2026-05-06 19:31:41] operator / voice_transcript_partial / voice: training
  meta: kind=partial | timestamp=1778067101.2986236 | source=vosk
- [2026-05-06 19:31:41] operator / voice_transcript_partial / voice: tuning changes
  meta: kind=partial | timestamp=1778067101.5448744 | source=vosk
- [2026-05-06 19:31:41] operator / voice_transcript_partial / voice: turn the change your
  meta: kind=partial | timestamp=1778067101.7935135 | source=vosk
- [2026-05-06 19:31:42] operator / voice_transcript_partial / voice: turn the change your voice
  meta: kind=partial | timestamp=1778067102.0445898 | source=vosk
- [2026-05-06 19:31:43] operator / voice_transcript_final / voice: turn the change your voice
  meta: kind=final | timestamp=1778067103.1697452 | source=final
- [2026-05-06 19:31:43] operator / voice_command / voice: turn the change your voice
  meta: normalized=True
- [2026-05-06 19:31:44] assistant / spoken_confirmation / voice: Sure. I can do that. Do you want Indian voice or Russian voice?
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 19:31:48] operator / voice_transcript_partial / voice: local matching pir guard system
  meta: kind=partial | timestamp=1778067108.0749142 | source=vosk
- [2026-05-06 19:31:48] operator / voice_transcript_partial / voice: local matching pir guard system recognition
  meta: kind=partial | timestamp=1778067108.0910661 | source=vosk
- [2026-05-06 19:31:49] operator / voice_transcript_final / voice: local matching no guard system recognition
  meta: kind=final | timestamp=1778067109.2602916 | source=final
- [2026-05-06 19:31:59] operator / voice_transcript_partial / voice: change your voice acoustic guard detection e zone sound output voice disable the buzzer
  meta: kind=partial | timestamp=1778067119.0593152 | source=vosk
- [2026-05-06 19:31:59] operator / voice_transcript_partial / voice: change your voice acoustic guard detection e zone sound output voice disable the buzzer in
  meta: kind=partial | timestamp=1778067119.5498693 | source=vosk
- [2026-05-06 19:32:00] operator / voice_transcript_partial / voice: change your voice acoustic guard detection e zone sound output voice disable the buzzer in current status
  meta: kind=partial | timestamp=1778067120.2947168 | source=vosk
- [2026-05-06 19:32:00] operator / voice_transcript_partial / voice: change your voice acoustic guard detection e zone sound output voice disable the buzzer in turn stay guard
  meta: kind=partial | timestamp=1778067120.8011823 | source=vosk
- [2026-05-06 19:32:01] operator / voice_transcript_partial / voice: change your voice acoustic guard detection e zone sound output voice disable the buzzer in turn stay guarding mode
  meta: kind=partial | timestamp=1778067121.04425 | source=vosk
- [2026-05-06 19:32:02] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:32:03] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:32:06] operator / voice_transcript_partial / voice: yes ai analysis
  meta: kind=partial | timestamp=1778067126.3239307 | source=vosk
- [2026-05-06 19:32:06] operator / voice_transcript_partial / voice: yes i have listening
  meta: kind=partial | timestamp=1778067126.8287728 | source=vosk
- [2026-05-06 19:32:07] operator / voice_transcript_final / voice: yes ai on listening
  meta: kind=final | timestamp=1778067127.4762821 | source=final
- [2026-05-06 19:32:08] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778067128.0768223 | source=vosk
- [2026-05-06 19:32:08] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778067128.333103 | source=vosk
- [2026-05-06 19:32:09] operator / voice_transcript_final / voice: change your voice
  meta: kind=final | timestamp=1778067129.445594 | source=final
- [2026-05-06 19:32:09] operator / voice_command / voice: change your voice
  meta: normalized=True
- [2026-05-06 19:32:11] assistant / spoken_confirmation / voice: Sure. I can do that. Do you want Indian voice or Russian voice?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:32:16] operator / voice_transcript_partial / voice: show are you do that the one human voice
  meta: kind=partial | timestamp=1778067136.2463155 | source=vosk
- [2026-05-06 19:32:16] operator / voice_transcript_partial / voice: show are you do that the one human voice running
  meta: kind=partial | timestamp=1778067136.2543418 | source=vosk
- [2026-05-06 19:32:16] operator / voice_transcript_partial / voice: show are you do that the one human voice russian dmitry
  meta: kind=partial | timestamp=1778067136.267953 | source=vosk
- [2026-05-06 19:32:16] operator / voice_transcript_partial / voice: show are you do that the one human voice russian
  meta: kind=partial | timestamp=1778067136.5102663 | source=vosk
- [2026-05-06 19:32:16] operator / voice_transcript_partial / voice: show are you do that the one human voice russian dmitry
  meta: kind=partial | timestamp=1778067136.759049 | source=vosk
- [2026-05-06 19:32:17] operator / voice_transcript_final / voice: show are you do that the one human voice russian rest
  meta: kind=final | timestamp=1778067137.4162693 | source=final
- [2026-05-06 19:32:18] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778067138.6083732 | source=vosk
- [2026-05-06 19:32:19] operator / voice_transcript_partial / voice: changes to anything
  meta: kind=partial | timestamp=1778067139.007348 | source=vosk
- [2026-05-06 19:32:19] operator / voice_transcript_partial / voice: changes to elliot
  meta: kind=partial | timestamp=1778067139.2552633 | source=vosk
- [2026-05-06 19:32:19] operator / voice_transcript_partial / voice: changes to elliot voice
  meta: kind=partial | timestamp=1778067139.5151591 | source=vosk
- [2026-05-06 19:32:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:32:22] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:32:27] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778067147.749861 | source=vosk
- [2026-05-06 19:32:27] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778067147.9856324 | source=vosk
- [2026-05-06 19:32:28] operator / voice_transcript_partial / voice: change your voice what is
  meta: kind=partial | timestamp=1778067148.3727813 | source=vosk
- [2026-05-06 19:32:28] operator / voice_transcript_partial / voice: change your voice buzzer in human
  meta: kind=partial | timestamp=1778067148.5501115 | source=vosk
- [2026-05-06 19:32:28] operator / voice_transcript_partial / voice: change your voice buzzer in human voice
  meta: kind=partial | timestamp=1778067148.7409108 | source=vosk
- [2026-05-06 19:32:29] operator / voice_transcript_final / voice: change your voice buzzer in human voice
  meta: kind=final | timestamp=1778067149.9473546 | source=final
- [2026-05-06 19:32:30] operator / voice_command / voice: change your voice buzzer in human voice
  meta: normalized=True
- [2026-05-06 19:32:50] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778067170.2424684 | source=vosk
- [2026-05-06 19:32:50] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778067170.4858875 | source=vosk
- [2026-05-06 19:32:50] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:32:51] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778067171.62499 | source=final
- [2026-05-06 19:32:58] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778067178.8314245 | source=vosk
- [2026-05-06 19:32:59] operator / voice_transcript_partial / voice: replies
  meta: kind=partial | timestamp=1778067179.0792427 | source=vosk
- [2026-05-06 19:33:01] operator / voice_transcript_final / voice: the auto on
  meta: kind=final | timestamp=1778067181.7342594 | source=final
- [2026-05-06 19:33:02] operator / voice_transcript_partial / voice: model
  meta: kind=partial | timestamp=1778067182.8328342 | source=vosk
- [2026-05-06 19:33:03] operator / voice_transcript_final / voice: model
  meta: kind=final | timestamp=1778067183.6741025 | source=final
- [2026-05-06 19:33:07] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778067187.7563562 | source=vosk
- [2026-05-06 19:33:08] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:33:09] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778067189.366954 | source=final
- [2026-05-06 19:33:22] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output deactivate
  meta: kind=partial | timestamp=1778067202.1234157 | source=vosk
- [2026-05-06 19:33:22] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output is
  meta: kind=partial | timestamp=1778067202.4081252 | source=vosk
- [2026-05-06 19:33:23] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output e lion
  meta: kind=partial | timestamp=1778067203.1183736 | source=vosk
- [2026-05-06 19:33:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:33:23] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of output e lion system
  meta: kind=partial | timestamp=1778067203.6235142 | source=vosk
- [2026-05-06 19:33:24] operator / voice_transcript_final / voice: acoustic guard detection on neutral sound of output e is pointer
  meta: kind=final | timestamp=1778067204.4306192 | source=final
- [2026-05-06 19:33:25] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778067205.1492636 | source=vosk
- [2026-05-06 19:33:25] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778067205.4134755 | source=vosk
- [2026-05-06 19:33:26] operator / voice_transcript_partial / voice: current status engaging
  meta: kind=partial | timestamp=1778067206.1611638 | source=vosk
- [2026-05-06 19:33:27] operator / voice_transcript_partial / voice: current status engaging scope
  meta: kind=partial | timestamp=1778067207.0108058 | source=vosk
- [2026-05-06 19:33:27] operator / voice_transcript_final / voice: current status engaging order
  meta: kind=final | timestamp=1778067207.3061175 | source=final
- [2026-05-06 19:33:31] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778067211.6529324 | source=vosk
- [2026-05-06 19:33:32] operator / voice_transcript_partial / voice: acoustic voice
  meta: kind=partial | timestamp=1778067212.151004 | source=vosk
- [2026-05-06 19:33:32] operator / voice_transcript_partial / voice: acoustic detection
  meta: kind=partial | timestamp=1778067212.4052427 | source=vosk
- [2026-05-06 19:33:32] operator / voice_transcript_partial / voice: acoustic detection on
  meta: kind=partial | timestamp=1778067212.9000063 | source=vosk
- [2026-05-06 19:33:33] operator / voice_transcript_partial / voice: acoustic detection on mute
  meta: kind=partial | timestamp=1778067213.1504908 | source=vosk
- [2026-05-06 19:33:33] operator / voice_transcript_partial / voice: acoustic detection on the visual overlay
  meta: kind=partial | timestamp=1778067213.4028304 | source=vosk
- [2026-05-06 19:33:33] operator / voice_transcript_partial / voice: acoustic detection on the visual sound
  meta: kind=partial | timestamp=1778067213.6515274 | source=vosk
- [2026-05-06 19:33:34] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output
  meta: kind=partial | timestamp=1778067214.1546469 | source=vosk
- [2026-05-06 19:33:34] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output suggestions
  meta: kind=partial | timestamp=1778067214.8997834 | source=vosk
- [2026-05-06 19:33:35] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output setting drafts
  meta: kind=partial | timestamp=1778067215.1470122 | source=vosk
- [2026-05-06 19:33:35] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken
  meta: kind=partial | timestamp=1778067215.4083683 | source=vosk
- [2026-05-06 19:33:35] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable the
  meta: kind=partial | timestamp=1778067215.6476645 | source=vosk
- [2026-05-06 19:33:35] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable
  meta: kind=partial | timestamp=1778067215.9085915 | source=vosk
- [2026-05-06 19:33:36] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable face
  meta: kind=partial | timestamp=1778067216.1507237 | source=vosk
- [2026-05-06 19:33:36] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable face elliot
  meta: kind=partial | timestamp=1778067216.407068 | source=vosk
- [2026-05-06 19:33:37] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable face elliot current
  meta: kind=partial | timestamp=1778067217.1943564 | source=vosk
- [2026-05-06 19:33:37] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable face elliot current status
  meta: kind=partial | timestamp=1778067217.4281108 | source=vosk
- [2026-05-06 19:33:38] operator / voice_transcript_partial / voice: acoustic detection on the visual sound output spoken disable face elliot current stay guarding mode
  meta: kind=partial | timestamp=1778067218.1562276 | source=vosk
- [2026-05-06 19:33:39] operator / voice_transcript_final / voice: elion acoustic detection on the visual sound output spoken disable servo face current stay guarding
  meta: kind=final | timestamp=1778067219.4254608 | source=final
- [2026-05-06 19:33:40] operator / voice_command / voice: elion acoustic detection on the visual sound output spoken disable servo face current stay guarding
  meta: normalized=True
- [2026-05-06 19:33:39] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778067219.433807 | source=vosk
- [2026-05-06 19:33:50] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1778067230.9284935 | source=vosk
- [2026-05-06 19:33:51] operator / voice_transcript_partial / voice: lion deactivate
  meta: kind=partial | timestamp=1778067231.1935594 | source=vosk
- [2026-05-06 19:33:51] operator / voice_transcript_partial / voice: name the
  meta: kind=partial | timestamp=1778067231.4316816 | source=vosk
- [2026-05-06 19:33:51] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778067231.695738 | source=vosk
- [2026-05-06 19:33:52] operator / voice_transcript_partial / voice: known face name
  meta: kind=partial | timestamp=1778067232.0618274 | source=vosk
- [2026-05-06 19:33:52] operator / voice_transcript_partial / voice: known face lion
  meta: kind=partial | timestamp=1778067232.4482572 | source=vosk
- [2026-05-06 19:33:52] operator / voice_transcript_partial / voice: known face name current
  meta: kind=partial | timestamp=1778067232.6809516 | source=vosk
- [2026-05-06 19:33:52] operator / voice_transcript_partial / voice: known face name current status
  meta: kind=partial | timestamp=1778067232.9441116 | source=vosk
- [2026-05-06 19:33:53] operator / voice_transcript_partial / voice: known face name current status id
  meta: kind=partial | timestamp=1778067233.4292946 | source=vosk
- [2026-05-06 19:33:54] operator / voice_transcript_final / voice: name the face name current status id
  meta: kind=final | timestamp=1778067234.3178117 | source=final
- [2026-05-06 19:35:17] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound switching on
  meta: kind=partial | timestamp=1778067317.7410684 | source=vosk
- [2026-05-06 19:35:17] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound switching on setting
  meta: kind=partial | timestamp=1778067317.943698 | source=vosk
- [2026-05-06 19:35:18] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound switching on setting the
  meta: kind=partial | timestamp=1778067318.7002544 | source=vosk
- [2026-05-06 19:35:18] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound switching on setting test video
  meta: kind=partial | timestamp=1778067318.9336572 | source=vosk
- [2026-05-06 19:35:19] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound switching on setting the overlay
  meta: kind=partial | timestamp=1778067319.192183 | source=vosk
- [2026-05-06 19:35:19] operator / voice_transcript_final / voice: acoustic guard detection on neutral sound switching on setting the overlay
  meta: kind=final | timestamp=1778067319.9335089 | source=final
- [2026-05-06 19:35:20] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778067320.1955683 | source=vosk
- [2026-05-06 19:35:20] operator / voice_transcript_partial / voice: current say
  meta: kind=partial | timestamp=1778067320.6823075 | source=vosk
- [2026-05-06 19:35:20] operator / voice_transcript_partial / voice: current say guarding mode
  meta: kind=partial | timestamp=1778067320.9473238 | source=vosk
- [2026-05-06 19:35:22] operator / voice_transcript_final / voice: current say guarding
  meta: kind=final | timestamp=1778067322.0766144 | source=final
- [2026-05-06 19:36:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound updates
  meta: kind=partial | timestamp=1778067407.6489913 | source=vosk
- [2026-05-06 19:36:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound update
  meta: kind=partial | timestamp=1778067407.6702933 | source=vosk
- [2026-05-06 19:36:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound activate the
  meta: kind=partial | timestamp=1778067407.9003687 | source=vosk
- [2026-05-06 19:36:48] operator / voice_transcript_final / voice: acoustic guard detection on the visual sound update
  meta: kind=final | timestamp=1778067408.7903965 | source=final
- [2026-05-06 19:36:48] operator / voice_transcript_partial / voice: execution
  meta: kind=partial | timestamp=1778067408.845222 | source=vosk
- [2026-05-06 19:36:48] operator / voice_transcript_partial / voice: disable the
  meta: kind=partial | timestamp=1778067408.8595278 | source=vosk
- [2026-05-06 19:36:49] operator / voice_transcript_partial / voice: disable spoken
  meta: kind=partial | timestamp=1778067409.0732923 | source=vosk
- [2026-05-06 19:36:49] operator / voice_transcript_partial / voice: disabled of zone
  meta: kind=partial | timestamp=1778067409.3273227 | source=vosk
- [2026-05-06 19:36:50] operator / voice_transcript_partial / voice: disabled of zone current
  meta: kind=partial | timestamp=1778067410.0716527 | source=vosk
- [2026-05-06 19:36:50] operator / voice_transcript_partial / voice: disabled of zone current status
  meta: kind=partial | timestamp=1778067410.322097 | source=vosk
- [2026-05-06 19:36:50] operator / voice_transcript_partial / voice: disabled of zone current stay guard
  meta: kind=partial | timestamp=1778067410.8442924 | source=vosk
- [2026-05-06 19:36:51] operator / voice_transcript_partial / voice: disabled of zone current stay guarding mode
  meta: kind=partial | timestamp=1778067411.0839734 | source=vosk
- [2026-05-06 19:36:51] operator / voice_transcript_partial / voice: disabled of zone current stay guarding elliot
  meta: kind=partial | timestamp=1778067411.5672767 | source=vosk
- [2026-05-06 19:36:52] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778067412.985416 | source=vosk
- [2026-05-06 19:36:53] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778067413.317186 | source=vosk
- [2026-05-06 19:36:53] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778067413.5752351 | source=vosk
- [2026-05-06 19:36:54] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778067414.069961 | source=vosk
- [2026-05-06 19:36:54] operator / voice_transcript_partial / voice: acoustic guard detection leon use
  meta: kind=partial | timestamp=1778067414.3181584 | source=vosk
- [2026-05-06 19:36:54] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound
  meta: kind=partial | timestamp=1778067414.5867105 | source=vosk
- [2026-05-06 19:36:55] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound announcements
  meta: kind=partial | timestamp=1778067415.0924013 | source=vosk
- [2026-05-06 19:36:55] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory
  meta: kind=partial | timestamp=1778067415.3446605 | source=vosk
- [2026-05-06 19:36:55] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the
  meta: kind=partial | timestamp=1778067415.5712447 | source=vosk
- [2026-05-06 19:36:55] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory
  meta: kind=partial | timestamp=1778067415.8172534 | source=vosk
- [2026-05-06 19:36:56] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat
  meta: kind=partial | timestamp=1778067416.3664792 | source=vosk
- [2026-05-06 19:36:56] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat execution
  meta: kind=partial | timestamp=1778067416.591549 | source=vosk
- [2026-05-06 19:36:57] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat execution off
  meta: kind=partial | timestamp=1778067417.0663533 | source=vosk
- [2026-05-06 19:36:57] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat disable servo face
  meta: kind=partial | timestamp=1778067417.339353 | source=vosk
- [2026-05-06 19:36:57] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat disable servo face id
  meta: kind=partial | timestamp=1778067417.8344114 | source=vosk
- [2026-05-06 19:36:58] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat disable servo face lion alion
  meta: kind=partial | timestamp=1778067418.073916 | source=vosk
- [2026-05-06 19:36:58] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:36:58] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat disable servo face lion alion current status
  meta: kind=partial | timestamp=1778067418.6432586 | source=vosk
- [2026-05-06 19:36:58] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat disable servo face lion alion current stay guard
  meta: kind=partial | timestamp=1778067418.843849 | source=vosk
- [2026-05-06 19:36:59] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound off the threat disable servo face lion alion current stay guarding mode
  meta: kind=partial | timestamp=1778067419.0998912 | source=vosk
- [2026-05-06 19:37:02] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:37:01] operator / voice_transcript_final / voice: elion acoustic guard detection on neutral sound off the threat disable servo face lion current stay guarding
  meta: kind=final | timestamp=1778067421.178677 | source=final
- [2026-05-06 19:37:03] operator / voice_command / voice: elion acoustic guard detection on neutral sound off the threat disable servo face lion current stay guarding
  meta: normalized=True
- [2026-05-06 19:37:26] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778067446.5010712 | source=vosk
- [2026-05-06 19:37:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:37:26] operator / voice_transcript_partial / voice: e lion disable
  meta: kind=partial | timestamp=1778067446.7686162 | source=vosk
- [2026-05-06 19:37:27] operator / voice_transcript_partial / voice: e lion disable the
  meta: kind=partial | timestamp=1778067447.006845 | source=vosk
- [2026-05-06 19:37:27] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778067447.255119 | source=vosk
- [2026-05-06 19:37:27] operator / voice_transcript_partial / voice: known faces
  meta: kind=partial | timestamp=1778067447.5010567 | source=vosk
- [2026-05-06 19:37:27] operator / voice_transcript_partial / voice: e lion the face lion
  meta: kind=partial | timestamp=1778067447.7638783 | source=vosk
- [2026-05-06 19:37:30] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:37:28] operator / voice_transcript_partial / voice: e lion the face lion current status
  meta: kind=partial | timestamp=1778067448.5230162 | source=vosk
- [2026-05-06 19:37:30] operator / voice_transcript_final / voice: elion lion disable the face current status
  meta: kind=final | timestamp=1778067450.2923784 | source=final
- [2026-05-06 19:37:32] operator / voice_command / voice: elion lion disable the face current status
  meta: normalized=True
- [2026-05-06 19:37:37] assistant / spoken_confirmation / voice: Received. I started a live runtime analysis in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 19:37:43] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778067463.3034718 | source=vosk
- [2026-05-06 19:37:44] operator / voice_transcript_partial / voice: acoustic guard disabled
  meta: kind=partial | timestamp=1778067464.070598 | source=vosk
- [2026-05-06 19:37:44] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778067464.3292384 | source=vosk
- [2026-05-06 19:37:44] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778067464.5529974 | source=vosk
- [2026-05-06 19:37:44] operator / voice_transcript_partial / voice: acoustic guard detection on use
  meta: kind=partial | timestamp=1778067464.8325052 | source=vosk
- [2026-05-06 19:37:45] operator / voice_transcript_partial / voice: acoustic guard detection on the visual
  meta: kind=partial | timestamp=1778067465.057403 | source=vosk
- [2026-05-06 19:37:46] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound
  meta: kind=partial | timestamp=1778067466.164765 | source=vosk
- [2026-05-06 19:37:46] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound announcements
  meta: kind=partial | timestamp=1778067466.5186107 | source=vosk
- [2026-05-06 19:37:46] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound the
  meta: kind=partial | timestamp=1778067466.6825047 | source=vosk
- [2026-05-06 19:37:46] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound the video
  meta: kind=partial | timestamp=1778067466.9313507 | source=vosk
- [2026-05-06 19:37:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound the feed execution
  meta: kind=partial | timestamp=1778067467.1823437 | source=vosk
- [2026-05-06 19:37:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled
  meta: kind=partial | timestamp=1778067467.47328 | source=vosk
- [2026-05-06 19:37:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of
  meta: kind=partial | timestamp=1778067467.6892292 | source=vosk
- [2026-05-06 19:37:47] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face
  meta: kind=partial | timestamp=1778067467.9998279 | source=vosk
- [2026-05-06 19:37:48] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face no
  meta: kind=partial | timestamp=1778067468.6880531 | source=vosk
- [2026-05-06 19:37:48] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status
  meta: kind=partial | timestamp=1778067468.9807775 | source=vosk
- [2026-05-06 19:37:49] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status is
  meta: kind=partial | timestamp=1778067469.4528642 | source=vosk
- [2026-05-06 19:37:49] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry
  meta: kind=partial | timestamp=1778067469.6922195 | source=vosk
- [2026-05-06 19:37:51] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic
  meta: kind=partial | timestamp=1778067471.8133252 | source=vosk
- [2026-05-06 19:37:52] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard
  meta: kind=partial | timestamp=1778067472.062003 | source=vosk
- [2026-05-06 19:37:52] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection
  meta: kind=partial | timestamp=1778067472.596974 | source=vosk
- [2026-05-06 19:37:53] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on
  meta: kind=partial | timestamp=1778067473.2354891 | source=vosk
- [2026-05-06 19:37:53] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on use
  meta: kind=partial | timestamp=1778067473.244834 | source=vosk
- [2026-05-06 19:37:53] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral
  meta: kind=partial | timestamp=1778067473.4008727 | source=vosk
- [2026-05-06 19:37:53] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sound announcements
  meta: kind=partial | timestamp=1778067473.9263117 | source=vosk
- [2026-05-06 19:37:55] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:37:54] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the
  meta: kind=partial | timestamp=1778067474.520564 | source=vosk
- [2026-05-06 19:37:55] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the auto export
  meta: kind=partial | timestamp=1778067475.5003617 | source=vosk
- [2026-05-06 19:37:55] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a
  meta: kind=partial | timestamp=1778067475.7855716 | source=vosk
- [2026-05-06 19:37:56] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a disable face id
  meta: kind=partial | timestamp=1778067476.2467246 | source=vosk
- [2026-05-06 19:37:57] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:37:56] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a disable face id current
  meta: kind=partial | timestamp=1778067476.9842045 | source=vosk
- [2026-05-06 19:37:57] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a disable face id current status
  meta: kind=partial | timestamp=1778067477.2314892 | source=vosk
- [2026-05-06 19:37:57] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a disable face id current status motion
  meta: kind=partial | timestamp=1778067477.7400565 | source=vosk
- [2026-05-06 19:37:58] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a disable face id current status motion machine
  meta: kind=partial | timestamp=1778067478.006407 | source=vosk
- [2026-05-06 19:37:59] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:37:58] operator / voice_transcript_partial / voice: acoustic guard detection on the visual sound disabled of face alion status the smart sentry acoustic guard detection on neutral sentinel the a disable face id current status motion the smart sentry
  meta: kind=partial | timestamp=1778067478.265151 | source=vosk
- [2026-05-06 19:37:59] operator / voice_transcript_final / voice: disable smart sentry
  meta: kind=final | timestamp=1778067479.556443 | source=final
- [2026-05-06 19:38:01] operator / voice_command / voice: disable smart sentry
  meta: normalized=True
- [2026-05-06 19:38:04] assistant / spoken_confirmation / voice: Pausing Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:38:13] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778067493.8833566 | source=vosk
- [2026-05-06 19:38:15] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778067495.1897156 | source=vosk
- [2026-05-06 19:38:15] operator / voice_transcript_partial / voice: acoustic guard detection on neutral
  meta: kind=partial | timestamp=1778067495.2728899 | source=vosk
- [2026-05-06 19:38:15] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo motion
  meta: kind=partial | timestamp=1778067495.6018171 | source=vosk
- [2026-05-06 19:38:15] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo
  meta: kind=partial | timestamp=1778067495.8508534 | source=vosk
- [2026-05-06 19:38:16] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat scores
  meta: kind=partial | timestamp=1778067496.1370528 | source=vosk
- [2026-05-06 19:38:16] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known
  meta: kind=partial | timestamp=1778067496.603116 | source=vosk
- [2026-05-06 19:38:16] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known the
  meta: kind=partial | timestamp=1778067496.8763046 | source=vosk
- [2026-05-06 19:38:17] assistant / assistant_analysis / text: Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Runtime facts: state=ENGAGING | camera_open=True | yolo_loaded=True | face_backend=opencv_sface | face_profiles_ready=3/6 | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=projectile burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Enable at least one PIR sensor or disable PIR guard to match actual intent. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=projectile_servo; burst=6@70ms; return_delay=1.50s; face=on; pir=on. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 19:38:17] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known the of
  meta: kind=partial | timestamp=1778067497.744925 | source=vosk
- [2026-05-06 19:38:17] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known faces
  meta: kind=partial | timestamp=1778067497.877728 | source=vosk
- [2026-05-06 19:38:18] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known face elliot
  meta: kind=partial | timestamp=1778067498.1042688 | source=vosk
- [2026-05-06 19:38:18] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known face elliot current
  meta: kind=partial | timestamp=1778067498.8894806 | source=vosk
- [2026-05-06 19:38:19] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known face elliot current status
  meta: kind=partial | timestamp=1778067499.1376524 | source=vosk
- [2026-05-06 19:38:19] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known face elliot current stay guard
  meta: kind=partial | timestamp=1778067499.601818 | source=vosk
- [2026-05-06 19:38:19] operator / voice_transcript_partial / voice: acoustic guard detection on neutral servo threat known face elliot current stay guard off
  meta: kind=partial | timestamp=1778067499.8521829 | source=vosk
- [2026-05-06 19:38:22] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:38:24] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:38:28] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778067508.127826 | source=vosk
- [2026-05-06 19:38:28] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1778067508.344145 | source=vosk

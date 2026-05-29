# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 19:54:15
- Entries: 290
- Roles: {'assistant': 11, 'system': 1, 'operator': 278}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 224, 'voice_transcript_final': 39, 'voice_command': 15, 'spoken_confirmation': 7, 'spoken_reply': 1}
- Channels: {'text': 3, 'voice': 287}
- Latest operator request: listening
- Latest assistant message: I am here. Ask your question.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 19:48:48] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 19:48:48] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 19:48:50] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778068130.5920987 | source=vosk
- [2026-05-06 19:49:20] operator / voice_transcript_partial / voice: automatic
  meta: kind=partial | timestamp=1778068160.2873523 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:20] operator / voice_transcript_partial / voice: order the
  meta: kind=partial | timestamp=1778068160.7955017 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:21] operator / voice_transcript_partial / voice: order the invert
  meta: kind=partial | timestamp=1778068161.0395546 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:21] operator / voice_transcript_partial / voice: order enabled
  meta: kind=partial | timestamp=1778068161.2881148 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:21] operator / voice_transcript_partial / voice: order the runtime analysis
  meta: kind=partial | timestamp=1778068161.5388534 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:21] operator / voice_transcript_partial / voice: turn off
  meta: kind=partial | timestamp=1778068161.7913845 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:22] operator / voice_transcript_final / voice: order the turn off
  meta: kind=final | timestamp=1778068162.43791 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:24] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1778068164.037907 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:27] operator / voice_transcript_partial / voice: buzzer
  meta: kind=partial | timestamp=1778068167.537819 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:28] operator / voice_transcript_partial / voice: is the window
  meta: kind=partial | timestamp=1778068168.040624 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:28] operator / voice_transcript_partial / voice: is the window shortcuts
  meta: kind=partial | timestamp=1778068168.2902956 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:29] operator / voice_transcript_final / voice: is the window
  meta: kind=final | timestamp=1778068169.186242 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:31] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1778068171.04665 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:31] operator / voice_transcript_partial / voice: use medium model
  meta: kind=partial | timestamp=1778068171.3143697 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:31] operator / voice_transcript_partial / voice: is name on id enabled
  meta: kind=partial | timestamp=1778068171.5483935 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:32] operator / voice_transcript_partial / voice: is name elliot enable adaptive
  meta: kind=partial | timestamp=1778068172.0487866 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:32] operator / voice_transcript_partial / voice: is name elliot enable adaptive after
  meta: kind=partial | timestamp=1778068172.297336 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:32] operator / voice_transcript_partial / voice: display media loop turn
  meta: kind=partial | timestamp=1778068172.5503807 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:33] operator / voice_transcript_partial / voice: display media loop turn on acoustic
  meta: kind=partial | timestamp=1778068173.0569575 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:33] operator / voice_transcript_partial / voice: display media loop turn on include
  meta: kind=partial | timestamp=1778068173.2943292 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:33] operator / voice_transcript_partial / voice: display media loop turn on include logs
  meta: kind=partial | timestamp=1778068173.5443494 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:34] operator / voice_transcript_final / voice: is name on id loop turn on include cleanup
  meta: kind=final | timestamp=1778068174.2734363 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:34] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1778068174.305555 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:34] operator / voice_transcript_partial / voice: aiming
  meta: kind=partial | timestamp=1778068174.5406811 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:35] operator / voice_transcript_final / voice: aiming
  meta: kind=final | timestamp=1778068175.2304735 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:36] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778068176.2920759 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:36] operator / voice_transcript_partial / voice: video display
  meta: kind=partial | timestamp=1778068176.5479453 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:36] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778068176.7905738 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:37] operator / voice_transcript_final / voice: video
  meta: kind=final | timestamp=1778068177.568613 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:37] operator / voice_transcript_partial / voice: is the buzzer
  meta: kind=partial | timestamp=1778068177.586781 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:37] operator / voice_transcript_partial / voice: is the running
  meta: kind=partial | timestamp=1778068177.6019025 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:38] operator / voice_transcript_final / voice: is the running
  meta: kind=final | timestamp=1778068178.2097907 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:39] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778068179.0837963 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:40] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1778068180.0398004 | source=final | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:41] operator / voice_transcript_partial / voice: elliot enable
  meta: kind=partial | timestamp=1778068181.2534294 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:41] operator / voice_transcript_partial / voice: elliot enable do
  meta: kind=partial | timestamp=1778068181.7442863 | source=vosk | frequency_hz=165.5 | rms=793 | updated_at=1778068132.7800558
- [2026-05-06 19:49:42] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:49:42] assistant / spoken_confirmation / voice: I am here. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:49:45] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778068185.9124527 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:46] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778068186.1647236 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:46] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:49:46] operator / voice_transcript_partial / voice: e ask
  meta: kind=partial | timestamp=1778068186.4168844 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:46] operator / voice_transcript_partial / voice: e ask a question
  meta: kind=partial | timestamp=1778068186.6646347 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:47] operator / voice_transcript_partial / voice: e ask a question optimization
  meta: kind=partial | timestamp=1778068187.4138455 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:47] operator / voice_transcript_partial / voice: e ask a question what the continuous
  meta: kind=partial | timestamp=1778068187.665906 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:47] operator / voice_transcript_partial / voice: e ask a question guard
  meta: kind=partial | timestamp=1778068187.9205737 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:48] operator / voice_transcript_partial / voice: e ask a question what the continuous hunt
  meta: kind=partial | timestamp=1778068188.1639392 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:48] operator / voice_transcript_partial / voice: e ask a question what the continuous alien
  meta: kind=partial | timestamp=1778068188.9156623 | source=vosk | frequency_hz=284.0 | rms=691 | updated_at=1778068181.9859693
- [2026-05-06 19:49:49] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:49:50] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:49:53] operator / voice_transcript_partial / voice: engagement zone yes what do you working
  meta: kind=partial | timestamp=1778068193.504821 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:49:53] operator / voice_transcript_partial / voice: engagement zone yes what do you run
  meta: kind=partial | timestamp=1778068193.512836 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:49:53] operator / voice_transcript_partial / voice: engagement zone yes what do you run the smart
  meta: kind=partial | timestamp=1778068193.7457383 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:49:53] operator / voice_transcript_partial / voice: engagement zone yes what do you run the smart sentry
  meta: kind=partial | timestamp=1778068193.997308 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:49:54] operator / voice_transcript_final / voice: boards video yes what do you run the smart
  meta: kind=final | timestamp=1778068194.888045 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:06] operator / voice_transcript_partial / voice: reports off
  meta: kind=partial | timestamp=1778068206.998943 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:10] operator / voice_transcript_final / voice: reports
  meta: kind=final | timestamp=1778068210.0923743 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:14] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778068214.5011108 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:14] operator / voice_transcript_partial / voice: auto enable
  meta: kind=partial | timestamp=1778068214.7538538 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:14] operator / voice_transcript_partial / voice: auto enable no
  meta: kind=partial | timestamp=1778068214.9976587 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:15] operator / voice_transcript_partial / voice: auto enable no zone
  meta: kind=partial | timestamp=1778068215.2472074 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:15] operator / voice_transcript_partial / voice: auto enable no zone pir sensors
  meta: kind=partial | timestamp=1778068215.498137 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:15] operator / voice_transcript_partial / voice: auto enable no zone buzzer
  meta: kind=partial | timestamp=1778068215.7512224 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:16] operator / voice_transcript_partial / voice: auto enable no zone buzzer the pir guard
  meta: kind=partial | timestamp=1778068216.248734 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:16] operator / voice_transcript_partial / voice: auto enable no zone buzzer the current
  meta: kind=partial | timestamp=1778068216.4988754 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:17] operator / voice_transcript_final / voice: auto enable no joke buzzer for the pir current
  meta: kind=final | timestamp=1778068217.3993564 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:19] operator / voice_transcript_partial / voice: keyboard
  meta: kind=partial | timestamp=1778068219.7480438 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:20] operator / voice_transcript_partial / voice: buzzer
  meta: kind=partial | timestamp=1778068220.2553153 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:20] operator / voice_transcript_partial / voice: buzzer enabled
  meta: kind=partial | timestamp=1778068220.4978669 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:20] operator / voice_transcript_partial / voice: buzzer in human
  meta: kind=partial | timestamp=1778068220.7522702 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:21] operator / voice_transcript_partial / voice: buzzer in human the guard
  meta: kind=partial | timestamp=1778068221.0016615 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:21] operator / voice_transcript_partial / voice: buzzer in human the turn
  meta: kind=partial | timestamp=1778068221.2464008 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:21] operator / voice_transcript_partial / voice: buzzer in human the guard running
  meta: kind=partial | timestamp=1778068221.5014706 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:21] operator / voice_transcript_partial / voice: buzzer in human voice buzzer mute
  meta: kind=partial | timestamp=1778068221.7494466 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:21] operator / voice_transcript_partial / voice: buzzer in human voice buzzer
  meta: kind=partial | timestamp=1778068221.9997175 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:22] operator / voice_transcript_partial / voice: buzzer in human voice buzzer mute
  meta: kind=partial | timestamp=1778068222.2516189 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:23] operator / voice_transcript_final / voice: buzzer mute buzzer in human the turn human buzzer mute
  meta: kind=final | timestamp=1778068223.6662722 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:23] operator / voice_transcript_partial / voice: movement
  meta: kind=partial | timestamp=1778068223.7470837 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:24] operator / voice_transcript_final / voice: movement
  meta: kind=final | timestamp=1778068224.6051242 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:24] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1778068224.6129417 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:26] operator / voice_transcript_partial / voice: in human
  meta: kind=partial | timestamp=1778068226.2564206 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:26] operator / voice_transcript_partial / voice: include logs
  meta: kind=partial | timestamp=1778068226.4974718 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:27] operator / voice_transcript_final / voice: include
  meta: kind=final | timestamp=1778068227.3538203 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:29] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778068229.2496827 | source=vosk | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:29] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:50:30] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778068230.6063507 | source=final | frequency_hz=126.0 | rms=1200 | updated_at=1778068192.7551074
- [2026-05-06 19:50:53] operator / voice_transcript_partial / voice: summaries
  meta: kind=partial | timestamp=1778068253.998836 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:54] operator / voice_transcript_partial / voice: on is
  meta: kind=partial | timestamp=1778068254.2469087 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:54] operator / voice_transcript_partial / voice: servo motion
  meta: kind=partial | timestamp=1778068254.501052 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:55] operator / voice_transcript_partial / voice: on no zone
  meta: kind=partial | timestamp=1778068255.2471492 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:56] operator / voice_transcript_final / voice: servo on no zone
  meta: kind=final | timestamp=1778068256.136889 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:56] operator / voice_transcript_partial / voice: manual
  meta: kind=partial | timestamp=1778068256.2456179 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:57] operator / voice_transcript_partial / voice: mode suggestions
  meta: kind=partial | timestamp=1778068257.0069633 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:57] operator / voice_transcript_partial / voice: the mute buzzer lion
  meta: kind=partial | timestamp=1778068257.2489245 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:57] operator / voice_transcript_partial / voice: summaries
  meta: kind=partial | timestamp=1778068257.5091448 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:57] operator / voice_transcript_partial / voice: elian the the assistant
  meta: kind=partial | timestamp=1778068257.750765 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:57] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:50:58] operator / voice_transcript_partial / voice: elian the the acoustic guard
  meta: kind=partial | timestamp=1778068258.5023563 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:58] operator / voice_transcript_partial / voice: the mute buzzer mute buzzer
  meta: kind=partial | timestamp=1778068258.746507 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:59] operator / voice_transcript_final / voice: summaries off
  meta: kind=final | timestamp=1778068259.1071053 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:59] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778068259.293055 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:50:59] operator / voice_transcript_partial / voice: on the
  meta: kind=partial | timestamp=1778068259.4962752 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:00] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1778068260.0961258 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:03] operator / voice_transcript_partial / voice: summaries is
  meta: kind=partial | timestamp=1778068263.2515764 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:03] operator / voice_transcript_partial / voice: summaries is working
  meta: kind=partial | timestamp=1778068263.5016255 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:03] operator / voice_transcript_partial / voice: summaries is what
  meta: kind=partial | timestamp=1778068263.7513866 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:04] operator / voice_transcript_final / voice: summaries
  meta: kind=final | timestamp=1778068264.0873487 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:06] operator / voice_transcript_partial / voice: loss
  meta: kind=partial | timestamp=1778068266.000492 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:06] operator / voice_transcript_partial / voice: last request
  meta: kind=partial | timestamp=1778068266.2485704 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:06] operator / voice_transcript_partial / voice: loss recovery
  meta: kind=partial | timestamp=1778068266.7461588 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:06] operator / voice_transcript_partial / voice: loss recovery disabled
  meta: kind=partial | timestamp=1778068266.9977407 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:07] operator / voice_transcript_partial / voice: loss recovery the spoken
  meta: kind=partial | timestamp=1778068267.256698 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:07] operator / voice_transcript_partial / voice: loss recovery the spoken is
  meta: kind=partial | timestamp=1778068267.748396 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:08] operator / voice_transcript_partial / voice: loss recovery the spoken spoken alerts
  meta: kind=partial | timestamp=1778068268.007684 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:08] operator / voice_transcript_partial / voice: loss recovery the spoken spoken the movement
  meta: kind=partial | timestamp=1778068268.246611 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:08] operator / voice_transcript_partial / voice: loss recovery the spoken spoken the movement is the precision
  meta: kind=partial | timestamp=1778068268.5067136 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:08] operator / voice_transcript_partial / voice: loss recovery the spoken spoken alerts
  meta: kind=partial | timestamp=1778068268.7470684 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:08] operator / voice_transcript_partial / voice: loss recovery the spoken spoken the movement is the pir event blink
  meta: kind=partial | timestamp=1778068268.9973974 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:09] operator / voice_transcript_partial / voice: loss recovery the spoken spoken the movement running
  meta: kind=partial | timestamp=1778068269.301615 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:09] operator / voice_transcript_partial / voice: loss recovery the spoken spoken the movement run microphone
  meta: kind=partial | timestamp=1778068269.756921 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:10] operator / voice_transcript_partial / voice: loss recovery the spoken spoken the movement running rest on no
  meta: kind=partial | timestamp=1778068270.2552345 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:11] operator / voice_transcript_final / voice: loss recovery the spoken spoken the movement is the current run microphone zone
  meta: kind=final | timestamp=1778068271.2087417 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:12] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778068272.74874 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:13] operator / voice_transcript_partial / voice: mode
  meta: kind=partial | timestamp=1778068273.0005846 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:13] operator / voice_transcript_partial / voice: servo motion
  meta: kind=partial | timestamp=1778068273.250512 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:13] operator / voice_transcript_partial / voice: the anomaly trigger what is
  meta: kind=partial | timestamp=1778068273.5039213 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:13] operator / voice_transcript_partial / voice: the anomaly trigger what is not loading
  meta: kind=partial | timestamp=1778068273.7564683 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:14] operator / voice_transcript_partial / voice: human human voice mode is on what
  meta: kind=partial | timestamp=1778068274.003906 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:14] operator / voice_transcript_partial / voice: human human voice mode is on recognition
  meta: kind=partial | timestamp=1778068274.2496276 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:14] operator / voice_transcript_partial / voice: human human voice mode is on what is the
  meta: kind=partial | timestamp=1778068274.5059264 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:14] operator / voice_transcript_partial / voice: human human voice mode is on what is the manual
  meta: kind=partial | timestamp=1778068274.7500906 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:14] operator / voice_transcript_partial / voice: human human voice mode is on what is ml known
  meta: kind=partial | timestamp=1778068274.99719 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:16] operator / voice_transcript_final / voice: anomaly human voice mode is on what is the window ml known
  meta: kind=final | timestamp=1778068276.0329509 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:17] operator / voice_transcript_partial / voice: updates
  meta: kind=partial | timestamp=1778068277.5843813 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:17] operator / voice_transcript_partial / voice: the fire
  meta: kind=partial | timestamp=1778068277.7575874 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:17] operator / voice_transcript_partial / voice: the fire announcements
  meta: kind=partial | timestamp=1778068277.9969149 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:18] operator / voice_transcript_partial / voice: the fire
  meta: kind=partial | timestamp=1778068278.252005 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:18] operator / voice_transcript_partial / voice: the fire off the microphone
  meta: kind=partial | timestamp=1778068278.4990482 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:18] operator / voice_transcript_partial / voice: the fire
  meta: kind=partial | timestamp=1778068278.8530264 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:19] operator / voice_transcript_partial / voice: the fire running
  meta: kind=partial | timestamp=1778068279.0030172 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:19] operator / voice_transcript_partial / voice: the fire off the mode suggestions
  meta: kind=partial | timestamp=1778068279.2616115 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:19] operator / voice_transcript_partial / voice: the fire for human
  meta: kind=partial | timestamp=1778068279.5089948 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:19] operator / voice_transcript_partial / voice: the fire elliot disable the manual
  meta: kind=partial | timestamp=1778068279.7521787 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:19] operator / voice_transcript_partial / voice: the fire for human voice
  meta: kind=partial | timestamp=1778068279.9985929 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:20] operator / voice_transcript_final / voice: the fire for human voice
  meta: kind=final | timestamp=1778068280.9334397 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:21] operator / voice_transcript_partial / voice: mask assistant
  meta: kind=partial | timestamp=1778068281.2474945 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:21] operator / voice_transcript_partial / voice: mask automatic
  meta: kind=partial | timestamp=1778068281.4981623 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:21] operator / voice_transcript_partial / voice: mask cancel mask diagnostics
  meta: kind=partial | timestamp=1778068281.7500126 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:22] operator / voice_transcript_partial / voice: mask automatic lion
  meta: kind=partial | timestamp=1778068282.246534 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:22] operator / voice_transcript_partial / voice: mask automatic lion decrease
  meta: kind=partial | timestamp=1778068282.9971838 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:23] operator / voice_transcript_partial / voice: mask automatic lion the guard
  meta: kind=partial | timestamp=1778068283.2521217 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:23] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output
  meta: kind=partial | timestamp=1778068283.7557795 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:23] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the
  meta: kind=partial | timestamp=1778068283.9976506 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:24] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the one
  meta: kind=partial | timestamp=1778068284.2496624 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:24] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert
  meta: kind=partial | timestamp=1778068284.499153 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:25] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert guard zone masks
  meta: kind=partial | timestamp=1778068285.004574 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:25] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert guard zone
  meta: kind=partial | timestamp=1778068285.246809 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:25] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert guard zone local actions
  meta: kind=partial | timestamp=1778068285.7492476 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:26] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert guard zone what for prompted
  meta: kind=partial | timestamp=1778068286.0008528 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:26] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert guard zone microphone anomaly
  meta: kind=partial | timestamp=1778068286.2579613 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:26] operator / voice_transcript_partial / voice: mask automatic lion is the adaptive output on the invert guard zone local enable on auto
  meta: kind=partial | timestamp=1778068286.5081854 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:51:28] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:51:31] operator / voice_transcript_partial / voice: is yes
  meta: kind=partial | timestamp=1778068291.6405709 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:31] operator / voice_transcript_partial / voice: is yes ai on listening
  meta: kind=partial | timestamp=1778068291.8870654 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:32] operator / voice_transcript_final / voice: is yes ai on listening
  meta: kind=final | timestamp=1778068292.7873797 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:33] operator / voice_transcript_partial / voice: hi set
  meta: kind=partial | timestamp=1778068293.138878 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:34] operator / voice_transcript_partial / voice: hi set run
  meta: kind=partial | timestamp=1778068294.107684 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:34] operator / voice_transcript_partial / voice: hi set run the smart
  meta: kind=partial | timestamp=1778068294.1165872 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:34] operator / voice_transcript_partial / voice: hi set run the smart sentry
  meta: kind=partial | timestamp=1778068294.146122 | source=vosk | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:35] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778068295.2949286 | source=final | frequency_hz=240.0 | rms=617 | updated_at=1778068231.2388015
- [2026-05-06 19:51:35] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 19:51:35] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:51:47] operator / voice_transcript_partial / voice: smart alien enable ask another
  meta: kind=partial | timestamp=1778068307.7546182 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:47] operator / voice_transcript_partial / voice: smart alien enable ask another question
  meta: kind=partial | timestamp=1778068307.916744 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:48] operator / voice_transcript_partial / voice: smart alien enable ask another question give another
  meta: kind=partial | timestamp=1778068308.9163048 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:49] operator / voice_transcript_partial / voice: smart alien enable ask another question give another recognition
  meta: kind=partial | timestamp=1778068309.9185972 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:50] operator / voice_transcript_partial / voice: smart alien enable ask another question give another greeting
  meta: kind=partial | timestamp=1778068310.1818187 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:51] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:51:51] operator / voice_transcript_partial / voice: activate
  meta: kind=partial | timestamp=1778068311.4192064 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:52] operator / voice_transcript_final / voice: activate
  meta: kind=final | timestamp=1778068312.2655575 | source=final | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:53] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778068313.415029 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:53] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778068313.7195835 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:54] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778068314.5189836 | source=final | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:54] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:51:55] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:51:57] operator / voice_transcript_partial / voice: yes eileen listening
  meta: kind=partial | timestamp=1778068317.923665 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:58] operator / voice_transcript_partial / voice: yes eileen listening hey
  meta: kind=partial | timestamp=1778068318.1656718 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:58] operator / voice_transcript_partial / voice: yes eileen listening who are you
  meta: kind=partial | timestamp=1778068318.4161348 | source=vosk | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:59] operator / voice_transcript_final / voice: yes on listening who are you
  meta: kind=final | timestamp=1778068319.3610408 | source=final | frequency_hz=160.0 | rms=316 | updated_at=1778068304.1592
- [2026-05-06 19:51:59] operator / voice_command / voice: yes on listening who are you
  meta: normalized=True
- [2026-05-06 19:51:59] assistant / assistant_prompt / text: I am Elion Mesk, Elion for short. I am the AI assistant voice inside Smart Sentry.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 19:52:00] assistant / spoken_reply / voice: I am Elion Mesk, Elion for short. I am the AI assistant voice inside Smart Sentry.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-06 19:52:06] operator / voice_transcript_partial / voice: ai assistant voice changes
  meta: kind=partial | timestamp=1778068326.7104986 | source=vosk | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:06] operator / voice_transcript_partial / voice: ai assistant voice engagement
  meta: kind=partial | timestamp=1778068326.8832655 | source=vosk | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:07] operator / voice_transcript_partial / voice: ai assistant voice smart sentry
  meta: kind=partial | timestamp=1778068327.1412644 | source=vosk | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:08] operator / voice_transcript_final / voice: ai assistant voice smart sentry
  meta: kind=final | timestamp=1778068328.5298002 | source=final | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:11] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778068331.3937867 | source=vosk | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:11] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778068331.6428492 | source=vosk | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:12] operator / voice_transcript_final / voice: change your voice
  meta: kind=final | timestamp=1778068332.99854 | source=final | frequency_hz=205.8 | rms=1165 | updated_at=1778068324.8750365
- [2026-05-06 19:52:13] operator / voice_command / voice: change your voice
  meta: normalized=True
- [2026-05-06 19:52:14] assistant / spoken_confirmation / voice: I can speak in 69 voices across 18 voice families, including Microsoft Zira Desktop, Microsoft Mark, Microsoft David Desktop, American English, and 14 more. Tell me what voice you want, or ask what are the options.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:52:26] operator / voice_transcript_partial / voice: hey the disconnect
  meta: kind=partial | timestamp=1778068346.4257047 | source=vosk | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:26] operator / voice_transcript_partial / voice: hey the test
  meta: kind=partial | timestamp=1778068346.682373 | source=vosk | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:27] operator / voice_transcript_partial / voice: hey the test ml refinement
  meta: kind=partial | timestamp=1778068347.3832014 | source=vosk | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:27] operator / voice_transcript_partial / voice: hey the test alerts enabled
  meta: kind=partial | timestamp=1778068347.4256713 | source=vosk | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:27] operator / voice_transcript_partial / voice: hey the test camera feed visual
  meta: kind=partial | timestamp=1778068347.6772974 | source=vosk | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:27] operator / voice_transcript_partial / voice: hey the test ml alien what is
  meta: kind=partial | timestamp=1778068347.9301062 | source=vosk | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:28] operator / voice_transcript_final / voice: be the test camera feed laser pointer
  meta: kind=final | timestamp=1778068348.745398 | source=final | frequency_hz=222.0 | rms=1137 | updated_at=1778068345.4258394
- [2026-05-06 19:52:29] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778068349.5174866 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:29] operator / voice_transcript_partial / voice: the what voice
  meta: kind=partial | timestamp=1778068349.7611837 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:30] operator / voice_transcript_partial / voice: the what voice human
  meta: kind=partial | timestamp=1778068350.2619758 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:30] operator / voice_transcript_partial / voice: the what voice want to
  meta: kind=partial | timestamp=1778068350.510203 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:31] operator / voice_transcript_partial / voice: the what voice want to ask
  meta: kind=partial | timestamp=1778068351.0755944 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:31] operator / voice_transcript_partial / voice: the what voice want to ask what is
  meta: kind=partial | timestamp=1778068351.2631547 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:31] operator / voice_transcript_partial / voice: the what voice want to ask what is the
  meta: kind=partial | timestamp=1778068351.514491 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:32] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions
  meta: kind=partial | timestamp=1778068352.014022 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:32] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions status
  meta: kind=partial | timestamp=1778068352.2647467 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:32] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions speak
  meta: kind=partial | timestamp=1778068352.5235944 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:32] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions speak enabled
  meta: kind=partial | timestamp=1778068352.773057 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:33] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions speak inversion
  meta: kind=partial | timestamp=1778068353.0133247 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:33] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions speak russian dmitry
  meta: kind=partial | timestamp=1778068353.2608907 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:33] operator / voice_transcript_partial / voice: the what voice want to ask what is the actions speak russian voice
  meta: kind=partial | timestamp=1778068353.5232847 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:34] operator / voice_transcript_final / voice: the what voice want to ask what is the actions speak in a russian voice
  meta: kind=final | timestamp=1778068354.6187775 | source=final | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:50] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778068370.5121305 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:50] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:52:50] operator / voice_transcript_partial / voice: video display
  meta: kind=partial | timestamp=1778068370.7731373 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:51] operator / voice_transcript_partial / voice: video speak
  meta: kind=partial | timestamp=1778068371.0105848 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:51] operator / voice_transcript_partial / voice: video speak enabled
  meta: kind=partial | timestamp=1778068371.2718167 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:51] operator / voice_transcript_partial / voice: video speak to russian
  meta: kind=partial | timestamp=1778068371.5205905 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:52] operator / voice_transcript_partial / voice: video speak to russian voice
  meta: kind=partial | timestamp=1778068372.0143814 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:52:52] operator / voice_transcript_final / voice: video speak to russian voice
  meta: kind=final | timestamp=1778068372.8821259 | source=final | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:05] operator / voice_transcript_partial / voice: overlay
  meta: kind=partial | timestamp=1778068385.0360944 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:05] operator / voice_transcript_final / voice: overlay
  meta: kind=final | timestamp=1778068385.6286395 | source=final | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:10] operator / voice_transcript_partial / voice: resume the accessory
  meta: kind=partial | timestamp=1778068390.053812 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:10] operator / voice_transcript_partial / voice: resume execution
  meta: kind=partial | timestamp=1778068390.3034637 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:10] operator / voice_transcript_partial / voice: recent logs
  meta: kind=partial | timestamp=1778068390.5456593 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:10] operator / voice_transcript_final / voice: recent logs
  meta: kind=final | timestamp=1778068390.9329634 | source=final | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:24] operator / voice_transcript_partial / voice: the face
  meta: kind=partial | timestamp=1778068404.2992904 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:24] operator / voice_transcript_partial / voice: the face name
  meta: kind=partial | timestamp=1778068404.544887 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:24] operator / voice_transcript_partial / voice: the face lion
  meta: kind=partial | timestamp=1778068404.7974405 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:25] operator / voice_transcript_partial / voice: the face greeting
  meta: kind=partial | timestamp=1778068405.2947774 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:25] operator / voice_transcript_partial / voice: the face lion current
  meta: kind=partial | timestamp=1778068405.546962 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:25] operator / voice_transcript_partial / voice: the face lion current status
  meta: kind=partial | timestamp=1778068405.7971866 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:26] operator / voice_transcript_partial / voice: the face lion current status logging
  meta: kind=partial | timestamp=1778068406.3249307 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:53:28] assistant / spoken_confirmation / voice: I am here. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 19:53:31] operator / voice_transcript_partial / voice: i have e active
  meta: kind=partial | timestamp=1778068411.9671414 | source=vosk | frequency_hz=74.0 | rms=872 | updated_at=1778068349.2568083
- [2026-05-06 19:53:32] operator / voice_transcript_final / voice: ai e active
  meta: kind=final | timestamp=1778068412.9706368 | source=final | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:33] operator / voice_transcript_partial / voice: i ask a
  meta: kind=partial | timestamp=1778068413.3024964 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:34] operator / voice_transcript_partial / voice: i ask a voice
  meta: kind=partial | timestamp=1778068414.2955973 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:35] operator / voice_transcript_final / voice: i ask cue voice
  meta: kind=final | timestamp=1778068415.2585142 | source=final | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:51] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting
  meta: kind=partial | timestamp=1778068431.403929 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:52] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting gesture
  meta: kind=partial | timestamp=1778068432.15561 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:52] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of accessory output
  meta: kind=partial | timestamp=1778068432.1651266 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:52] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face
  meta: kind=partial | timestamp=1778068432.4009168 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:52] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face leon
  meta: kind=partial | timestamp=1778068432.65565 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:52] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face eileen
  meta: kind=partial | timestamp=1778068432.89001 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:53] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face hello
  meta: kind=partial | timestamp=1778068433.1418676 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:53] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face eileen current status
  meta: kind=partial | timestamp=1778068433.4055023 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:53] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face eileen current stay guard
  meta: kind=partial | timestamp=1778068433.9113333 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:54] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face eileen current stay guard enabled
  meta: kind=partial | timestamp=1778068434.138289 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:54] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound of greeting of face eileen current stay guard alion
  meta: kind=partial | timestamp=1778068434.3935132 | source=vosk | frequency_hz=374.0 | rms=557 | updated_at=1778068412.3465037
- [2026-05-06 19:53:54] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:54:03] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi
  meta: kind=partial | timestamp=1778068443.9468882 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:04] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi activate
  meta: kind=partial | timestamp=1778068444.1921015 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:04] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi a
  meta: kind=partial | timestamp=1778068444.4469466 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:04] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi a disable the
  meta: kind=partial | timestamp=1778068444.689609 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:05] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi a disable the of laser
  meta: kind=partial | timestamp=1778068445.191598 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:05] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi a disable the of alion what
  meta: kind=partial | timestamp=1778068445.4410634 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:07] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 19:54:06] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml training hi a disable the of laser
  meta: kind=partial | timestamp=1778068446.0312457 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:06] operator / voice_transcript_final / voice: acoustic guard detection on visual sound ml training hi a disable the of laser
  meta: kind=final | timestamp=1778068446.2748158 | source=final | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:07] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778068447.133107 | source=vosk | frequency_hz=196.0 | rms=659 | updated_at=1778068437.9336
- [2026-05-06 19:54:08] operator / voice_transcript_final / voice: current
  meta: kind=final | timestamp=1778068448.4052508 | source=final | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:08] operator / voice_transcript_partial / voice: the manual
  meta: kind=partial | timestamp=1778068448.4273286 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:08] operator / voice_transcript_partial / voice: ml setting
  meta: kind=partial | timestamp=1778068448.6837568 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:08] operator / voice_transcript_partial / voice: ml
  meta: kind=partial | timestamp=1778068448.9239469 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:09] operator / voice_transcript_final / voice: commands
  meta: kind=final | timestamp=1778068449.5529857 | source=final | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:09] operator / voice_transcript_partial / voice: buzzer
  meta: kind=partial | timestamp=1778068449.676686 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:10] operator / voice_transcript_final / voice: listening
  meta: kind=final | timestamp=1778068450.988827 | source=final | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:12] operator / voice_transcript_partial / voice: order
  meta: kind=partial | timestamp=1778068452.5532284 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:13] operator / voice_transcript_partial / voice: reporting
  meta: kind=partial | timestamp=1778068453.3052704 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:13] operator / voice_transcript_partial / voice: spoken
  meta: kind=partial | timestamp=1778068453.6075578 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:13] operator / voice_transcript_partial / voice: spoken acoustic
  meta: kind=partial | timestamp=1778068453.8101127 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:14] operator / voice_transcript_partial / voice: spoken acoustic guard
  meta: kind=partial | timestamp=1778068454.0633 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278
- [2026-05-06 19:54:14] operator / voice_transcript_partial / voice: spoken acoustic guard disabled
  meta: kind=partial | timestamp=1778068454.3010905 | source=vosk | frequency_hz=145.0 | rms=317 | updated_at=1778068447.3772278

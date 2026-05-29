# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-05 00:33:26
- Entries: 996
- Roles: {'assistant': 60, 'system': 1, 'operator': 935}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 2, 'voice_status': 1, 'voice_transcript_partial': 650, 'voice_transcript_final': 163, 'spoken_confirmation': 54, 'voice_command': 122, 'spoken_reply': 2}
- Channels: {'text': 4, 'voice': 992}
- Latest operator request: the
- Latest assistant message: That does not match a known command. Please repeat.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 00:14:14] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:14:14] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:14:15] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777911255.7741163 | source=vosk
- [2026-05-05 00:14:17] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777911257.3023689 | source=vosk | frequency_hz=106.0 | rms=1203 | updated_at=1777911256.2958462
- [2026-05-05 00:14:17] operator / voice_transcript_partial / voice: strict on
  meta: kind=partial | timestamp=1777911257.5523329 | source=vosk | frequency_hz=106.0 | rms=1203 | updated_at=1777911256.2958462
- [2026-05-05 00:14:17] operator / voice_transcript_partial / voice: strict that again
  meta: kind=partial | timestamp=1777911257.8038108 | source=vosk | frequency_hz=106.0 | rms=1203 | updated_at=1777911256.2958462
- [2026-05-05 00:14:18] operator / voice_transcript_partial / voice: strict on commands
  meta: kind=partial | timestamp=1777911258.0570333 | source=vosk | frequency_hz=106.0 | rms=1203 | updated_at=1777911256.2958462
- [2026-05-05 00:14:18] operator / voice_transcript_partial / voice: strict on
  meta: kind=partial | timestamp=1777911258.3028436 | source=vosk | frequency_hz=106.0 | rms=1203 | updated_at=1777911256.2958462
- [2026-05-05 00:14:18] operator / voice_transcript_final / voice: strict on to
  meta: kind=final | timestamp=1777911258.5575428 | source=final | frequency_hz=106.0 | rms=1203 | updated_at=1777911256.2958462
- [2026-05-05 00:14:20] assistant / spoken_confirmation / voice: Elion is ready. Say a task and I will execute it step by step.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:14:22] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777911262.3020265 | source=vosk | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:22] operator / voice_transcript_partial / voice: stop that
  meta: kind=partial | timestamp=1777911262.5516772 | source=vosk | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:22] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777911262.8021061 | source=vosk | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:23] operator / voice_transcript_final / voice: stop that
  meta: kind=final | timestamp=1777911263.0551896 | source=final | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:23] operator / voice_command / voice: stop that
  meta: normalized=True
- [2026-05-05 00:14:23] assistant / spoken_confirmation / voice: There was no active task to cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:14:26] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911266.552906 | source=vosk | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:26] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777911266.8057969 | source=vosk | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:27] operator / voice_transcript_final / voice: do it
  meta: kind=final | timestamp=1777911267.3035471 | source=final | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:50] operator / voice_command / voice: do it
  meta: normalized=True
- [2026-05-05 00:14:30] operator / voice_transcript_partial / voice: mind
  meta: kind=partial | timestamp=1777911270.051309 | source=vosk | frequency_hz=322.1 | rms=286 | updated_at=1777911261.2961397
- [2026-05-05 00:14:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777911270.802051 | source=vosk | frequency_hz=320.0 | rms=286 | updated_at=1777911270.5456991
- [2026-05-05 00:14:31] operator / voice_transcript_partial / voice: the com
  meta: kind=partial | timestamp=1777911271.347889 | source=vosk | frequency_hz=332.6 | rms=292 | updated_at=1777911271.3406785
- [2026-05-05 00:14:31] operator / voice_transcript_final / voice: theme
  meta: kind=final | timestamp=1777911271.5568259 | source=final | frequency_hz=332.6 | rms=292 | updated_at=1777911271.3406785
- [2026-05-05 00:14:50] operator / voice_command / voice: theme
  meta: normalized=True
- [2026-05-05 00:14:31] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777911271.8056133 | source=vosk | frequency_hz=332.6 | rms=292 | updated_at=1777911271.3406785
- [2026-05-05 00:14:32] operator / voice_transcript_partial / voice: aileen analyze
  meta: kind=partial | timestamp=1777911272.8014276 | source=vosk | frequency_hz=332.6 | rms=292 | updated_at=1777911271.3406785
- [2026-05-05 00:14:33] operator / voice_transcript_partial / voice: eileen on commands
  meta: kind=partial | timestamp=1777911273.0544345 | source=vosk | frequency_hz=332.6 | rms=292 | updated_at=1777911271.3406785
- [2026-05-05 00:14:33] operator / voice_transcript_final / voice: the on commands
  meta: kind=final | timestamp=1777911273.8037438 | source=final | frequency_hz=404.0 | rms=319 | updated_at=1777911273.2966907
- [2026-05-05 00:14:50] operator / voice_command / voice: the on commands
  meta: normalized=True
- [2026-05-05 00:14:34] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777911274.0524633 | source=vosk | frequency_hz=404.0 | rms=319 | updated_at=1777911273.2966907
- [2026-05-05 00:14:39] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911279.3021975 | source=vosk | frequency_hz=286.5 | rms=327 | updated_at=1777911279.046018
- [2026-05-05 00:14:39] operator / voice_transcript_partial / voice: speed the decrease
  meta: kind=partial | timestamp=1777911279.8038673 | source=vosk | frequency_hz=286.5 | rms=327 | updated_at=1777911279.046018
- [2026-05-05 00:14:40] operator / voice_transcript_partial / voice: speed to the smart
  meta: kind=partial | timestamp=1777911280.301626 | source=vosk | frequency_hz=286.5 | rms=327 | updated_at=1777911279.046018
- [2026-05-05 00:14:40] operator / voice_transcript_partial / voice: speed the decrease
  meta: kind=partial | timestamp=1777911280.5522058 | source=vosk | frequency_hz=412.0 | rms=300 | updated_at=1777911280.5460393
- [2026-05-05 00:14:41] operator / voice_transcript_final / voice: speed the decrease
  meta: kind=final | timestamp=1777911281.303653 | source=final | frequency_hz=412.0 | rms=254 | updated_at=1777911281.0476334
- [2026-05-05 00:14:50] operator / voice_command / voice: speed the decrease
  meta: normalized=True
- [2026-05-05 00:14:42] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777911282.550991 | source=vosk | frequency_hz=412.0 | rms=254 | updated_at=1777911281.0476334
- [2026-05-05 00:14:42] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911282.802992 | source=vosk | frequency_hz=412.0 | rms=254 | updated_at=1777911281.0476334
- [2026-05-05 00:14:43] operator / voice_transcript_partial / voice: response delay
  meta: kind=partial | timestamp=1777911283.0540972 | source=vosk | frequency_hz=412.0 | rms=254 | updated_at=1777911281.0476334
- [2026-05-05 00:14:43] operator / voice_transcript_partial / voice: response disconnect
  meta: kind=partial | timestamp=1777911283.553935 | source=vosk | frequency_hz=412.0 | rms=254 | updated_at=1777911281.0476334
- [2026-05-05 00:14:43] operator / voice_transcript_final / voice: response decrease
  meta: kind=final | timestamp=1777911283.8068535 | source=final | frequency_hz=412.0 | rms=254 | updated_at=1777911281.0476334
- [2026-05-05 00:14:50] operator / voice_command / voice: response decrease
  meta: normalized=True
- [2026-05-05 00:14:47] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777911287.5527167 | source=vosk | frequency_hz=271.7 | rms=263 | updated_at=1777911286.5466564
- [2026-05-05 00:14:48] operator / voice_transcript_partial / voice: silence
  meta: kind=partial | timestamp=1777911288.0519059 | source=vosk | frequency_hz=271.7 | rms=263 | updated_at=1777911286.5466564
- [2026-05-05 00:14:48] operator / voice_transcript_partial / voice: last go
  meta: kind=partial | timestamp=1777911288.301968 | source=vosk | frequency_hz=271.7 | rms=263 | updated_at=1777911286.5466564
- [2026-05-05 00:14:48] operator / voice_transcript_final / voice: last
  meta: kind=final | timestamp=1777911288.5542598 | source=final | frequency_hz=271.7 | rms=263 | updated_at=1777911286.5466564
- [2026-05-05 00:14:48] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777911288.8027358 | source=vosk | frequency_hz=271.7 | rms=263 | updated_at=1777911286.5466564
- [2026-05-05 00:14:49] operator / voice_transcript_partial / voice: on commands
  meta: kind=partial | timestamp=1777911289.0516665 | source=vosk | frequency_hz=271.7 | rms=263 | updated_at=1777911286.5466564
- [2026-05-05 00:14:49] operator / voice_transcript_final / voice: on again
  meta: kind=final | timestamp=1777911289.5534842 | source=final | frequency_hz=268.0 | rms=246 | updated_at=1777911289.2968853
- [2026-05-05 00:14:50] assistant / spoken_confirmation / voice: What do you want me to do next? I can resume autodetection and guarding mode, stay paused, or run another task.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:14:53] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777911293.30375 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:53] operator / voice_transcript_partial / voice: on commands
  meta: kind=partial | timestamp=1777911293.813625 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:54] operator / voice_transcript_final / voice: on commands
  meta: kind=final | timestamp=1777911294.5558605 | source=final | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:55] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911295.553672 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:55] operator / voice_transcript_partial / voice: do you do
  meta: kind=partial | timestamp=1777911295.8066719 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:56] operator / voice_transcript_partial / voice: do you do brightness
  meta: kind=partial | timestamp=1777911296.055216 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:56] operator / voice_transcript_partial / voice: do you do threshold
  meta: kind=partial | timestamp=1777911296.305122 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:56] operator / voice_transcript_partial / voice: do you do brightness
  meta: kind=partial | timestamp=1777911296.5521264 | source=vosk | frequency_hz=315.6 | rms=248 | updated_at=1777911292.7989001
- [2026-05-05 00:14:57] operator / voice_transcript_final / voice: do you do brightness
  meta: kind=final | timestamp=1777911297.0569546 | source=final | frequency_hz=392.0 | rms=268 | updated_at=1777911297.0470097
- [2026-05-05 00:14:58] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777911298.5558681 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:14:58] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777911298.8034637 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:14:59] operator / voice_transcript_partial / voice: to com do
  meta: kind=partial | timestamp=1777911299.0614965 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:14:59] operator / voice_transcript_partial / voice: to com do you do
  meta: kind=partial | timestamp=1777911299.5528653 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:14:59] operator / voice_transcript_partial / voice: to com do strict on
  meta: kind=partial | timestamp=1777911299.8045118 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:15:00] operator / voice_transcript_partial / voice: to com do strict to
  meta: kind=partial | timestamp=1777911300.313857 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:15:00] operator / voice_transcript_partial / voice: to com do strict decrease
  meta: kind=partial | timestamp=1777911300.5552957 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:15:00] operator / voice_transcript_partial / voice: to com do strict decrease tracking
  meta: kind=partial | timestamp=1777911300.8046658 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:15:01] operator / voice_transcript_partial / voice: to com do strict decrease decrease
  meta: kind=partial | timestamp=1777911301.055605 | source=vosk | frequency_hz=366.4 | rms=287 | updated_at=1777911298.0475512
- [2026-05-05 00:15:01] operator / voice_transcript_partial / voice: to com do strict decrease decrease decrease
  meta: kind=partial | timestamp=1777911301.5539854 | source=vosk | frequency_hz=268.0 | rms=262 | updated_at=1777911301.5469625
- [2026-05-05 00:15:02] operator / voice_transcript_final / voice: to com do strict decrease decrease decrease
  meta: kind=final | timestamp=1777911302.3050687 | source=final | frequency_hz=287.1 | rms=272 | updated_at=1777911302.2969766
- [2026-05-05 00:15:03] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1777911303.3029075 | source=vosk | frequency_hz=329.4 | rms=280 | updated_at=1777911302.5480392
- [2026-05-05 00:15:03] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:15:03] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777911303.980938 | source=vosk | frequency_hz=340.0 | rms=273 | updated_at=1777911303.9709094
- [2026-05-05 00:15:05] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777911305.171047 | source=final | frequency_hz=322.6 | rms=834 | updated_at=1777911304.721059
- [2026-05-05 00:15:06] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911306.4777868 | source=vosk | frequency_hz=366.0 | rms=273 | updated_at=1777911305.2210977
- [2026-05-05 00:15:06] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911306.9783163 | source=vosk | frequency_hz=366.0 | rms=273 | updated_at=1777911305.2210977
- [2026-05-05 00:15:09] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911309.729266 | source=final | frequency_hz=341.2 | rms=269 | updated_at=1777911309.7212145
- [2026-05-05 00:15:09] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:15:10] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911310.9840243 | source=vosk | frequency_hz=341.2 | rms=269 | updated_at=1777911309.7212145
- [2026-05-05 00:15:14] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911314.9031122 | source=final | frequency_hz=350.9 | rms=272 | updated_at=1777911314.7221541
- [2026-05-05 00:15:14] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:15:16] operator / voice_transcript_partial / voice: boards and
  meta: kind=partial | timestamp=1777911316.2271805 | source=vosk | frequency_hz=337.3 | rms=281 | updated_at=1777911315.4711244
- [2026-05-05 00:15:16] operator / voice_transcript_partial / voice: abort
  meta: kind=partial | timestamp=1777911316.4773557 | source=vosk | frequency_hz=337.3 | rms=281 | updated_at=1777911315.4711244
- [2026-05-05 00:15:16] operator / voice_transcript_partial / voice: boards and enable lion
  meta: kind=partial | timestamp=1777911316.7297752 | source=vosk | frequency_hz=345.9 | rms=288 | updated_at=1777911316.7214084
- [2026-05-05 00:15:17] operator / voice_transcript_partial / voice: boards and enable lion be speed
  meta: kind=partial | timestamp=1777911317.9793348 | source=vosk | frequency_hz=345.9 | rms=288 | updated_at=1777911316.7214084
- [2026-05-05 00:15:18] operator / voice_transcript_partial / voice: boards and enable lion be speed on commands
  meta: kind=partial | timestamp=1777911318.4771736 | source=vosk | frequency_hz=345.9 | rms=288 | updated_at=1777911316.7214084
- [2026-05-05 00:15:18] operator / voice_transcript_final / voice: boards and abort lion be speed com again
  meta: kind=final | timestamp=1777911318.9892218 | source=final | frequency_hz=312.0 | rms=277 | updated_at=1777911318.9714856
- [2026-05-05 00:15:19] operator / voice_command / voice: boards and abort lion be speed com again
  meta: normalized=True
- [2026-05-05 00:15:21] operator / voice_transcript_partial / voice: to anything
  meta: kind=partial | timestamp=1777911321.4783652 | source=vosk | frequency_hz=266.4 | rms=280 | updated_at=1777911320.4724257
- [2026-05-05 00:15:21] operator / voice_transcript_partial / voice: to alion
  meta: kind=partial | timestamp=1777911321.7278957 | source=vosk | frequency_hz=266.4 | rms=280 | updated_at=1777911320.4724257
- [2026-05-05 00:15:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:15:26] operator / voice_transcript_partial / voice: silence
  meta: kind=partial | timestamp=1777911326.2615104 | source=vosk | frequency_hz=322.9 | rms=291 | updated_at=1777911325.2552745
- [2026-05-05 00:15:26] operator / voice_transcript_partial / voice: silence lion
  meta: kind=partial | timestamp=1777911326.7615278 | source=vosk | frequency_hz=322.9 | rms=291 | updated_at=1777911325.2552745
- [2026-05-05 00:15:27] operator / voice_transcript_partial / voice: silence a the
  meta: kind=partial | timestamp=1777911327.0160687 | source=vosk | frequency_hz=322.9 | rms=291 | updated_at=1777911325.2552745
- [2026-05-05 00:15:27] operator / voice_transcript_partial / voice: silence a be less
  meta: kind=partial | timestamp=1777911327.2630122 | source=vosk | frequency_hz=322.9 | rms=291 | updated_at=1777911325.2552745
- [2026-05-05 00:15:27] operator / voice_transcript_partial / voice: silence eileen abort current
  meta: kind=partial | timestamp=1777911327.510519 | source=vosk | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:27] operator / voice_transcript_partial / voice: silence eileen abort
  meta: kind=partial | timestamp=1777911327.7623913 | source=vosk | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:28] operator / voice_transcript_partial / voice: silence eileen abort last
  meta: kind=partial | timestamp=1777911328.0153139 | source=vosk | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:28] operator / voice_transcript_partial / voice: silence eileen abort lion
  meta: kind=partial | timestamp=1777911328.26403 | source=vosk | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:28] operator / voice_transcript_final / voice: same lion the abort delay that
  meta: kind=final | timestamp=1777911328.5244296 | source=final | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:28] operator / voice_command / voice: same lion the abort delay that
  meta: normalized=True
- [2026-05-05 00:15:28] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911328.7613273 | source=vosk | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:29] operator / voice_transcript_partial / voice: smart lion
  meta: kind=partial | timestamp=1777911329.0113652 | source=vosk | frequency_hz=340.0 | rms=310 | updated_at=1777911327.504997
- [2026-05-05 00:15:29] operator / voice_transcript_partial / voice: smart lion be
  meta: kind=partial | timestamp=1777911329.513519 | source=vosk | frequency_hz=388.0 | rms=327 | updated_at=1777911329.505495
- [2026-05-05 00:15:29] operator / voice_transcript_partial / voice: smart lion be less
  meta: kind=partial | timestamp=1777911329.7609022 | source=vosk | frequency_hz=388.0 | rms=327 | updated_at=1777911329.505495
- [2026-05-05 00:15:30] operator / voice_transcript_partial / voice: smart lion be more strict
  meta: kind=partial | timestamp=1777911330.262475 | source=vosk | frequency_hz=344.6 | rms=287 | updated_at=1777911330.2564626
- [2026-05-05 00:15:30] operator / voice_transcript_final / voice: smart lion be less board
  meta: kind=final | timestamp=1777911330.763103 | source=final | frequency_hz=341.9 | rms=291 | updated_at=1777911330.7556171
- [2026-05-05 00:15:30] operator / voice_command / voice: smart lion be less board
  meta: normalized=True
- [2026-05-05 00:15:33] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777911333.0179417 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:33] operator / voice_transcript_partial / voice: same silence
  meta: kind=partial | timestamp=1777911333.2627554 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:33] operator / voice_transcript_partial / voice: same silence threshold
  meta: kind=partial | timestamp=1777911333.5199249 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:34] operator / voice_transcript_partial / voice: same silence current
  meta: kind=partial | timestamp=1777911334.2614758 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:34] operator / voice_transcript_partial / voice: same silence are never
  meta: kind=partial | timestamp=1777911334.5140905 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:34] operator / voice_transcript_partial / voice: same silence current app
  meta: kind=partial | timestamp=1777911334.7612307 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:35] operator / voice_transcript_partial / voice: same silence current app behavior
  meta: kind=partial | timestamp=1777911335.2626336 | source=vosk | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:35] operator / voice_transcript_final / voice: same silence current app behavior
  meta: kind=final | timestamp=1777911335.7649014 | source=final | frequency_hz=377.4 | rms=295 | updated_at=1777911332.0076492
- [2026-05-05 00:15:35] operator / voice_command / voice: same silence current app behavior
  meta: normalized=True
- [2026-05-05 00:15:37] assistant / spoken_confirmation / voice: Received. I started your background analysis about same silence current app behavior in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:15:37] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777911337.2660015 | source=vosk | frequency_hz=339.6 | rms=292 | updated_at=1777911336.5050943
- [2026-05-05 00:15:37] operator / voice_transcript_partial / voice: lion override
  meta: kind=partial | timestamp=1777911337.5195246 | source=vosk | frequency_hz=339.6 | rms=292 | updated_at=1777911336.5050943
- [2026-05-05 00:15:37] operator / voice_transcript_partial / voice: lion mode
  meta: kind=partial | timestamp=1777911337.763974 | source=vosk | frequency_hz=320.1 | rms=298 | updated_at=1777911337.7559192
- [2026-05-05 00:15:38] operator / voice_transcript_final / voice: lion mode
  meta: kind=final | timestamp=1777911338.5138798 | source=final | frequency_hz=251.7 | rms=293 | updated_at=1777911338.5063663
- [2026-05-05 00:15:38] operator / voice_command / voice: lion mode
  meta: normalized=True
- [2026-05-05 00:15:40] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777911340.0177817 | source=vosk | frequency_hz=251.8 | rms=290 | updated_at=1777911339.5055308
- [2026-05-05 00:15:40] operator / voice_transcript_partial / voice: go current
  meta: kind=partial | timestamp=1777911340.267713 | source=vosk | frequency_hz=251.8 | rms=290 | updated_at=1777911339.5055308
- [2026-05-05 00:15:40] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911340.5119026 | source=vosk | frequency_hz=251.8 | rms=290 | updated_at=1777911339.5055308
- [2026-05-05 00:15:41] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1777911341.0180404 | source=final | frequency_hz=293.1 | rms=294 | updated_at=1777911341.0060282
- [2026-05-05 00:15:41] operator / voice_command / voice: go
  meta: normalized=True
- [2026-05-05 00:15:43] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777911343.0140781 | source=vosk | frequency_hz=350.1 | rms=321 | updated_at=1777911343.0060406
- [2026-05-05 00:15:44] operator / voice_transcript_final / voice: lion
  meta: kind=final | timestamp=1777911344.0759964 | source=final | frequency_hz=308.1 | rms=302 | updated_at=1777911344.0060995
- [2026-05-05 00:15:44] operator / voice_command / voice: lion
  meta: normalized=True
- [2026-05-05 00:15:44] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777911344.5148714 | source=vosk | frequency_hz=308.1 | rms=302 | updated_at=1777911344.0060995
- [2026-05-05 00:15:44] operator / voice_transcript_partial / voice: to no
  meta: kind=partial | timestamp=1777911344.7737234 | source=vosk | frequency_hz=308.1 | rms=302 | updated_at=1777911344.0060995
- [2026-05-05 00:16:11] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777911371.0577178 | source=vosk | frequency_hz=309.0 | rms=273 | updated_at=1777911369.8046641
- [2026-05-05 00:16:11] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911371.5713372 | source=vosk | frequency_hz=309.0 | rms=273 | updated_at=1777911369.8046641
- [2026-05-05 00:16:12] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777911372.3102765 | source=final | frequency_hz=309.0 | rms=273 | updated_at=1777911369.8046641
- [2026-05-05 00:16:15] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777911375.8075085 | source=vosk | frequency_hz=338.3 | rms=272 | updated_at=1777911374.7996676
- [2026-05-05 00:16:16] operator / voice_transcript_partial / voice: lion decrease
  meta: kind=partial | timestamp=1777911376.3127706 | source=vosk | frequency_hz=338.3 | rms=272 | updated_at=1777911374.7996676
- [2026-05-05 00:16:16] operator / voice_transcript_partial / voice: what do you do
  meta: kind=partial | timestamp=1777911376.5638394 | source=vosk | frequency_hz=338.3 | rms=272 | updated_at=1777911374.7996676
- [2026-05-05 00:16:16] operator / voice_transcript_partial / voice: lion decrease
  meta: kind=partial | timestamp=1777911376.821898 | source=vosk | frequency_hz=338.3 | rms=272 | updated_at=1777911374.7996676
- [2026-05-05 00:16:17] operator / voice_transcript_final / voice: what do you do yes
  meta: kind=final | timestamp=1777911377.809675 | source=final | frequency_hz=314.9 | rms=269 | updated_at=1777911377.800166
- [2026-05-05 00:16:21] assistant / assistant_analysis / text: Assistant update. Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Runtime facts: state=PAUSED | camera_open=True | yolo_loaded=True | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=water burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Reconnect the controller link before expecting movement, trigger commands, or live bridge telemetry. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. - [high] Controller link offline: The sentry is not currently connected to its controller link. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:16:30] operator / voice_transcript_partial / voice: abort
  meta: kind=partial | timestamp=1777911390.823922 | source=vosk | frequency_hz=347.6 | rms=310 | updated_at=1777911390.8169153
- [2026-05-05 00:16:45] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777911405.938478 | source=vosk | frequency_hz=340.8 | rms=288 | updated_at=1777911405.4316573
- [2026-05-05 00:16:46] operator / voice_transcript_partial / voice: theme
  meta: kind=partial | timestamp=1777911406.6904702 | source=vosk | frequency_hz=340.8 | rms=288 | updated_at=1777911405.4316573
- [2026-05-05 00:16:47] operator / voice_transcript_partial / voice: theme alien be
  meta: kind=partial | timestamp=1777911407.4394422 | source=vosk | frequency_hz=264.0 | rms=286 | updated_at=1777911406.9321542
- [2026-05-05 00:16:48] operator / voice_transcript_final / voice: theme be
  meta: kind=final | timestamp=1777911408.7025208 | source=final | frequency_hz=278.2 | rms=292 | updated_at=1777911408.6816316
- [2026-05-05 00:16:48] operator / voice_command / voice: theme be
  meta: normalized=True
- [2026-05-05 00:16:49] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:16:49] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911409.691383 | source=vosk | frequency_hz=278.2 | rms=292 | updated_at=1777911408.6816316
- [2026-05-05 00:17:02] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777911422.5244405 | source=vosk | frequency_hz=366.0 | rms=1204 | updated_at=1777911422.513909
- [2026-05-05 00:17:03] operator / voice_transcript_partial / voice: mind
  meta: kind=partial | timestamp=1777911423.7701778 | source=vosk | frequency_hz=366.0 | rms=1204 | updated_at=1777911422.513909
- [2026-05-05 00:17:04] operator / voice_transcript_partial / voice: run diagnostics
  meta: kind=partial | timestamp=1777911424.0246966 | source=vosk | frequency_hz=366.0 | rms=1204 | updated_at=1777911422.513909
- [2026-05-05 00:17:04] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911424.2705376 | source=vosk | frequency_hz=366.0 | rms=1204 | updated_at=1777911422.513909
- [2026-05-05 00:17:04] operator / voice_transcript_partial / voice: [unk] connect
  meta: kind=partial | timestamp=1777911424.519758 | source=vosk | frequency_hz=366.0 | rms=1204 | updated_at=1777911422.513909
- [2026-05-05 00:17:04] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911424.76993 | source=vosk | frequency_hz=366.0 | rms=1204 | updated_at=1777911422.513909
- [2026-05-05 00:17:08] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911428.2790523 | source=final | frequency_hz=266.4 | rms=321 | updated_at=1777911428.2653773
- [2026-05-05 00:17:10] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911430.0205212 | source=vosk | frequency_hz=247.3 | rms=322 | updated_at=1777911429.51382
- [2026-05-05 00:17:10] operator / voice_transcript_partial / voice: disable
  meta: kind=partial | timestamp=1777911430.27552 | source=vosk | frequency_hz=247.3 | rms=322 | updated_at=1777911429.51382
- [2026-05-05 00:17:11] operator / voice_transcript_partial / voice: disable queued
  meta: kind=partial | timestamp=1777911431.527136 | source=vosk | frequency_hz=247.3 | rms=322 | updated_at=1777911429.51382
- [2026-05-05 00:17:19] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911439.2654314 | source=vosk | frequency_hz=292.8 | rms=329 | updated_at=1777911438.504782
- [2026-05-05 00:17:19] operator / voice_transcript_partial / voice: delay and enable
  meta: kind=partial | timestamp=1777911439.7635195 | source=vosk | frequency_hz=292.8 | rms=329 | updated_at=1777911438.504782
- [2026-05-05 00:17:20] operator / voice_transcript_final / voice: delay and
  meta: kind=final | timestamp=1777911440.5141096 | source=final | frequency_hz=416.0 | rms=376 | updated_at=1777911440.005918
- [2026-05-05 00:17:27] operator / voice_transcript_partial / voice: com
  meta: kind=partial | timestamp=1777911447.2699506 | source=vosk | frequency_hz=261.9 | rms=326 | updated_at=1777911446.25542
- [2026-05-05 00:17:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777911450.7632127 | source=vosk | frequency_hz=333.4 | rms=368 | updated_at=1777911449.2560513
- [2026-05-05 00:17:31] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777911451.7609594 | source=vosk | frequency_hz=333.4 | rms=368 | updated_at=1777911449.2560513
- [2026-05-05 00:17:32] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777911452.0131075 | source=vosk | frequency_hz=333.4 | rms=368 | updated_at=1777911449.2560513
- [2026-05-05 00:17:43] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911463.712252 | source=vosk | frequency_hz=339.0 | rms=323 | updated_at=1777911463.206827
- [2026-05-05 00:17:44] operator / voice_transcript_partial / voice: speed do e
  meta: kind=partial | timestamp=1777911464.2130845 | source=vosk | frequency_hz=339.0 | rms=323 | updated_at=1777911463.206827
- [2026-05-05 00:17:44] operator / voice_transcript_partial / voice: speed do e priority
  meta: kind=partial | timestamp=1777911464.4639902 | source=vosk | frequency_hz=339.0 | rms=323 | updated_at=1777911463.206827
- [2026-05-05 00:17:44] operator / voice_transcript_final / voice: speed do unk
  meta: kind=final | timestamp=1777911464.715498 | source=final | frequency_hz=339.0 | rms=323 | updated_at=1777911463.206827
- [2026-05-05 00:17:45] operator / voice_transcript_partial / voice: priority
  meta: kind=partial | timestamp=1777911465.4631584 | source=vosk | frequency_hz=272.0 | rms=339 | updated_at=1777911464.9564946
- [2026-05-05 00:17:45] operator / voice_transcript_partial / voice: but faster
  meta: kind=partial | timestamp=1777911465.9641016 | source=vosk | frequency_hz=269.2 | rms=317 | updated_at=1777911465.9572535
- [2026-05-05 00:17:46] operator / voice_transcript_final / voice: but
  meta: kind=final | timestamp=1777911466.7156806 | source=final | frequency_hz=271.8 | rms=326 | updated_at=1777911466.706648
- [2026-05-05 00:17:47] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1777911467.4635475 | source=vosk | frequency_hz=271.8 | rms=326 | updated_at=1777911466.706648
- [2026-05-05 00:17:47] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1777911467.714701 | source=vosk | frequency_hz=271.8 | rms=326 | updated_at=1777911466.706648
- [2026-05-05 00:17:47] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:17:47] operator / voice_transcript_partial / voice: repeat that
  meta: kind=partial | timestamp=1777911467.9676719 | source=vosk | frequency_hz=313.9 | rms=329 | updated_at=1777911467.9610035
- [2026-05-05 00:17:49] operator / voice_transcript_final / voice: do you it repeat that
  meta: kind=final | timestamp=1777911469.017159 | source=final | frequency_hz=295.9 | rms=358 | updated_at=1777911468.4571846
- [2026-05-05 00:17:49] operator / voice_command / voice: do you it repeat that
  meta: normalized=True
- [2026-05-05 00:17:49] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777911469.4706478 | source=vosk | frequency_hz=318.7 | rms=371 | updated_at=1777911469.2143524
- [2026-05-05 00:17:50] assistant / spoken_confirmation / voice: There is no recent command to repeat yet.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:17:50] operator / voice_transcript_partial / voice: boards and enable
  meta: kind=partial | timestamp=1777911470.3738477 | source=vosk | frequency_hz=316.4 | rms=338 | updated_at=1777911469.9575982
- [2026-05-05 00:18:13] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911493.7729766 | source=vosk | frequency_hz=220.6 | rms=319 | updated_at=1777911493.2599452
- [2026-05-05 00:18:14] operator / voice_transcript_partial / voice: speed to anything
  meta: kind=partial | timestamp=1777911494.2666457 | source=vosk | frequency_hz=220.6 | rms=319 | updated_at=1777911493.2599452
- [2026-05-05 00:18:14] operator / voice_transcript_partial / voice: speed to mind diagnostics
  meta: kind=partial | timestamp=1777911494.517729 | source=vosk | frequency_hz=220.6 | rms=319 | updated_at=1777911493.2599452
- [2026-05-05 00:18:15] operator / voice_transcript_final / voice: speed to unk
  meta: kind=final | timestamp=1777911495.0174227 | source=final | frequency_hz=232.0 | rms=328 | updated_at=1777911495.009406
- [2026-05-05 00:18:19] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777911499.7671046 | source=vosk | frequency_hz=336.4 | rms=343 | updated_at=1777911499.509884
- [2026-05-05 00:18:21] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911501.5170326 | source=vosk | frequency_hz=336.4 | rms=343 | updated_at=1777911499.509884
- [2026-05-05 00:18:22] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777911502.0203474 | source=vosk | frequency_hz=336.4 | rms=343 | updated_at=1777911499.509884
- [2026-05-05 00:18:22] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911502.2656188 | source=vosk | frequency_hz=336.4 | rms=343 | updated_at=1777911499.509884
- [2026-05-05 00:18:25] operator / voice_transcript_final / voice: yourself
  meta: kind=final | timestamp=1777911505.0186498 | source=final | frequency_hz=260.2 | rms=327 | updated_at=1777911504.759625
- [2026-05-05 00:18:25] operator / voice_transcript_partial / voice: repeat smart
  meta: kind=partial | timestamp=1777911505.7652745 | source=vosk | frequency_hz=260.2 | rms=327 | updated_at=1777911504.759625
- [2026-05-05 00:18:26] operator / voice_transcript_partial / voice: repeat smart sentry
  meta: kind=partial | timestamp=1777911506.020981 | source=vosk | frequency_hz=260.2 | rms=327 | updated_at=1777911504.759625
- [2026-05-05 00:18:26] operator / voice_transcript_final / voice: repeat smart
  meta: kind=final | timestamp=1777911506.767424 | source=final | frequency_hz=260.2 | rms=327 | updated_at=1777911504.759625
- [2026-05-05 00:18:28] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777911508.0183218 | source=vosk | frequency_hz=270.0 | rms=347 | updated_at=1777911507.510658
- [2026-05-05 00:18:28] operator / voice_transcript_partial / voice: less strict
  meta: kind=partial | timestamp=1777911508.7656546 | source=vosk | frequency_hz=270.0 | rms=347 | updated_at=1777911507.510658
- [2026-05-05 00:18:29] operator / voice_transcript_partial / voice: less say go
  meta: kind=partial | timestamp=1777911509.0176876 | source=vosk | frequency_hz=336.0 | rms=350 | updated_at=1777911509.0101776
- [2026-05-05 00:18:30] operator / voice_transcript_final / voice: less say go
  meta: kind=final | timestamp=1777911510.0262525 | source=final | frequency_hz=275.9 | rms=313 | updated_at=1777911510.0167224
- [2026-05-05 00:18:31] operator / voice_transcript_partial / voice: e delay
  meta: kind=partial | timestamp=1777911511.0168953 | source=vosk | frequency_hz=283.6 | rms=321 | updated_at=1777911510.5132
- [2026-05-05 00:18:50] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777911530.0098844 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:50] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777911530.2545922 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:50] operator / voice_transcript_partial / voice: resume to
  meta: kind=partial | timestamp=1777911530.4984243 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:50] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777911530.74937 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:51] operator / voice_transcript_partial / voice: resume last
  meta: kind=partial | timestamp=1777911531.2507975 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:51] operator / voice_transcript_partial / voice: resume last delay
  meta: kind=partial | timestamp=1777911531.7497091 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:52] operator / voice_transcript_partial / voice: resume last delay say
  meta: kind=partial | timestamp=1777911532.2499032 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:53] operator / voice_transcript_partial / voice: resume last delay say elliot
  meta: kind=partial | timestamp=1777911533.0007825 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:53] operator / voice_transcript_partial / voice: resume last delay say elliot response
  meta: kind=partial | timestamp=1777911533.2500858 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:53] operator / voice_transcript_partial / voice: resume last delay say elliot speed
  meta: kind=partial | timestamp=1777911533.4990492 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:54] operator / voice_transcript_partial / voice: resume last delay say elliot speed speed
  meta: kind=partial | timestamp=1777911534.0000603 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:54] operator / voice_transcript_partial / voice: resume last delay say elliot speed speed status
  meta: kind=partial | timestamp=1777911534.7494957 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:54] operator / voice_transcript_partial / voice: resume last delay say elliot speed speed strict go
  meta: kind=partial | timestamp=1777911534.9999793 | source=vosk | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:55] operator / voice_transcript_final / voice: resume last delay say speed speed the strict go
  meta: kind=final | timestamp=1777911535.7509465 | source=final | frequency_hz=353.4 | rms=266 | updated_at=1777911527.4937966
- [2026-05-05 00:18:55] operator / voice_command / voice: resume last delay say speed speed the strict go
  meta: normalized=True
- [2026-05-05 00:18:57] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:19:02] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777911542.2495182 | source=vosk | frequency_hz=301.3 | rms=284 | updated_at=1777911541.243703
- [2026-05-05 00:19:02] operator / voice_transcript_partial / voice: boards speed
  meta: kind=partial | timestamp=1777911542.5171025 | source=vosk | frequency_hz=301.3 | rms=284 | updated_at=1777911541.243703
- [2026-05-05 00:19:03] operator / voice_transcript_final / voice: boards speed
  meta: kind=final | timestamp=1777911543.9313328 | source=final | frequency_hz=301.3 | rms=284 | updated_at=1777911541.243703
- [2026-05-05 00:19:04] operator / voice_command / voice: boards speed
  meta: normalized=True
- [2026-05-05 00:19:04] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911544.2482152 | source=vosk | frequency_hz=301.3 | rms=284 | updated_at=1777911541.243703
- [2026-05-05 00:19:04] operator / voice_transcript_partial / voice: speed you
  meta: kind=partial | timestamp=1777911544.4993196 | source=vosk | frequency_hz=301.3 | rms=284 | updated_at=1777911541.243703
- [2026-05-05 00:19:05] operator / voice_transcript_partial / voice: speed yourself
  meta: kind=partial | timestamp=1777911545.1562264 | source=vosk | frequency_hz=336.0 | rms=278 | updated_at=1777911544.7437098
- [2026-05-05 00:19:05] operator / voice_transcript_partial / voice: speed you are you
  meta: kind=partial | timestamp=1777911545.1627371 | source=vosk | frequency_hz=330.4 | rms=278 | updated_at=1777911545.1562264
- [2026-05-05 00:19:05] operator / voice_transcript_final / voice: speed you are
  meta: kind=final | timestamp=1777911545.7509599 | source=final | frequency_hz=313.8 | rms=277 | updated_at=1777911545.743955
- [2026-05-05 00:19:05] operator / voice_command / voice: speed you are
  meta: normalized=True
- [2026-05-05 00:19:07] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:19:07] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:19:10] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777911550.0001712 | source=vosk | frequency_hz=304.8 | rms=281 | updated_at=1777911549.9951673
- [2026-05-05 00:19:10] operator / voice_transcript_final / voice: delay
  meta: kind=final | timestamp=1777911550.7517738 | source=final | frequency_hz=306.6 | rms=283 | updated_at=1777911550.2439642
- [2026-05-05 00:19:11] operator / voice_transcript_partial / voice: mode
  meta: kind=partial | timestamp=1777911551.7502894 | source=vosk | frequency_hz=324.6 | rms=388 | updated_at=1777911551.4938982
- [2026-05-05 00:19:12] operator / voice_transcript_partial / voice: mode no
  meta: kind=partial | timestamp=1777911552.5105217 | source=vosk | frequency_hz=304.4 | rms=280 | updated_at=1777911552.4964027
- [2026-05-05 00:19:13] operator / voice_transcript_final / voice: mode no
  meta: kind=final | timestamp=1777911553.0029588 | source=final | frequency_hz=309.9 | rms=293 | updated_at=1777911552.9949532
- [2026-05-05 00:19:15] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777911555.4995184 | source=vosk | frequency_hz=272.7 | rms=269 | updated_at=1777911554.499018
- [2026-05-05 00:19:16] operator / voice_transcript_final / voice: current
  meta: kind=final | timestamp=1777911556.2515936 | source=final | frequency_hz=272.7 | rms=269 | updated_at=1777911554.499018
- [2026-05-05 00:19:17] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777911557.7494516 | source=vosk | frequency_hz=420.0 | rms=721 | updated_at=1777911556.744424
- [2026-05-05 00:19:18] operator / voice_transcript_partial / voice: queued tasks
  meta: kind=partial | timestamp=1777911558.011956 | source=vosk | frequency_hz=420.0 | rms=721 | updated_at=1777911556.744424
- [2026-05-05 00:19:18] operator / voice_transcript_final / voice: queued do
  meta: kind=final | timestamp=1777911558.5774999 | source=final | frequency_hz=420.0 | rms=721 | updated_at=1777911556.744424
- [2026-05-05 00:19:20] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777911560.5011644 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:20] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911560.7503452 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:21] operator / voice_transcript_partial / voice: go to sentry
  meta: kind=partial | timestamp=1777911561.0006807 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:21] operator / voice_transcript_partial / voice: elian say that again
  meta: kind=partial | timestamp=1777911561.248984 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:19:21] operator / voice_transcript_partial / voice: elian say that do
  meta: kind=partial | timestamp=1777911561.5007153 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:21] operator / voice_transcript_partial / voice: elian say that again yourself
  meta: kind=partial | timestamp=1777911561.7533388 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:22] operator / voice_transcript_partial / voice: elian say that do status report
  meta: kind=partial | timestamp=1777911562.000789 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:22] operator / voice_transcript_partial / voice: elian say that do status report decrease
  meta: kind=partial | timestamp=1777911562.506908 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:23] operator / voice_transcript_partial / voice: elian say that do status report the queue
  meta: kind=partial | timestamp=1777911563.000977 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:19:23] operator / voice_transcript_partial / voice: elian say that do status report the queue mode
  meta: kind=partial | timestamp=1777911563.2635095 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:23] operator / voice_transcript_final / voice: status report
  meta: kind=final | timestamp=1777911563.7543793 | source=final | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:23] operator / voice_command / voice: status report
  meta: normalized=True
- [2026-05-05 00:19:24] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777911564.50556 | source=vosk | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:24] operator / voice_transcript_final / voice: sentry
  meta: kind=final | timestamp=1777911564.7514074 | source=final | frequency_hz=337.6 | rms=295 | updated_at=1777911559.799951
- [2026-05-05 00:19:24] operator / voice_command / voice: sentry
  meta: normalized=True
- [2026-05-05 00:19:26] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Analysis complete. Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=off; pir=on. Also. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 00:19:26] operator / voice_transcript_partial / voice: the current
  meta: kind=partial | timestamp=1777911566.7516284 | source=vosk | frequency_hz=312.0 | rms=298 | updated_at=1777911565.7438927
- [2026-05-05 00:19:27] operator / voice_transcript_partial / voice: run diagnostics
  meta: kind=partial | timestamp=1777911567.0000658 | source=vosk | frequency_hz=312.0 | rms=298 | updated_at=1777911565.7438927
- [2026-05-05 00:19:27] operator / voice_transcript_partial / voice: the theme to the
  meta: kind=partial | timestamp=1777911567.2521985 | source=vosk | frequency_hz=224.0 | rms=281 | updated_at=1777911567.2441936
- [2026-05-05 00:19:28] operator / voice_transcript_final / voice: the run delay
  meta: kind=final | timestamp=1777911568.2622843 | source=final | frequency_hz=243.8 | rms=287 | updated_at=1777911568.2537675
- [2026-05-05 00:19:28] operator / voice_command / voice: the run delay
  meta: normalized=True
- [2026-05-05 00:19:28] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777911568.750098 | source=vosk | frequency_hz=243.8 | rms=287 | updated_at=1777911568.2537675
- [2026-05-05 00:19:29] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911569.0008788 | source=vosk | frequency_hz=243.8 | rms=287 | updated_at=1777911568.2537675
- [2026-05-05 00:19:32] operator / voice_transcript_partial / voice: last abort current app to do it repeat it
  meta: kind=partial | timestamp=1777911572.499902 | source=vosk | frequency_hz=278.1 | rms=281 | updated_at=1777911570.994543
- [2026-05-05 00:19:32] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911572.7510006 | source=vosk | frequency_hz=278.1 | rms=281 | updated_at=1777911570.994543
- [2026-05-05 00:19:33] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911573.0024748 | source=final | frequency_hz=278.1 | rms=281 | updated_at=1777911570.994543
- [2026-05-05 00:19:33] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:19:33] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777911573.2508209 | source=vosk | frequency_hz=278.1 | rms=281 | updated_at=1777911570.994543
- [2026-05-05 00:19:33] operator / voice_transcript_partial / voice: to connect
  meta: kind=partial | timestamp=1777911573.5010245 | source=vosk | frequency_hz=278.1 | rms=281 | updated_at=1777911570.994543
- [2026-05-05 00:19:33] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777911573.749811 | source=vosk | frequency_hz=278.1 | rms=281 | updated_at=1777911570.994543
- [2026-05-05 00:19:34] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777911574.0022836 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:34] operator / voice_transcript_partial / voice: delay delay
  meta: kind=partial | timestamp=1777911574.2488308 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:34] operator / voice_transcript_partial / voice: delay delay what
  meta: kind=partial | timestamp=1777911574.4996388 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:34] operator / voice_transcript_partial / voice: delay delay response
  meta: kind=partial | timestamp=1777911574.7509654 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:35] operator / voice_transcript_partial / voice: delay delay rest
  meta: kind=partial | timestamp=1777911575.0000565 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:35] operator / voice_transcript_partial / voice: delay delay rest increase
  meta: kind=partial | timestamp=1777911575.249742 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:35] operator / voice_transcript_partial / voice: delay delay rest queued tasks
  meta: kind=partial | timestamp=1777911575.7495186 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:36] operator / voice_transcript_partial / voice: delay delay rest queued
  meta: kind=partial | timestamp=1777911576.6943734 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:36] operator / voice_transcript_partial / voice: delay delay rest queued increase
  meta: kind=partial | timestamp=1777911576.702574 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:37] operator / voice_transcript_final / voice: delay delay rest queued increase it
  meta: kind=final | timestamp=1777911577.0026996 | source=final | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:37] operator / voice_command / voice: delay delay rest queued increase it
  meta: normalized=True
- [2026-05-05 00:19:37] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777911577.4993985 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:38] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777911578.0016222 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:38] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777911578.24998 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:38] operator / voice_transcript_partial / voice: a lion speed
  meta: kind=partial | timestamp=1777911578.501129 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:39] operator / voice_transcript_partial / voice: a lion speed connect
  meta: kind=partial | timestamp=1777911579.2567465 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:39] operator / voice_transcript_partial / voice: a lion speed connect app
  meta: kind=partial | timestamp=1777911579.7505271 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:40] operator / voice_transcript_final / voice: the speed delay again
  meta: kind=final | timestamp=1777911580.335472 | source=final | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:40] operator / voice_command / voice: the speed delay again
  meta: normalized=True
- [2026-05-05 00:19:41] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:19:41] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:19:42] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777911582.5074637 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:42] operator / voice_transcript_partial / voice: and enable the
  meta: kind=partial | timestamp=1777911582.7748783 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:43] operator / voice_transcript_partial / voice: and enable the app
  meta: kind=partial | timestamp=1777911583.0089247 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:44] operator / voice_transcript_partial / voice: and enable the app aileen
  meta: kind=partial | timestamp=1777911584.251515 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:44] operator / voice_transcript_partial / voice: and enable the app eileen status
  meta: kind=partial | timestamp=1777911584.501254 | source=vosk | frequency_hz=342.0 | rms=293 | updated_at=1777911573.9946492
- [2026-05-05 00:19:45] operator / voice_transcript_final / voice: and enable the app status
  meta: kind=final | timestamp=1777911585.2538245 | source=final | frequency_hz=232.3 | rms=320 | updated_at=1777911585.2448225
- [2026-05-05 00:19:45] operator / voice_command / voice: and enable the app status
  meta: normalized=True
- [2026-05-05 00:19:46] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:19:46] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777911586.750834 | source=vosk | frequency_hz=281.4 | rms=291 | updated_at=1777911585.998633
- [2026-05-05 00:19:49] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777911589.001277 | source=vosk | frequency_hz=343.6 | rms=312 | updated_at=1777911588.2441099
- [2026-05-05 00:19:49] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:19:51] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911591.0001178 | source=vosk | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:51] operator / voice_transcript_partial / voice: do say
  meta: kind=partial | timestamp=1777911591.2513213 | source=vosk | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:51] operator / voice_transcript_final / voice: do sentry
  meta: kind=final | timestamp=1777911591.5011723 | source=final | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:51] operator / voice_command / voice: do sentry
  meta: normalized=True
- [2026-05-05 00:19:51] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777911591.7508774 | source=vosk | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:19:52] operator / voice_transcript_partial / voice: less strict
  meta: kind=partial | timestamp=1777911592.2505078 | source=vosk | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:52] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777911592.5007052 | source=vosk | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:52] operator / voice_transcript_partial / voice: the last sentry
  meta: kind=partial | timestamp=1777911592.7501848 | source=vosk | frequency_hz=308.5 | rms=283 | updated_at=1777911590.248061
- [2026-05-05 00:19:52] operator / voice_transcript_partial / voice: less strict on
  meta: kind=partial | timestamp=1777911592.9998817 | source=vosk | frequency_hz=256.0 | rms=290 | updated_at=1777911592.9939656
- [2026-05-05 00:19:53] operator / voice_transcript_partial / voice: the last sentry
  meta: kind=partial | timestamp=1777911593.7507908 | source=vosk | frequency_hz=299.4 | rms=369 | updated_at=1777911593.2443054
- [2026-05-05 00:19:54] operator / voice_transcript_final / voice: last sentry
  meta: kind=final | timestamp=1777911594.002394 | source=final | frequency_hz=299.4 | rms=369 | updated_at=1777911593.2443054
- [2026-05-05 00:19:54] operator / voice_command / voice: last sentry
  meta: normalized=True
- [2026-05-05 00:19:55] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777911595.0040011 | source=vosk | frequency_hz=304.9 | rms=289 | updated_at=1777911594.9959912
- [2026-05-05 00:19:55] operator / voice_transcript_final / voice: a
  meta: kind=final | timestamp=1777911595.7526205 | source=final | frequency_hz=299.0 | rms=289 | updated_at=1777911595.7446094
- [2026-05-05 00:19:55] operator / voice_command / voice: a
  meta: normalized=True
- [2026-05-05 00:19:56] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777911596.5092235 | source=vosk | frequency_hz=284.6 | rms=290 | updated_at=1777911595.9949615
- [2026-05-05 00:19:57] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777911597.012456 | source=vosk | frequency_hz=284.6 | rms=290 | updated_at=1777911595.9949615
- [2026-05-05 00:19:57] operator / voice_transcript_partial / voice: boards and
  meta: kind=partial | timestamp=1777911597.2569108 | source=vosk | frequency_hz=320.8 | rms=289 | updated_at=1777911597.246158
- [2026-05-05 00:19:57] operator / voice_transcript_partial / voice: boards and last
  meta: kind=partial | timestamp=1777911597.501178 | source=vosk | frequency_hz=320.8 | rms=289 | updated_at=1777911597.246158
- [2026-05-05 00:19:58] operator / voice_transcript_final / voice: brightness boards and last
  meta: kind=final | timestamp=1777911598.5004222 | source=final | frequency_hz=320.8 | rms=289 | updated_at=1777911597.246158
- [2026-05-05 00:19:58] operator / voice_command / voice: brightness boards and last
  meta: normalized=True
- [2026-05-05 00:19:58] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777911598.5059333 | source=vosk | frequency_hz=320.8 | rms=289 | updated_at=1777911597.246158
- [2026-05-05 00:19:59] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911599.7710435 | source=vosk | frequency_hz=317.1 | rms=879 | updated_at=1777911599.2513585
- [2026-05-05 00:20:00] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777911600.5062723 | source=vosk | frequency_hz=317.1 | rms=879 | updated_at=1777911599.2513585
- [2026-05-05 00:20:00] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777911600.7594504 | source=vosk | frequency_hz=324.0 | rms=299 | updated_at=1777911600.7510786
- [2026-05-05 00:20:01] operator / voice_transcript_final / voice: change
  meta: kind=final | timestamp=1777911601.5084674 | source=final | frequency_hz=305.8 | rms=298 | updated_at=1777911601.5009413
- [2026-05-05 00:20:01] operator / voice_command / voice: change
  meta: normalized=True
- [2026-05-05 00:20:03] operator / voice_transcript_partial / voice: run diagnostics
  meta: kind=partial | timestamp=1777911603.0190818 | source=vosk | frequency_hz=305.8 | rms=298 | updated_at=1777911601.5009413
- [2026-05-05 00:20:03] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911603.756234 | source=vosk | frequency_hz=305.8 | rms=298 | updated_at=1777911601.5009413
- [2026-05-05 00:20:04] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777911604.0072563 | source=vosk | frequency_hz=305.8 | rms=298 | updated_at=1777911601.5009413
- [2026-05-05 00:20:04] operator / voice_transcript_partial / voice: that again serial
  meta: kind=partial | timestamp=1777911604.506112 | source=vosk | frequency_hz=305.8 | rms=298 | updated_at=1777911601.5009413
- [2026-05-05 00:20:04] operator / voice_transcript_partial / voice: that again queue
  meta: kind=partial | timestamp=1777911604.7579381 | source=vosk | frequency_hz=276.0 | rms=299 | updated_at=1777911604.751429
- [2026-05-05 00:20:05] operator / voice_transcript_final / voice: that again queue
  meta: kind=final | timestamp=1777911605.2590265 | source=final | frequency_hz=276.0 | rms=299 | updated_at=1777911604.751429
- [2026-05-05 00:20:05] operator / voice_command / voice: that again queue
  meta: normalized=True
- [2026-05-05 00:20:06] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777911606.258566 | source=vosk | frequency_hz=276.0 | rms=299 | updated_at=1777911604.751429
- [2026-05-05 00:20:06] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777911606.7929976 | source=vosk | frequency_hz=276.0 | rms=299 | updated_at=1777911604.751429
- [2026-05-05 00:20:07] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777911607.2710936 | source=vosk | frequency_hz=276.0 | rms=299 | updated_at=1777911604.751429
- [2026-05-05 00:20:08] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777911608.7568934 | source=final | frequency_hz=408.0 | rms=316 | updated_at=1777911608.251491
- [2026-05-05 00:20:09] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:20:09] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911609.7692924 | source=vosk | frequency_hz=408.0 | rms=316 | updated_at=1777911608.251491
- [2026-05-05 00:20:13] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911613.7608101 | source=final | frequency_hz=277.2 | rms=295 | updated_at=1777911613.7509806
- [2026-05-05 00:20:14] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:20:15] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:20:15] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:20:20] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911620.508649 | source=vosk | frequency_hz=309.7 | rms=306 | updated_at=1777911620.5010612
- [2026-05-05 00:20:20] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777911620.757185 | source=vosk | frequency_hz=309.7 | rms=306 | updated_at=1777911620.5010612
- [2026-05-05 00:20:21] operator / voice_transcript_final / voice: smart
  meta: kind=final | timestamp=1777911621.507648 | source=final | frequency_hz=348.3 | rms=379 | updated_at=1777911621.2510395
- [2026-05-05 00:20:21] operator / voice_command / voice: smart
  meta: normalized=True
- [2026-05-05 00:20:22] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:20:23] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911623.7571893 | source=vosk | frequency_hz=348.4 | rms=314 | updated_at=1777911623.7516365
- [2026-05-05 00:20:24] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777911624.7666643 | source=vosk | frequency_hz=367.2 | rms=350 | updated_at=1777911624.7515438
- [2026-05-05 00:20:25] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777911625.0973356 | source=vosk | frequency_hz=364.0 | rms=329 | updated_at=1777911625.082807
- [2026-05-05 00:20:25] operator / voice_transcript_partial / voice: all queued tasks
  meta: kind=partial | timestamp=1777911625.2625732 | source=vosk | frequency_hz=294.7 | rms=295 | updated_at=1777911625.2514794
- [2026-05-05 00:20:26] operator / voice_transcript_final / voice: all queued
  meta: kind=final | timestamp=1777911626.009921 | source=final | frequency_hz=318.1 | rms=293 | updated_at=1777911626.0009072
- [2026-05-05 00:20:31] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777911631.5074508 | source=vosk | frequency_hz=292.6 | rms=356 | updated_at=1777911631.2515817
- [2026-05-05 00:20:31] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777911631.7570255 | source=vosk | frequency_hz=292.6 | rms=356 | updated_at=1777911631.2515817
- [2026-05-05 00:20:32] operator / voice_transcript_partial / voice: lion mode
  meta: kind=partial | timestamp=1777911632.0599477 | source=vosk | frequency_hz=292.6 | rms=356 | updated_at=1777911631.2515817
- [2026-05-05 00:20:32] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777911632.2566113 | source=vosk | frequency_hz=292.6 | rms=356 | updated_at=1777911631.2515817
- [2026-05-05 00:20:32] operator / voice_transcript_partial / voice: brightness silence
  meta: kind=partial | timestamp=1777911632.5085096 | source=vosk | frequency_hz=292.6 | rms=356 | updated_at=1777911631.2515817
- [2026-05-05 00:20:32] operator / voice_transcript_final / voice: brightness
  meta: kind=final | timestamp=1777911632.7599368 | source=final | frequency_hz=292.6 | rms=356 | updated_at=1777911631.2515817
- [2026-05-05 00:20:40] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777911640.554927 | source=vosk | frequency_hz=388.0 | rms=266 | updated_at=1777911639.7520218
- [2026-05-05 00:20:42] operator / voice_transcript_final / voice: be
  meta: kind=final | timestamp=1777911642.060086 | source=final | frequency_hz=388.0 | rms=266 | updated_at=1777911639.7520218
- [2026-05-05 00:20:43] operator / voice_transcript_partial / voice: mode
  meta: kind=partial | timestamp=1777911643.3230934 | source=vosk | frequency_hz=388.0 | rms=266 | updated_at=1777911639.7520218
- [2026-05-05 00:20:44] operator / voice_transcript_final / voice: mode
  meta: kind=final | timestamp=1777911644.069208 | source=final | frequency_hz=388.0 | rms=266 | updated_at=1777911639.7520218
- [2026-05-05 00:20:45] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911645.322986 | source=vosk | frequency_hz=312.0 | rms=265 | updated_at=1777911644.3158996
- [2026-05-05 00:20:46] operator / voice_transcript_final / voice: decrease
  meta: kind=final | timestamp=1777911646.3187804 | source=final | frequency_hz=312.0 | rms=265 | updated_at=1777911644.3158996
- [2026-05-05 00:20:47] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777911647.8850121 | source=vosk | frequency_hz=312.0 | rms=265 | updated_at=1777911644.3158996
- [2026-05-05 00:20:48] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777911648.0686674 | source=vosk | frequency_hz=312.0 | rms=265 | updated_at=1777911644.3158996
- [2026-05-05 00:20:48] operator / voice_transcript_final / voice: are you
  meta: kind=final | timestamp=1777911648.569397 | source=final | frequency_hz=395.0 | rms=252 | updated_at=1777911648.5628877
- [2026-05-05 00:20:52] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777911652.56774 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:52] operator / voice_transcript_partial / voice: last clear
  meta: kind=partial | timestamp=1777911652.8176484 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:53] operator / voice_transcript_partial / voice: last clear the
  meta: kind=partial | timestamp=1777911653.0690527 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:53] operator / voice_transcript_partial / voice: last clear boards
  meta: kind=partial | timestamp=1777911653.569113 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:53] operator / voice_transcript_partial / voice: last clear board disconnect
  meta: kind=partial | timestamp=1777911653.8198812 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:54] operator / voice_transcript_partial / voice: last clear brightness clear the
  meta: kind=partial | timestamp=1777911654.0740428 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:54] operator / voice_transcript_partial / voice: last clear brightness clear alion
  meta: kind=partial | timestamp=1777911654.9880228 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:55] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:20:55] operator / voice_transcript_partial / voice: last clear brightness clear alien cancel
  meta: kind=partial | timestamp=1777911655.0742047 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:55] operator / voice_transcript_partial / voice: last clear brightness clear alien queued tasks
  meta: kind=partial | timestamp=1777911655.3346915 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:55] operator / voice_transcript_partial / voice: last clear brightness clear alien queued yourself
  meta: kind=partial | timestamp=1777911655.8173807 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:56] operator / voice_transcript_partial / voice: last clear brightness clear you do you
  meta: kind=partial | timestamp=1777911656.0700078 | source=vosk | frequency_hz=388.0 | rms=264 | updated_at=1777911651.5618584
- [2026-05-05 00:20:56] operator / voice_transcript_final / voice: last clear brightness clear enable you do you
  meta: kind=final | timestamp=1777911656.578802 | source=final | frequency_hz=292.0 | rms=257 | updated_at=1777911656.5621364
- [2026-05-05 00:20:56] operator / voice_command / voice: last clear brightness clear enable you do you
  meta: normalized=True
- [2026-05-05 00:20:58] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777911658.0761309 | source=vosk | frequency_hz=292.0 | rms=257 | updated_at=1777911656.5621364
- [2026-05-05 00:20:58] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1777911658.5743792 | source=vosk | frequency_hz=292.0 | rms=257 | updated_at=1777911656.5621364
- [2026-05-05 00:20:59] operator / voice_transcript_partial / voice: do you mode
  meta: kind=partial | timestamp=1777911659.583402 | source=vosk | frequency_hz=292.0 | rms=257 | updated_at=1777911656.5621364
- [2026-05-05 00:20:59] operator / voice_transcript_partial / voice: do you brightness
  meta: kind=partial | timestamp=1777911659.8201828 | source=vosk | frequency_hz=292.0 | rms=257 | updated_at=1777911656.5621364
- [2026-05-05 00:21:00] operator / voice_transcript_final / voice: do you a brightness
  meta: kind=final | timestamp=1777911660.8196704 | source=final | frequency_hz=275.0 | rms=244 | updated_at=1777911660.5619168
- [2026-05-05 00:21:01] operator / voice_command / voice: do you a brightness
  meta: normalized=True
- [2026-05-05 00:21:02] operator / voice_transcript_partial / voice: home
  meta: kind=partial | timestamp=1777911662.0676625 | source=vosk | frequency_hz=297.8 | rms=261 | updated_at=1777911661.0617342
- [2026-05-05 00:21:02] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777911662.3185399 | source=vosk | frequency_hz=297.8 | rms=261 | updated_at=1777911661.0617342
- [2026-05-05 00:21:03] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777911663.841156 | source=final | frequency_hz=297.8 | rms=261 | updated_at=1777911661.0617342
- [2026-05-05 00:21:04] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-05 00:21:03] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777911663.8641295 | source=vosk | frequency_hz=297.8 | rms=261 | updated_at=1777911661.0617342
- [2026-05-05 00:21:05] operator / voice_transcript_final / voice: delay
  meta: kind=final | timestamp=1777911665.044449 | source=final | frequency_hz=297.8 | rms=261 | updated_at=1777911661.0617342
- [2026-05-05 00:21:05] operator / voice_command / voice: delay
  meta: normalized=True
- [2026-05-05 00:21:07] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777911667.5575738 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:07] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777911667.8084736 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:08] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777911668.317506 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:08] operator / voice_transcript_partial / voice: you do
  meta: kind=partial | timestamp=1777911668.5641322 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:08] operator / voice_transcript_partial / voice: you the
  meta: kind=partial | timestamp=1777911668.801745 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:09] operator / voice_transcript_partial / voice: you the be
  meta: kind=partial | timestamp=1777911669.052658 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:09] operator / voice_transcript_partial / voice: you the be less
  meta: kind=partial | timestamp=1777911669.8039873 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:10] operator / voice_transcript_partial / voice: you the be lion
  meta: kind=partial | timestamp=1777911670.302263 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:10] operator / voice_transcript_final / voice: stop you the be less
  meta: kind=final | timestamp=1777911670.6852894 | source=final | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:10] operator / voice_command / voice: stop you the be less
  meta: normalized=True
- [2026-05-05 00:21:11] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777911671.5573823 | source=vosk | frequency_hz=257.9 | rms=819 | updated_at=1777911665.7995453
- [2026-05-05 00:21:24] operator / voice_transcript_partial / voice: are
  meta: kind=partial | timestamp=1777911684.3023603 | source=vosk | frequency_hz=373.4 | rms=239 | updated_at=1777911683.2969437
- [2026-05-05 00:21:24] operator / voice_transcript_partial / voice: are decrease
  meta: kind=partial | timestamp=1777911684.554664 | source=vosk | frequency_hz=363.1 | rms=252 | updated_at=1777911684.5466604
- [2026-05-05 00:21:25] operator / voice_transcript_final / voice: are again
  meta: kind=final | timestamp=1777911685.521277 | source=final | frequency_hz=363.1 | rms=252 | updated_at=1777911684.5466604
- [2026-05-05 00:21:25] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777911685.5343885 | source=vosk | frequency_hz=363.1 | rms=252 | updated_at=1777911684.5466604
- [2026-05-05 00:21:26] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1777911686.052752 | source=final | frequency_hz=362.0 | rms=459 | updated_at=1777911685.7714765
- [2026-05-05 00:21:50] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911710.5551598 | source=vosk | frequency_hz=420.0 | rms=475 | updated_at=1777911709.367087
- [2026-05-05 00:21:51] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777911711.0372283 | source=final | frequency_hz=420.0 | rms=475 | updated_at=1777911709.367087
- [2026-05-05 00:21:52] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777911712.534689 | source=vosk | frequency_hz=412.0 | rms=271 | updated_at=1777911712.528178
- [2026-05-05 00:21:52] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911712.7846313 | source=vosk | frequency_hz=412.0 | rms=271 | updated_at=1777911712.528178
- [2026-05-05 00:21:53] operator / voice_transcript_partial / voice: change theme
  meta: kind=partial | timestamp=1777911713.0381186 | source=vosk | frequency_hz=412.0 | rms=271 | updated_at=1777911712.528178
- [2026-05-05 00:21:53] operator / voice_transcript_partial / voice: change theme to
  meta: kind=partial | timestamp=1777911713.536098 | source=vosk | frequency_hz=412.0 | rms=271 | updated_at=1777911712.528178
- [2026-05-05 00:21:53] operator / voice_transcript_partial / voice: change theme
  meta: kind=partial | timestamp=1777911713.7832062 | source=vosk | frequency_hz=412.0 | rms=271 | updated_at=1777911712.528178
- [2026-05-05 00:21:54] operator / voice_transcript_final / voice: do theme
  meta: kind=final | timestamp=1777911714.25329 | source=final | frequency_hz=404.0 | rms=267 | updated_at=1777911714.2181966
- [2026-05-05 00:21:56] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777911716.7846668 | source=vosk | frequency_hz=350.0 | rms=359 | updated_at=1777911715.7784836
- [2026-05-05 00:21:57] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777911717.0328634 | source=vosk | frequency_hz=350.0 | rms=359 | updated_at=1777911715.7784836
- [2026-05-05 00:21:57] operator / voice_transcript_final / voice: say
  meta: kind=final | timestamp=1777911717.2864842 | source=final | frequency_hz=350.0 | rms=359 | updated_at=1777911715.7784836
- [2026-05-05 00:21:59] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911719.5352511 | source=vosk | frequency_hz=410.0 | rms=283 | updated_at=1777911717.7832258
- [2026-05-05 00:22:00] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777911720.542205 | source=vosk | frequency_hz=410.0 | rms=283 | updated_at=1777911717.7832258
- [2026-05-05 00:22:00] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911720.8052003 | source=vosk | frequency_hz=410.0 | rms=283 | updated_at=1777911717.7832258
- [2026-05-05 00:22:01] operator / voice_transcript_final / voice: yourself
  meta: kind=final | timestamp=1777911721.043568 | source=final | frequency_hz=410.0 | rms=283 | updated_at=1777911717.7832258
- [2026-05-05 00:22:02] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911722.534848 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:02] operator / voice_transcript_partial / voice: you serial
  meta: kind=partial | timestamp=1777911722.795698 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:03] operator / voice_transcript_partial / voice: you say
  meta: kind=partial | timestamp=1777911723.03353 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:03] operator / voice_transcript_partial / voice: you say more
  meta: kind=partial | timestamp=1777911723.2842233 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:03] operator / voice_transcript_partial / voice: you say mode
  meta: kind=partial | timestamp=1777911723.5353754 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:03] operator / voice_transcript_partial / voice: you say more
  meta: kind=partial | timestamp=1777911723.8076358 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:04] operator / voice_transcript_partial / voice: you say mode do
  meta: kind=partial | timestamp=1777911724.0357044 | source=vosk | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:04] operator / voice_transcript_final / voice: you say mode
  meta: kind=final | timestamp=1777911724.2873964 | source=final | frequency_hz=388.4 | rms=244 | updated_at=1777911722.028328
- [2026-05-05 00:22:52] operator / voice_transcript_partial / voice: queued
  meta: kind=partial | timestamp=1777911772.0356777 | source=vosk | frequency_hz=364.0 | rms=240 | updated_at=1777911771.2785408
- [2026-05-05 00:22:52] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777911772.5364618 | source=vosk | frequency_hz=364.0 | rms=240 | updated_at=1777911771.2785408
- [2026-05-05 00:22:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:22:52] operator / voice_transcript_partial / voice: e decrease
  meta: kind=partial | timestamp=1777911772.8138192 | source=vosk | frequency_hz=364.0 | rms=240 | updated_at=1777911771.2785408
- [2026-05-05 00:22:53] operator / voice_transcript_partial / voice: e theme
  meta: kind=partial | timestamp=1777911773.0358396 | source=vosk | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:53] operator / voice_transcript_final / voice: e theme
  meta: kind=final | timestamp=1777911773.59742 | source=final | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:54] operator / voice_command / voice: e theme
  meta: normalized=True
- [2026-05-05 00:22:54] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911774.2850184 | source=vosk | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:54] operator / voice_transcript_partial / voice: the connect
  meta: kind=partial | timestamp=1777911774.8437517 | source=vosk | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:55] operator / voice_transcript_partial / voice: the connect do
  meta: kind=partial | timestamp=1777911775.2896442 | source=vosk | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:56] operator / voice_transcript_partial / voice: the connect do no
  meta: kind=partial | timestamp=1777911776.03942 | source=vosk | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:56] operator / voice_transcript_partial / voice: the connect do no board
  meta: kind=partial | timestamp=1777911776.3045833 | source=vosk | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:56] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777911776.788602 | source=final | frequency_hz=320.0 | rms=275 | updated_at=1777911773.0293314
- [2026-05-05 00:22:57] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 00:22:58] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:23:06] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777911786.796014 | source=vosk | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:07] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777911787.2877567 | source=final | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:07] operator / voice_command / voice: that
  meta: normalized=True
- [2026-05-05 00:23:07] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777911787.5374296 | source=vosk | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:07] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777911787.8798127 | source=vosk | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:08] operator / voice_transcript_partial / voice: you guarding
  meta: kind=partial | timestamp=1777911788.047856 | source=vosk | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:08] operator / voice_transcript_partial / voice: you task
  meta: kind=partial | timestamp=1777911788.2860792 | source=vosk | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:08] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777911788.5359795 | source=vosk | frequency_hz=377.7 | rms=319 | updated_at=1777911786.5443225
- [2026-05-05 00:23:09] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911789.0779123 | source=vosk | frequency_hz=400.4 | rms=263 | updated_at=1777911789.0709069
- [2026-05-05 00:23:11] operator / voice_transcript_partial / voice: [unk] response
  meta: kind=partial | timestamp=1777911791.7863698 | source=vosk | frequency_hz=314.0 | rms=272 | updated_at=1777911790.791908
- [2026-05-05 00:23:12] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911792.036549 | source=vosk | frequency_hz=314.0 | rms=272 | updated_at=1777911790.791908
- [2026-05-05 00:23:12] operator / voice_transcript_partial / voice: [unk] say
  meta: kind=partial | timestamp=1777911792.2932408 | source=vosk | frequency_hz=314.0 | rms=272 | updated_at=1777911790.791908
- [2026-05-05 00:23:13] operator / voice_transcript_final / voice: you stop say
  meta: kind=final | timestamp=1777911793.1522193 | source=final | frequency_hz=314.0 | rms=272 | updated_at=1777911790.791908
- [2026-05-05 00:23:16] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777911796.785841 | source=vosk | frequency_hz=344.2 | rms=254 | updated_at=1777911796.2812183
- [2026-05-05 00:23:17] operator / voice_transcript_partial / voice: you do
  meta: kind=partial | timestamp=1777911797.5363123 | source=vosk | frequency_hz=344.2 | rms=254 | updated_at=1777911796.2812183
- [2026-05-05 00:23:18] operator / voice_transcript_final / voice: you do
  meta: kind=final | timestamp=1777911798.038246 | source=final | frequency_hz=276.0 | rms=257 | updated_at=1777911797.7802465
- [2026-05-05 00:23:18] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777911798.284938 | source=vosk | frequency_hz=276.0 | rms=257 | updated_at=1777911797.7802465
- [2026-05-05 00:23:20] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777911800.0410466 | source=vosk | frequency_hz=327.6 | rms=250 | updated_at=1777911799.2798283
- [2026-05-05 00:23:20] operator / voice_transcript_partial / voice: on lion
  meta: kind=partial | timestamp=1777911800.2855897 | source=vosk | frequency_hz=327.6 | rms=250 | updated_at=1777911799.2798283
- [2026-05-05 00:23:20] operator / voice_transcript_partial / voice: on lion be
  meta: kind=partial | timestamp=1777911800.5445688 | source=vosk | frequency_hz=327.6 | rms=250 | updated_at=1777911799.2798283
- [2026-05-05 00:23:21] operator / voice_transcript_partial / voice: on lion be be
  meta: kind=partial | timestamp=1777911801.5400755 | source=vosk | frequency_hz=327.6 | rms=250 | updated_at=1777911799.2798283
- [2026-05-05 00:23:22] operator / voice_transcript_partial / voice: on lion be be do
  meta: kind=partial | timestamp=1777911802.535892 | source=vosk | frequency_hz=352.0 | rms=261 | updated_at=1777911802.5303802
- [2026-05-05 00:23:23] operator / voice_transcript_final / voice: on lion be be do
  meta: kind=final | timestamp=1777911803.2867384 | source=final | frequency_hz=312.8 | rms=261 | updated_at=1777911803.2802289
- [2026-05-05 00:23:23] operator / voice_command / voice: on lion be be do
  meta: normalized=True
- [2026-05-05 00:23:25] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:23:27] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911807.029127 | source=vosk | frequency_hz=328.5 | rms=290 | updated_at=1777911805.2812169
- [2026-05-05 00:23:27] operator / voice_transcript_partial / voice: speed identify
  meta: kind=partial | timestamp=1777911807.536173 | source=vosk | frequency_hz=328.5 | rms=290 | updated_at=1777911805.2812169
- [2026-05-05 00:23:27] operator / voice_transcript_partial / voice: speed no do
  meta: kind=partial | timestamp=1777911807.7859044 | source=vosk | frequency_hz=328.5 | rms=290 | updated_at=1777911805.2812169
- [2026-05-05 00:23:28] operator / voice_transcript_final / voice: speed no
  meta: kind=final | timestamp=1777911808.038113 | source=final | frequency_hz=328.5 | rms=290 | updated_at=1777911805.2812169
- [2026-05-05 00:23:28] operator / voice_command / voice: speed no
  meta: normalized=True
- [2026-05-05 00:23:28] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911808.5393689 | source=vosk | frequency_hz=328.5 | rms=290 | updated_at=1777911805.2812169
- [2026-05-05 00:23:29] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777911809.0380642 | source=final | frequency_hz=328.5 | rms=290 | updated_at=1777911805.2812169
- [2026-05-05 00:23:29] operator / voice_command / voice: do
  meta: normalized=True
- [2026-05-05 00:23:31] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:23:31] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:23:33] operator / voice_transcript_partial / voice: talk
  meta: kind=partial | timestamp=1777911813.2015653 | source=vosk | frequency_hz=308.0 | rms=251 | updated_at=1777911812.2605505
- [2026-05-05 00:23:33] operator / voice_transcript_partial / voice: talk less
  meta: kind=partial | timestamp=1777911813.2753582 | source=vosk | frequency_hz=308.0 | rms=251 | updated_at=1777911812.2605505
- [2026-05-05 00:23:33] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777911813.7674708 | source=vosk | frequency_hz=308.0 | rms=251 | updated_at=1777911812.2605505
- [2026-05-05 00:23:34] operator / voice_transcript_final / voice: talk
  meta: kind=final | timestamp=1777911814.0611594 | source=final | frequency_hz=360.0 | rms=282 | updated_at=1777911814.0121996
- [2026-05-05 00:23:37] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777911817.0182376 | source=vosk | frequency_hz=297.2 | rms=261 | updated_at=1777911816.5100079
- [2026-05-05 00:23:37] operator / voice_transcript_partial / voice: queue
  meta: kind=partial | timestamp=1777911817.5169232 | source=vosk | frequency_hz=297.2 | rms=261 | updated_at=1777911816.5100079
- [2026-05-05 00:23:38] operator / voice_transcript_final / voice: queue
  meta: kind=final | timestamp=1777911818.0227413 | source=final | frequency_hz=343.2 | rms=281 | updated_at=1777911818.014732
- [2026-05-05 00:23:38] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777911818.266876 | source=vosk | frequency_hz=343.2 | rms=281 | updated_at=1777911818.014732
- [2026-05-05 00:23:38] operator / voice_transcript_partial / voice: board decrease
  meta: kind=partial | timestamp=1777911818.5154908 | source=vosk | frequency_hz=312.7 | rms=273 | updated_at=1777911818.5099792
- [2026-05-05 00:23:38] operator / voice_transcript_partial / voice: board theme
  meta: kind=partial | timestamp=1777911818.7655947 | source=vosk | frequency_hz=313.9 | rms=248 | updated_at=1777911818.7600868
- [2026-05-05 00:23:39] operator / voice_transcript_final / voice: board theme
  meta: kind=final | timestamp=1777911819.267568 | source=final | frequency_hz=302.6 | rms=276 | updated_at=1777911819.2605493
- [2026-05-05 00:23:41] operator / voice_transcript_partial / voice: to the
  meta: kind=partial | timestamp=1777911821.6786566 | source=vosk | frequency_hz=316.4 | rms=303 | updated_at=1777911821.0182827
- [2026-05-05 00:23:41] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777911821.7804189 | source=vosk | frequency_hz=316.4 | rms=303 | updated_at=1777911821.0182827
- [2026-05-05 00:23:42] operator / voice_transcript_partial / voice: do it again
  meta: kind=partial | timestamp=1777911822.0159721 | source=vosk | frequency_hz=316.4 | rms=303 | updated_at=1777911821.0182827
- [2026-05-05 00:23:42] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1777911822.2686164 | source=final | frequency_hz=316.4 | rms=303 | updated_at=1777911821.0182827
- [2026-05-05 00:23:42] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-05 00:23:43] operator / voice_command / voice: status report
  meta: normalized=True
- [2026-05-05 00:23:43] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911823.9828694 | source=vosk | frequency_hz=320.0 | rms=284 | updated_at=1777911823.971366
- [2026-05-05 00:23:44] operator / voice_transcript_final / voice: yourself
  meta: kind=final | timestamp=1777911824.6536293 | source=final | frequency_hz=288.0 | rms=272 | updated_at=1777911824.513385
- [2026-05-05 00:23:45] operator / voice_command / voice: yourself
  meta: normalized=True
- [2026-05-05 00:23:46] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:23:46] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Smart Sentry is paused right now. Latest AI note. Analysis complete. Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=False
- [2026-05-05 00:23:47] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777911827.266205 | source=vosk | frequency_hz=284.6 | rms=266 | updated_at=1777911826.2752132
- [2026-05-05 00:23:47] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911827.5985484 | source=vosk | frequency_hz=284.6 | rms=266 | updated_at=1777911826.2752132
- [2026-05-05 00:23:49] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911829.5205626 | source=final | frequency_hz=344.7 | rms=276 | updated_at=1777911828.7606692
- [2026-05-05 00:23:50] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:23:51] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:23:52] operator / voice_transcript_partial / voice: mind
  meta: kind=partial | timestamp=1777911832.7661853 | source=vosk | frequency_hz=368.4 | rms=290 | updated_at=1777911832.51164
- [2026-05-05 00:23:53] operator / voice_transcript_partial / voice: commands
  meta: kind=partial | timestamp=1777911833.017411 | source=vosk | frequency_hz=368.4 | rms=290 | updated_at=1777911832.51164
- [2026-05-05 00:23:53] operator / voice_transcript_final / voice: commands
  meta: kind=final | timestamp=1777911833.6472023 | source=final | frequency_hz=368.4 | rms=290 | updated_at=1777911832.51164
- [2026-05-05 00:23:54] operator / voice_command / voice: commands
  meta: normalized=True
- [2026-05-05 00:23:55] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:23:55] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777911835.517424 | source=vosk | frequency_hz=385.4 | rms=271 | updated_at=1777911835.0101285
- [2026-05-05 00:23:55] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777911835.7665012 | source=vosk | frequency_hz=385.4 | rms=271 | updated_at=1777911835.0101285
- [2026-05-05 00:23:56] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911836.0189648 | source=vosk | frequency_hz=385.4 | rms=271 | updated_at=1777911835.0101285
- [2026-05-05 00:23:56] operator / voice_transcript_final / voice: speed
  meta: kind=final | timestamp=1777911836.577097 | source=final | frequency_hz=385.4 | rms=271 | updated_at=1777911835.0101285
- [2026-05-05 00:23:59] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911839.0168066 | source=vosk | frequency_hz=270.2 | rms=254 | updated_at=1777911838.3799806
- [2026-05-05 00:23:59] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777911839.2792156 | source=vosk | frequency_hz=270.2 | rms=254 | updated_at=1777911838.3799806
- [2026-05-05 00:24:07] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777911847.4330192 | source=vosk | frequency_hz=321.4 | rms=266 | updated_at=1777911846.9267766
- [2026-05-05 00:24:08] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777911848.184022 | source=final | frequency_hz=365.7 | rms=261 | updated_at=1777911847.9263434
- [2026-05-05 00:24:10] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777911850.3451953 | source=vosk | frequency_hz=368.9 | rms=923 | updated_at=1777911848.9261584
- [2026-05-05 00:24:16] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777911856.9374883 | source=vosk | frequency_hz=330.1 | rms=266 | updated_at=1777911856.4637537
- [2026-05-05 00:24:17] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777911857.194977 | source=vosk | frequency_hz=325.2 | rms=264 | updated_at=1777911857.1829562
- [2026-05-05 00:24:17] operator / voice_transcript_partial / voice: queued tasks
  meta: kind=partial | timestamp=1777911857.9503658 | source=vosk | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:18] operator / voice_transcript_partial / voice: change theme
  meta: kind=partial | timestamp=1777911858.1833234 | source=vosk | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:18] operator / voice_transcript_partial / voice: change theme resume
  meta: kind=partial | timestamp=1777911858.4340553 | source=vosk | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:18] operator / voice_transcript_partial / voice: change theme resume brightness
  meta: kind=partial | timestamp=1777911858.9317312 | source=vosk | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:19] operator / voice_transcript_partial / voice: change theme resume
  meta: kind=partial | timestamp=1777911859.1821225 | source=vosk | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:19] operator / voice_transcript_partial / voice: change theme resume brightness
  meta: kind=partial | timestamp=1777911859.4537365 | source=vosk | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:20] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1777911860.065006 | source=final | frequency_hz=325.2 | rms=254 | updated_at=1777911857.6765492
- [2026-05-05 00:24:22] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777911862.5374463 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:22] operator / voice_transcript_partial / voice: behavior guarding
  meta: kind=partial | timestamp=1777911862.6846182 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:22] operator / voice_transcript_partial / voice: be a speed
  meta: kind=partial | timestamp=1777911862.93641 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:23] operator / voice_transcript_partial / voice: behavior a lion
  meta: kind=partial | timestamp=1777911863.1835454 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:23] operator / voice_transcript_partial / voice: behavior a
  meta: kind=partial | timestamp=1777911863.6959147 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:23] operator / voice_transcript_partial / voice: behavior a the smart
  meta: kind=partial | timestamp=1777911863.9324179 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:24] operator / voice_transcript_partial / voice: behavior a the smart sentry
  meta: kind=partial | timestamp=1777911864.4342535 | source=vosk | frequency_hz=324.6 | rms=268 | updated_at=1777911861.4270334
- [2026-05-05 00:24:32] operator / voice_transcript_partial / voice: stop
  meta: kind=partial | timestamp=1777911872.0663009 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:32] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777911872.8155942 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:33] operator / voice_transcript_partial / voice: status report
  meta: kind=partial | timestamp=1777911873.2694335 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:33] operator / voice_transcript_final / voice: stop status
  meta: kind=final | timestamp=1777911873.92128 | source=final | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:34] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777911874.9274294 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:35] operator / voice_transcript_partial / voice: be strict
  meta: kind=partial | timestamp=1777911875.1796713 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:35] operator / voice_transcript_partial / voice: be decrease response
  meta: kind=partial | timestamp=1777911875.7617211 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:36] operator / voice_transcript_partial / voice: be strict be smart sentry
  meta: kind=partial | timestamp=1777911876.3068132 | source=vosk | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:36] operator / voice_transcript_final / voice: be strict be smart
  meta: kind=final | timestamp=1777911876.8204513 | source=final | frequency_hz=204.2 | rms=260 | updated_at=1777911868.0603971
- [2026-05-05 00:24:40] operator / voice_transcript_partial / voice: priority
  meta: kind=partial | timestamp=1777911880.9408607 | source=vosk | frequency_hz=291.2 | rms=270 | updated_at=1777911880.4899101
- [2026-05-05 00:24:41] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777911881.4278255 | source=vosk | frequency_hz=291.2 | rms=270 | updated_at=1777911880.4899101
- [2026-05-05 00:24:41] operator / voice_transcript_partial / voice: app a lion
  meta: kind=partial | timestamp=1777911881.939799 | source=vosk | frequency_hz=268.0 | rms=272 | updated_at=1777911881.930797
- [2026-05-05 00:24:42] operator / voice_transcript_final / voice: current app a
  meta: kind=final | timestamp=1777911882.6793206 | source=final | frequency_hz=255.4 | rms=267 | updated_at=1777911882.4227428
- [2026-05-05 00:24:43] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777911883.1805415 | source=vosk | frequency_hz=255.4 | rms=267 | updated_at=1777911882.4227428
- [2026-05-05 00:24:43] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911883.4284983 | source=vosk | frequency_hz=255.4 | rms=267 | updated_at=1777911882.4227428
- [2026-05-05 00:24:44] operator / voice_transcript_final / voice: speed
  meta: kind=final | timestamp=1777911884.80084 | source=final | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:46] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777911886.5587096 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:46] operator / voice_transcript_partial / voice: say go
  meta: kind=partial | timestamp=1777911886.8303902 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:47] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777911887.0584996 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:47] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:24:47] operator / voice_transcript_partial / voice: say alien
  meta: kind=partial | timestamp=1777911887.3210275 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:47] operator / voice_transcript_partial / voice: say alien enable
  meta: kind=partial | timestamp=1777911887.5615766 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:48] operator / voice_transcript_partial / voice: say alien yes e lion
  meta: kind=partial | timestamp=1777911888.04789 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:48] operator / voice_transcript_partial / voice: say alien yes elliot
  meta: kind=partial | timestamp=1777911888.4094121 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:48] operator / voice_transcript_partial / voice: say alien yes eileen
  meta: kind=partial | timestamp=1777911888.659828 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:48] operator / voice_transcript_partial / voice: say alien yes aileen go
  meta: kind=partial | timestamp=1777911888.962704 | source=vosk | frequency_hz=388.0 | rms=280 | updated_at=1777911884.1259558
- [2026-05-05 00:24:53] operator / voice_transcript_partial / voice: task
  meta: kind=partial | timestamp=1777911893.3555236 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:53] operator / voice_transcript_partial / voice: task to
  meta: kind=partial | timestamp=1777911893.7431488 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:53] operator / voice_transcript_partial / voice: task to brightness
  meta: kind=partial | timestamp=1777911893.860561 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:54] operator / voice_transcript_partial / voice: task to brightness increase
  meta: kind=partial | timestamp=1777911894.118017 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:54] operator / voice_transcript_partial / voice: task to brightness increase speed
  meta: kind=partial | timestamp=1777911894.6081548 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:54] operator / voice_transcript_partial / voice: task to brightness increase theme
  meta: kind=partial | timestamp=1777911894.8547156 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:55] operator / voice_transcript_partial / voice: task to brightness increase theme alien
  meta: kind=partial | timestamp=1777911895.1363022 | source=vosk | frequency_hz=345.4 | rms=264 | updated_at=1777911891.5998602
- [2026-05-05 00:24:55] operator / voice_transcript_final / voice: task to brightness increase speed
  meta: kind=final | timestamp=1777911895.3577774 | source=final | frequency_hz=328.0 | rms=268 | updated_at=1777911895.3497615
- [2026-05-05 00:24:56] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777911896.973277 | source=vosk | frequency_hz=335.0 | rms=259 | updated_at=1777911895.6098125
- [2026-05-05 00:24:57] operator / voice_transcript_partial / voice: again again
  meta: kind=partial | timestamp=1777911897.6058147 | source=vosk | frequency_hz=335.0 | rms=259 | updated_at=1777911895.6098125
- [2026-05-05 00:24:58] operator / voice_transcript_final / voice: again again
  meta: kind=final | timestamp=1777911898.6077962 | source=final | frequency_hz=270.2 | rms=259 | updated_at=1777911898.600288
- [2026-05-05 00:25:00] operator / voice_transcript_partial / voice: are you do
  meta: kind=partial | timestamp=1777911900.566211 | source=vosk | frequency_hz=213.7 | rms=357 | updated_at=1777911899.8425431
- [2026-05-05 00:25:01] operator / voice_transcript_final / voice: are you do
  meta: kind=final | timestamp=1777911901.8891687 | source=final | frequency_hz=285.0 | rms=254 | updated_at=1777911901.5609236
- [2026-05-05 00:25:04] operator / voice_transcript_partial / voice: home
  meta: kind=partial | timestamp=1777911904.7057302 | source=vosk | frequency_hz=241.8 | rms=259 | updated_at=1777911903.8893564
- [2026-05-05 00:25:04] operator / voice_transcript_partial / voice: identify
  meta: kind=partial | timestamp=1777911904.8968372 | source=vosk | frequency_hz=241.8 | rms=259 | updated_at=1777911903.8893564
- [2026-05-05 00:25:05] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911905.1611202 | source=vosk | frequency_hz=241.8 | rms=259 | updated_at=1777911903.8893564
- [2026-05-05 00:25:05] operator / voice_transcript_partial / voice: who are you do
  meta: kind=partial | timestamp=1777911905.3951125 | source=vosk | frequency_hz=241.8 | rms=259 | updated_at=1777911903.8893564
- [2026-05-05 00:25:05] operator / voice_transcript_final / voice: who are you do
  meta: kind=final | timestamp=1777911905.8968906 | source=final | frequency_hz=241.8 | rms=259 | updated_at=1777911903.8893564
- [2026-05-05 00:25:08] operator / voice_transcript_partial / voice: app to
  meta: kind=partial | timestamp=1777911908.6969554 | source=vosk | frequency_hz=348.0 | rms=268 | updated_at=1777911906.138198
- [2026-05-05 00:25:08] operator / voice_transcript_partial / voice: app to the
  meta: kind=partial | timestamp=1777911908.9488857 | source=vosk | frequency_hz=348.0 | rms=268 | updated_at=1777911906.138198
- [2026-05-05 00:25:09] operator / voice_transcript_partial / voice: app to the boards
  meta: kind=partial | timestamp=1777911909.209512 | source=vosk | frequency_hz=348.0 | rms=268 | updated_at=1777911906.138198
- [2026-05-05 00:25:09] operator / voice_transcript_partial / voice: app to the board to com
  meta: kind=partial | timestamp=1777911909.449261 | source=vosk | frequency_hz=348.0 | rms=268 | updated_at=1777911906.138198
- [2026-05-05 00:25:09] operator / voice_transcript_partial / voice: app to the board to go rest
  meta: kind=partial | timestamp=1777911909.7002542 | source=vosk | frequency_hz=348.0 | rms=268 | updated_at=1777911906.138198
- [2026-05-05 00:25:09] operator / voice_transcript_partial / voice: app to the board talk less strict
  meta: kind=partial | timestamp=1777911909.9512308 | source=vosk | frequency_hz=296.0 | rms=244 | updated_at=1777911909.9462314
- [2026-05-05 00:25:10] operator / voice_transcript_partial / voice: app to the board to go rest do
  meta: kind=partial | timestamp=1777911910.1983862 | source=vosk | frequency_hz=296.0 | rms=244 | updated_at=1777911909.9462314
- [2026-05-05 00:25:10] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777911910.709788 | source=final | frequency_hz=297.4 | rms=271 | updated_at=1777911910.7011652
- [2026-05-05 00:25:15] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911915.4540749 | source=vosk | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:15] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777911915.70161 | source=final | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:15] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777911915.9669888 | source=vosk | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:16] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:25:16] operator / voice_transcript_partial / voice: who are
  meta: kind=partial | timestamp=1777911916.1984775 | source=vosk | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:16] operator / voice_transcript_partial / voice: who are you
  meta: kind=partial | timestamp=1777911916.4611328 | source=vosk | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:16] operator / voice_transcript_partial / voice: who are you do
  meta: kind=partial | timestamp=1777911916.6985133 | source=vosk | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:17] operator / voice_transcript_final / voice: who are you do
  meta: kind=final | timestamp=1777911917.4497004 | source=final | frequency_hz=348.9 | rms=239 | updated_at=1777911914.2080872
- [2026-05-05 00:25:18] operator / voice_command / voice: who are you do
  meta: normalized=True
- [2026-05-05 00:25:19] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False I am Elion Mesk. I monitor the live Smart Sentry runtime, explain what the system is doing, compare live behavior against intended app behavior, diagnose faults, accept supported local control commands, and adjust supported runtime settings while the app is running. I stay grounded in the running app and its supported controls. I do not invent hardware state or pretend unsupported actions already happened.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:25:20] assistant / spoken_confirmation / voice: Received. I started your assistant request about who are you do in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:25:20] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777911920.4726138 | source=vosk | frequency_hz=316.0 | rms=251 | updated_at=1777911919.4485335
- [2026-05-05 00:25:20] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777911920.704634 | source=vosk | frequency_hz=316.0 | rms=251 | updated_at=1777911919.4485335
- [2026-05-05 00:25:20] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777911920.9475946 | source=vosk | frequency_hz=316.0 | rms=251 | updated_at=1777911919.4485335
- [2026-05-05 00:25:21] operator / voice_transcript_partial / voice: standby guarding mode
  meta: kind=partial | timestamp=1777911921.2036161 | source=vosk | frequency_hz=316.0 | rms=251 | updated_at=1777911919.4485335
- [2026-05-05 00:25:21] operator / voice_transcript_partial / voice: standby guarding talk
  meta: kind=partial | timestamp=1777911921.9516063 | source=vosk | frequency_hz=316.0 | rms=251 | updated_at=1777911919.4485335
- [2026-05-05 00:25:22] operator / voice_transcript_partial / voice: standby guarding talk less
  meta: kind=partial | timestamp=1777911922.5286288 | source=vosk | frequency_hz=316.0 | rms=251 | updated_at=1777911919.4485335
- [2026-05-05 00:25:22] operator / voice_transcript_final / voice: standby guarding talk
  meta: kind=final | timestamp=1777911922.966795 | source=final | frequency_hz=309.8 | rms=245 | updated_at=1777911922.944669
- [2026-05-05 00:25:23] operator / voice_command / voice: standby guarding talk
  meta: normalized=True
- [2026-05-05 00:25:24] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777911924.2005298 | source=vosk | frequency_hz=304.1 | rms=242 | updated_at=1777911923.4473648
- [2026-05-05 00:25:24] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777911924.5012496 | source=vosk | frequency_hz=304.1 | rms=242 | updated_at=1777911923.4473648
- [2026-05-05 00:25:24] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777911924.699889 | source=vosk | frequency_hz=304.1 | rms=242 | updated_at=1777911923.4473648
- [2026-05-05 00:25:25] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:25:26] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777911926.2158892 | source=final | frequency_hz=304.8 | rms=232 | updated_at=1777911926.20638
- [2026-05-05 00:25:27] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:25:26] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911926.9488814 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:27] operator / voice_transcript_partial / voice: go rest
  meta: kind=partial | timestamp=1777911927.4495018 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:27] operator / voice_transcript_partial / voice: go rest resume
  meta: kind=partial | timestamp=1777911927.950928 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:28] operator / voice_transcript_partial / voice: go rest resume last
  meta: kind=partial | timestamp=1777911928.220274 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:28] operator / voice_transcript_partial / voice: go rest resume
  meta: kind=partial | timestamp=1777911928.748676 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:28] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777911928.7799203 | source=final | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:30] operator / voice_command / voice: go rest
  meta: normalized=True
- [2026-05-05 00:25:29] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777911929.7137861 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:29] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777911929.962364 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:31] operator / voice_transcript_final / voice: standby go
  meta: kind=final | timestamp=1777911931.0964537 | source=final | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:32] operator / voice_command / voice: standby go
  meta: normalized=True
- [2026-05-05 00:25:31] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777911931.1316836 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:31] operator / voice_transcript_partial / voice: start tracking
  meta: kind=partial | timestamp=1777911931.2166893 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:32] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:25:32] assistant / spoken_confirmation / voice: Resuming Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:25:32] operator / voice_transcript_final / voice: start
  meta: kind=final | timestamp=1777911932.2483368 | source=final | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:33] operator / voice_command / voice: start
  meta: normalized=True
- [2026-05-05 00:25:33] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777911933.49247 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:33] operator / voice_transcript_final / voice: tracking
  meta: kind=final | timestamp=1777911933.9604423 | source=final | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:35] operator / voice_command / voice: tracking
  meta: normalized=True
- [2026-05-05 00:25:34] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777911934.2091157 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:34] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777911934.4483285 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:35] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:25:35] operator / voice_transcript_partial / voice: smart guarding
  meta: kind=partial | timestamp=1777911935.2085717 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:35] operator / voice_transcript_final / voice: smart
  meta: kind=final | timestamp=1777911935.454963 | source=final | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:36] operator / voice_command / voice: smart
  meta: normalized=True
- [2026-05-05 00:25:36] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911936.4480767 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:36] operator / voice_transcript_partial / voice: guarding mode
  meta: kind=partial | timestamp=1777911936.698383 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:37] operator / voice_transcript_partial / voice: go rest
  meta: kind=partial | timestamp=1777911937.1517804 | source=vosk | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:37] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777911937.9483812 | source=final | frequency_hz=307.3 | rms=231 | updated_at=1777911926.2178876
- [2026-05-05 00:25:38] operator / voice_command / voice: go rest
  meta: normalized=True
- [2026-05-05 00:25:40] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:25:41] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:25:41] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:25:41] assistant / spoken_confirmation / voice: I think I heard start. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:25:41] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777911941.9519672 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:42] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777911942.204238 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:42] operator / voice_transcript_partial / voice: standby guarding mode
  meta: kind=partial | timestamp=1777911942.4513464 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:42] operator / voice_transcript_partial / voice: standby guarding no
  meta: kind=partial | timestamp=1777911942.703069 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:42] operator / voice_transcript_partial / voice: standby guarding no app to com
  meta: kind=partial | timestamp=1777911942.9487467 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:43] operator / voice_transcript_partial / voice: standby guarding no app to talk
  meta: kind=partial | timestamp=1777911943.1996355 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:43] operator / voice_transcript_partial / voice: standby guarding no app to com ports
  meta: kind=partial | timestamp=1777911943.44848 | source=vosk | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:43] operator / voice_transcript_final / voice: standby guarding no app to talk
  meta: kind=final | timestamp=1777911943.7021804 | source=final | frequency_hz=374.1 | rms=272 | updated_at=1777911940.6973977
- [2026-05-05 00:25:44] operator / voice_command / voice: standby guarding no app to talk
  meta: normalized=True
- [2026-05-05 00:25:45] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:25:47] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911947.797988 | source=vosk | frequency_hz=321.7 | rms=305 | updated_at=1777911945.5419767
- [2026-05-05 00:25:48] operator / voice_transcript_partial / voice: go in to
  meta: kind=partial | timestamp=1777911948.0899365 | source=vosk | frequency_hz=321.7 | rms=305 | updated_at=1777911945.5419767
- [2026-05-05 00:25:48] operator / voice_transcript_partial / voice: go in to rest
  meta: kind=partial | timestamp=1777911948.3029213 | source=vosk | frequency_hz=321.7 | rms=305 | updated_at=1777911945.5419767
- [2026-05-05 00:25:48] operator / voice_transcript_partial / voice: go in to rest resume last
  meta: kind=partial | timestamp=1777911948.7974386 | source=vosk | frequency_hz=321.7 | rms=305 | updated_at=1777911945.5419767
- [2026-05-05 00:25:49] operator / voice_transcript_partial / voice: go in to rest resume no
  meta: kind=partial | timestamp=1777911949.0523593 | source=vosk | frequency_hz=268.0 | rms=292 | updated_at=1777911949.0439088
- [2026-05-05 00:25:49] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777911949.8183153 | source=final | frequency_hz=241.6 | rms=296 | updated_at=1777911949.7938926
- [2026-05-05 00:25:51] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777911951.5515969 | source=vosk | frequency_hz=320.2 | rms=303 | updated_at=1777911950.7972598
- [2026-05-05 00:25:52] operator / voice_transcript_final / voice: override
  meta: kind=final | timestamp=1777911952.0632684 | source=final | frequency_hz=290.8 | rms=291 | updated_at=1777911952.0539804
- [2026-05-05 00:25:52] operator / voice_command / voice: override
  meta: normalized=True
- [2026-05-05 00:25:53] assistant / spoken_confirmation / voice: Priority acknowledged. Tell me the command.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:25:55] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777911955.5687222 | source=vosk | frequency_hz=280.8 | rms=288 | updated_at=1777911954.04219
- [2026-05-05 00:25:55] operator / voice_transcript_partial / voice: board e again
  meta: kind=partial | timestamp=1777911955.79807 | source=vosk | frequency_hz=280.8 | rms=288 | updated_at=1777911954.04219
- [2026-05-05 00:25:56] operator / voice_transcript_partial / voice: board e no
  meta: kind=partial | timestamp=1777911956.0555549 | source=vosk | frequency_hz=280.8 | rms=288 | updated_at=1777911954.04219
- [2026-05-05 00:25:56] operator / voice_transcript_partial / voice: board e no to
  meta: kind=partial | timestamp=1777911956.5495925 | source=vosk | frequency_hz=280.8 | rms=288 | updated_at=1777911954.04219
- [2026-05-05 00:25:57] operator / voice_transcript_partial / voice: board e no to to the
  meta: kind=partial | timestamp=1777911957.0497835 | source=vosk | frequency_hz=280.8 | rms=288 | updated_at=1777911954.04219
- [2026-05-05 00:25:57] operator / voice_transcript_partial / voice: board e no to to the commands
  meta: kind=partial | timestamp=1777911957.3015468 | source=vosk | frequency_hz=280.8 | rms=288 | updated_at=1777911954.04219
- [2026-05-05 00:25:58] operator / voice_transcript_final / voice: board e a no to to the commands
  meta: kind=final | timestamp=1777911958.3005247 | source=final | frequency_hz=276.0 | rms=314 | updated_at=1777911957.7918515
- [2026-05-05 00:25:58] operator / voice_command / voice: board e a no to to the commands
  meta: normalized=True
- [2026-05-05 00:25:58] operator / voice_transcript_partial / voice: check
  meta: kind=partial | timestamp=1777911958.7995157 | source=vosk | frequency_hz=276.0 | rms=314 | updated_at=1777911957.7918515
- [2026-05-05 00:25:59] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777911959.3899295 | source=vosk | frequency_hz=276.0 | rms=314 | updated_at=1777911957.7918515
- [2026-05-05 00:25:59] operator / voice_transcript_partial / voice: check faster
  meta: kind=partial | timestamp=1777911959.5492764 | source=vosk | frequency_hz=360.0 | rms=312 | updated_at=1777911959.542669
- [2026-05-05 00:26:00] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:00] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911960.0921397 | source=vosk | frequency_hz=360.0 | rms=312 | updated_at=1777911959.542669
- [2026-05-05 00:26:00] operator / voice_transcript_partial / voice: check talk app
  meta: kind=partial | timestamp=1777911960.3031652 | source=vosk | frequency_hz=360.0 | rms=312 | updated_at=1777911959.542669
- [2026-05-05 00:26:00] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777911960.5502162 | source=vosk | frequency_hz=320.1 | rms=302 | updated_at=1777911960.5416937
- [2026-05-05 00:26:02] operator / voice_transcript_partial / voice: check talk app
  meta: kind=partial | timestamp=1777911962.304058 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:02] operator / voice_transcript_partial / voice: check talk app that
  meta: kind=partial | timestamp=1777911962.5476398 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:02] operator / voice_transcript_partial / voice: check talk app that diagnostics
  meta: kind=partial | timestamp=1777911962.798659 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:03] operator / voice_transcript_partial / voice: check talk app that smart mind
  meta: kind=partial | timestamp=1777911963.0487344 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:03] operator / voice_transcript_partial / voice: check talk app that smart sentry
  meta: kind=partial | timestamp=1777911963.297152 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:03] operator / voice_transcript_partial / voice: check talk app that smart you no
  meta: kind=partial | timestamp=1777911963.5564036 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:03] operator / voice_transcript_partial / voice: check talk app that smart you no commands
  meta: kind=partial | timestamp=1777911963.798414 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:04] operator / voice_transcript_partial / voice: check talk app that smart you no commands elliot
  meta: kind=partial | timestamp=1777911964.5476575 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:04] operator / voice_transcript_partial / voice: check talk app that smart you no commands eileen repeat
  meta: kind=partial | timestamp=1777911964.8123326 | source=vosk | frequency_hz=228.6 | rms=311 | updated_at=1777911961.7917306
- [2026-05-05 00:26:06] operator / voice_transcript_final / voice: check the talk app that delay smart you no commands repeat
  meta: kind=final | timestamp=1777911966.4596806 | source=final | frequency_hz=268.0 | rms=306 | updated_at=1777911965.2926388
- [2026-05-05 00:26:06] operator / voice_command / voice: check the talk app that delay smart you no commands repeat
  meta: normalized=True
- [2026-05-05 00:26:06] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777911966.4706938 | source=vosk | frequency_hz=266.6 | rms=298 | updated_at=1777911966.460679
- [2026-05-05 00:26:06] operator / voice_transcript_partial / voice: go the
  meta: kind=partial | timestamp=1777911966.7989042 | source=vosk | frequency_hz=266.6 | rms=298 | updated_at=1777911966.460679
- [2026-05-05 00:26:07] operator / voice_transcript_partial / voice: go the change
  meta: kind=partial | timestamp=1777911967.297338 | source=vosk | frequency_hz=290.9 | rms=377 | updated_at=1777911967.2922401
- [2026-05-05 00:26:08] operator / voice_transcript_final / voice: go the change
  meta: kind=final | timestamp=1777911968.048792 | source=final | frequency_hz=254.9 | rms=303 | updated_at=1777911968.0422733
- [2026-05-05 00:26:08] operator / voice_command / voice: go the change
  meta: normalized=True
- [2026-05-05 00:26:09] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:09] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:26:11] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777911971.046606 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:11] operator / voice_transcript_partial / voice: that diagnostics
  meta: kind=partial | timestamp=1777911971.5497258 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:12] operator / voice_transcript_partial / voice: that do smart sentry
  meta: kind=partial | timestamp=1777911972.0473962 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:12] operator / voice_transcript_partial / voice: that do smart you no commands
  meta: kind=partial | timestamp=1777911972.3026435 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:12] operator / voice_transcript_partial / voice: that do smart you no commands override
  meta: kind=partial | timestamp=1777911972.799871 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:13] operator / voice_transcript_partial / voice: that do smart you no commands talk less
  meta: kind=partial | timestamp=1777911973.261941 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:13] operator / voice_transcript_final / voice: talk less
  meta: kind=final | timestamp=1777911973.333388 | source=final | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:13] operator / voice_command / voice: talk less
  meta: normalized=True
- [2026-05-05 00:26:13] operator / voice_transcript_partial / voice: else
  meta: kind=partial | timestamp=1777911973.8096113 | source=vosk | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:14] operator / voice_transcript_final / voice: else
  meta: kind=final | timestamp=1777911974.4774632 | source=final | frequency_hz=257.6 | rms=296 | updated_at=1777911970.5596554
- [2026-05-05 00:26:15] operator / voice_command / voice: else
  meta: normalized=True
- [2026-05-05 00:26:16] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:16] assistant / spoken_confirmation / voice: Understood. I will keep replies shorter and stop automatic assistant speech unless you ask for it.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:26:19] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777911979.0497382 | source=vosk | frequency_hz=357.4 | rms=320 | updated_at=1777911976.5420046
- [2026-05-05 00:26:19] operator / voice_transcript_partial / voice: that commands
  meta: kind=partial | timestamp=1777911979.5499432 | source=vosk | frequency_hz=357.4 | rms=320 | updated_at=1777911976.5420046
- [2026-05-05 00:26:19] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777911979.9536893 | source=final | frequency_hz=357.4 | rms=320 | updated_at=1777911976.5420046
- [2026-05-05 00:26:20] operator / voice_command / voice: that
  meta: normalized=True
- [2026-05-05 00:26:20] operator / voice_transcript_partial / voice: clear
  meta: kind=partial | timestamp=1777911980.0479035 | source=vosk | frequency_hz=357.4 | rms=320 | updated_at=1777911976.5420046
- [2026-05-05 00:26:20] operator / voice_transcript_partial / voice: eileen
  meta: kind=partial | timestamp=1777911980.3118486 | source=vosk | frequency_hz=357.4 | rms=320 | updated_at=1777911976.5420046
- [2026-05-05 00:26:20] operator / voice_transcript_partial / voice: aileen repeat
  meta: kind=partial | timestamp=1777911980.5503023 | source=vosk | frequency_hz=357.4 | rms=320 | updated_at=1777911976.5420046
- [2026-05-05 00:26:22] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:26:32] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777911992.3269098 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:32] operator / voice_transcript_partial / voice: sentry and
  meta: kind=partial | timestamp=1777911992.593546 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:32] operator / voice_transcript_partial / voice: sentry and enable
  meta: kind=partial | timestamp=1777911992.829626 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:33] operator / voice_transcript_partial / voice: sentry and
  meta: kind=partial | timestamp=1777911993.091694 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:33] operator / voice_transcript_partial / voice: sentry and are you
  meta: kind=partial | timestamp=1777911993.3313131 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:33] operator / voice_transcript_partial / voice: sentry and are you lion
  meta: kind=partial | timestamp=1777911993.5797718 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:33] operator / voice_transcript_partial / voice: sentry and are you lion app to
  meta: kind=partial | timestamp=1777911993.8296616 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:34] operator / voice_transcript_partial / voice: sentry and are you lion
  meta: kind=partial | timestamp=1777911994.077943 | source=vosk | frequency_hz=328.3 | rms=319 | updated_at=1777911989.823922
- [2026-05-05 00:26:34] operator / voice_transcript_partial / voice: sentry and are you last task
  meta: kind=partial | timestamp=1777911994.3284125 | source=vosk | frequency_hz=268.0 | rms=294 | updated_at=1777911994.3224034
- [2026-05-05 00:26:34] operator / voice_transcript_final / voice: sentry and are you lion task
  meta: kind=final | timestamp=1777911994.8316224 | source=final | frequency_hz=246.2 | rms=290 | updated_at=1777911994.823113
- [2026-05-05 00:26:35] operator / voice_command / voice: sentry and are you lion task
  meta: normalized=True
- [2026-05-05 00:26:36] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:39] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777911999.0774112 | source=vosk | frequency_hz=263.1 | rms=303 | updated_at=1777911998.572642
- [2026-05-05 00:26:39] operator / voice_transcript_final / voice: speed
  meta: kind=final | timestamp=1777911999.830623 | source=final | frequency_hz=256.4 | rms=286 | updated_at=1777911999.822113
- [2026-05-05 00:26:40] operator / voice_command / voice: speed
  meta: normalized=True
- [2026-05-05 00:26:41] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912002.0768507 | source=vosk | frequency_hz=298.1 | rms=297 | updated_at=1777912001.5938983
- [2026-05-05 00:26:42] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777912002.328354 | source=vosk | frequency_hz=298.1 | rms=297 | updated_at=1777912001.5938983
- [2026-05-05 00:26:43] operator / voice_transcript_final / voice: the last
  meta: kind=final | timestamp=1777912003.0779412 | source=final | frequency_hz=304.0 | rms=304 | updated_at=1777912003.071917
- [2026-05-05 00:26:43] operator / voice_command / voice: the last
  meta: normalized=True
- [2026-05-05 00:26:44] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:46] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912006.3432992 | source=vosk | frequency_hz=267.0 | rms=307 | updated_at=1777912005.9449072
- [2026-05-05 00:26:46] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912006.5784461 | source=vosk | frequency_hz=267.0 | rms=307 | updated_at=1777912005.9449072
- [2026-05-05 00:26:47] operator / voice_transcript_final / voice: smart home
  meta: kind=final | timestamp=1777912007.3518307 | source=final | frequency_hz=292.5 | rms=319 | updated_at=1777912007.3225899
- [2026-05-05 00:26:47] operator / voice_command / voice: smart home
  meta: normalized=True
- [2026-05-05 00:26:49] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:26:49] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777912009.833155 | source=vosk | frequency_hz=232.1 | rms=313 | updated_at=1777912009.3218253
- [2026-05-05 00:26:50] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777912010.0773208 | source=vosk | frequency_hz=232.1 | rms=313 | updated_at=1777912009.3218253
- [2026-05-05 00:26:50] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777912010.3320937 | source=vosk | frequency_hz=232.1 | rms=313 | updated_at=1777912009.3218253
- [2026-05-05 00:26:50] operator / voice_transcript_partial / voice: serial e be less
  meta: kind=partial | timestamp=1777912010.5765195 | source=vosk | frequency_hz=232.1 | rms=313 | updated_at=1777912009.3218253
- [2026-05-05 00:26:51] operator / voice_transcript_partial / voice: serial delay
  meta: kind=partial | timestamp=1777912011.0788293 | source=vosk | frequency_hz=232.1 | rms=313 | updated_at=1777912009.3218253
- [2026-05-05 00:26:54] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777912014.8268738 | source=vosk
- [2026-05-05 00:26:55] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777912015.069168 | source=vosk
- [2026-05-05 00:26:55] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777912015.3176484 | source=vosk
- [2026-05-05 00:26:55] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777912015.567102 | source=vosk
- [2026-05-05 00:26:55] operator / voice_transcript_partial / voice: do you speed delay that
  meta: kind=partial | timestamp=1777912015.8226862 | source=vosk
- [2026-05-05 00:26:56] operator / voice_transcript_partial / voice: do you speed delay
  meta: kind=partial | timestamp=1777912016.0671973 | source=vosk | frequency_hz=380.0 | rms=308 | updated_at=1777912016.0610957
- [2026-05-05 00:26:56] operator / voice_transcript_final / voice: do you speed delay
  meta: kind=final | timestamp=1777912016.584644 | source=final | frequency_hz=305.2 | rms=312 | updated_at=1777912016.5691288
- [2026-05-05 00:27:03] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1777912023.0906034 | source=vosk | frequency_hz=345.0 | rms=351 | updated_at=1777912022.9679306
- [2026-05-05 00:27:03] operator / voice_transcript_partial / voice: repeat that
  meta: kind=partial | timestamp=1777912023.3166254 | source=vosk | frequency_hz=345.0 | rms=351 | updated_at=1777912022.9679306
- [2026-05-05 00:27:03] operator / voice_transcript_partial / voice: repeat that e lion
  meta: kind=partial | timestamp=1777912023.9327986 | source=vosk | frequency_hz=345.0 | rms=351 | updated_at=1777912022.9679306
- [2026-05-05 00:27:04] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:27:04] operator / voice_transcript_final / voice: repeat that
  meta: kind=final | timestamp=1777912024.111742 | source=final | frequency_hz=345.0 | rms=351 | updated_at=1777912022.9679306
- [2026-05-05 00:27:05] operator / voice_command / voice: repeat that
  meta: normalized=True
- [2026-05-05 00:27:05] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777912025.0871012 | source=vosk | frequency_hz=362.0 | rms=378 | updated_at=1777912024.5618646
- [2026-05-05 00:27:05] operator / voice_command / voice: standby guarding no app to talk
  meta: normalized=True
- [2026-05-05 00:27:05] operator / voice_transcript_partial / voice: to be
  meta: kind=partial | timestamp=1777912025.5687332 | source=vosk | frequency_hz=368.3 | rms=700 | updated_at=1777912025.5617187
- [2026-05-05 00:27:06] operator / voice_transcript_final / voice: to behavior
  meta: kind=final | timestamp=1777912026.5310876 | source=final | frequency_hz=368.3 | rms=700 | updated_at=1777912025.5617187
- [2026-05-05 00:27:07] operator / voice_command / voice: to behavior
  meta: normalized=True
- [2026-05-05 00:27:11] assistant / spoken_confirmation / voice: Received. I started your background analysis about to behavior in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:27:11] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:27:11] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777912031.4006953 | source=vosk | frequency_hz=325.1 | rms=296 | updated_at=1777912030.8767602
- [2026-05-05 00:27:12] operator / voice_transcript_partial / voice: to do
  meta: kind=partial | timestamp=1777912032.629647 | source=vosk | frequency_hz=325.1 | rms=296 | updated_at=1777912030.8767602
- [2026-05-05 00:27:13] operator / voice_transcript_final / voice: to to do
  meta: kind=final | timestamp=1777912033.38107 | source=final | frequency_hz=325.1 | rms=296 | updated_at=1777912030.8767602
- [2026-05-05 00:27:14] operator / voice_command / voice: to to do
  meta: normalized=True
- [2026-05-05 00:27:13] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912033.8840508 | source=vosk | frequency_hz=325.1 | rms=296 | updated_at=1777912030.8767602
- [2026-05-05 00:27:14] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777912034.4036238 | source=final | frequency_hz=325.1 | rms=296 | updated_at=1777912030.8767602
- [2026-05-05 00:27:15] operator / voice_command / voice: do
  meta: normalized=True
- [2026-05-05 00:27:14] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912034.6291862 | source=vosk | frequency_hz=325.1 | rms=296 | updated_at=1777912030.8767602
- [2026-05-05 00:27:15] operator / voice_transcript_partial / voice: do do
  meta: kind=partial | timestamp=1777912035.4178832 | source=vosk | frequency_hz=324.0 | rms=279 | updated_at=1777912034.8760877
- [2026-05-05 00:27:15] operator / voice_transcript_partial / voice: do do it
  meta: kind=partial | timestamp=1777912035.6288888 | source=vosk | frequency_hz=324.0 | rms=279 | updated_at=1777912034.8760877
- [2026-05-05 00:27:17] operator / voice_transcript_partial / voice: do do it do it
  meta: kind=partial | timestamp=1777912037.047908 | source=vosk | frequency_hz=324.0 | rms=279 | updated_at=1777912034.8760877
- [2026-05-05 00:27:17] operator / voice_transcript_partial / voice: do do it
  meta: kind=partial | timestamp=1777912037.0734746 | source=vosk | frequency_hz=324.0 | rms=279 | updated_at=1777912034.8760877
- [2026-05-05 00:27:17] operator / voice_transcript_partial / voice: do do it status
  meta: kind=partial | timestamp=1777912037.0899842 | source=vosk | frequency_hz=324.0 | rms=279 | updated_at=1777912034.8760877
- [2026-05-05 00:27:17] operator / voice_transcript_partial / voice: do do it do it to
  meta: kind=partial | timestamp=1777912037.3047163 | source=vosk | frequency_hz=324.0 | rms=279 | updated_at=1777912034.8760877
- [2026-05-05 00:27:18] operator / voice_transcript_final / voice: do do it do it to
  meta: kind=final | timestamp=1777912038.319442 | source=final | frequency_hz=256.0 | rms=291 | updated_at=1777912038.299207
- [2026-05-05 00:27:19] operator / voice_command / voice: do do it do it to
  meta: normalized=True
- [2026-05-05 00:27:19] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777912039.8053093 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:20] operator / voice_transcript_partial / voice: lion abort
  meta: kind=partial | timestamp=1777912040.0697758 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:20] operator / voice_transcript_partial / voice: lion a boards and
  meta: kind=partial | timestamp=1777912040.562867 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:21] operator / voice_transcript_partial / voice: lion a boards and enable
  meta: kind=partial | timestamp=1777912041.0555933 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:21] operator / voice_transcript_partial / voice: lion a boards and
  meta: kind=partial | timestamp=1777912041.381373 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:22] operator / voice_transcript_partial / voice: lion a boards and response
  meta: kind=partial | timestamp=1777912042.034111 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:22] operator / voice_transcript_partial / voice: lion a boards and smart
  meta: kind=partial | timestamp=1777912042.0621285 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:22] operator / voice_transcript_partial / voice: lion a boards and smart the smart
  meta: kind=partial | timestamp=1777912042.0838003 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:22] operator / voice_transcript_partial / voice: lion a boards and smart response
  meta: kind=partial | timestamp=1777912042.3598862 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:22] operator / voice_transcript_partial / voice: lion a boards and smart less strict
  meta: kind=partial | timestamp=1777912042.5770328 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:22] operator / voice_transcript_partial / voice: lion a boards and smart disconnect less
  meta: kind=partial | timestamp=1777912042.8284342 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:23] operator / voice_transcript_partial / voice: lion a boards and smart less silence
  meta: kind=partial | timestamp=1777912043.0558853 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:24] operator / voice_transcript_partial / voice: lion a boards and smart less say
  meta: kind=partial | timestamp=1777912044.0879648 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:24] operator / voice_transcript_partial / voice: lion a boards and smart less say e
  meta: kind=partial | timestamp=1777912044.1309214 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:24] operator / voice_transcript_partial / voice: lion a boards and smart less silence threshold
  meta: kind=partial | timestamp=1777912044.3679717 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:24] operator / voice_transcript_partial / voice: lion a boards and smart less say e do
  meta: kind=partial | timestamp=1777912044.6014178 | source=vosk | frequency_hz=246.2 | rms=295 | updated_at=1777912038.5497985
- [2026-05-05 00:27:25] operator / voice_transcript_final / voice: stop that
  meta: kind=final | timestamp=1777912045.1315653 | source=final | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:26] operator / voice_command / voice: stop that
  meta: normalized=True
- [2026-05-05 00:27:25] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912045.350221 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:25] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777912045.8540475 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:26] operator / voice_transcript_partial / voice: do app
  meta: kind=partial | timestamp=1777912046.1286747 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:26] operator / voice_transcript_partial / voice: do app identify
  meta: kind=partial | timestamp=1777912046.41701 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:26] operator / voice_transcript_partial / voice: do enable that again
  meta: kind=partial | timestamp=1777912046.6343598 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:26] operator / voice_transcript_partial / voice: do app eileen repeat
  meta: kind=partial | timestamp=1777912046.8530095 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:27] operator / voice_transcript_partial / voice: do app eileen be less
  meta: kind=partial | timestamp=1777912047.3889432 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:28] assistant / spoken_confirmation / voice: Cancelled background analysis about to behavior. What do you want me to do next?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:27:27] operator / voice_transcript_partial / voice: do app eileen be less elian
  meta: kind=partial | timestamp=1777912047.8686218 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:27:28] operator / voice_transcript_partial / voice: do app eileen be less a lion
  meta: kind=partial | timestamp=1777912048.1302726 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:28] operator / voice_transcript_partial / voice: do app eileen be less analyze
  meta: kind=partial | timestamp=1777912048.3783145 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:28] operator / voice_transcript_partial / voice: do app eileen be less elian no
  meta: kind=partial | timestamp=1777912048.603757 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:28] operator / voice_transcript_partial / voice: do app eileen be less elian no and
  meta: kind=partial | timestamp=1777912048.8529959 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:29] operator / voice_transcript_partial / voice: do app eileen be less elian no and enable
  meta: kind=partial | timestamp=1777912049.8196082 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:31] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:27:29] operator / voice_transcript_partial / voice: do app eileen be less elian never mind
  meta: kind=partial | timestamp=1777912049.8536904 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:31] operator / voice_transcript_final / voice: do app be less elian no and never mind
  meta: kind=final | timestamp=1777912051.2450228 | source=final | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:33] operator / voice_command / voice: do app be less elian no and never mind
  meta: normalized=True
- [2026-05-05 00:27:31] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777912051.3882825 | source=vosk | frequency_hz=344.0 | rms=656 | updated_at=1777912044.842379
- [2026-05-05 00:27:32] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777912052.2869594 | source=final | frequency_hz=286.7 | rms=348 | updated_at=1777912052.2390604
- [2026-05-05 00:27:34] operator / voice_command / voice: do
  meta: normalized=True
- [2026-05-05 00:27:36] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1777912056.6341531 | source=vosk | frequency_hz=277.6 | rms=322 | updated_at=1777912056.1264348
- [2026-05-05 00:27:36] operator / voice_transcript_partial / voice: but faster
  meta: kind=partial | timestamp=1777912056.879245 | source=vosk | frequency_hz=302.9 | rms=318 | updated_at=1777912056.8712368
- [2026-05-05 00:27:47] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777912067.248836 | source=vosk | frequency_hz=350.5 | rms=346 | updated_at=1777912067.2396219
- [2026-05-05 00:27:48] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777912068.2474146 | source=final | frequency_hz=316.0 | rms=271 | updated_at=1777912068.2393951
- [2026-05-05 00:27:48] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:27:52] operator / voice_transcript_partial / voice: disable
  meta: kind=partial | timestamp=1777912072.2460842 | source=vosk | frequency_hz=315.1 | rms=264 | updated_at=1777912070.989557
- [2026-05-05 00:27:52] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777912072.4951425 | source=vosk | frequency_hz=315.1 | rms=264 | updated_at=1777912070.989557
- [2026-05-05 00:27:52] operator / voice_transcript_partial / voice: say sentry
  meta: kind=partial | timestamp=1777912072.7625756 | source=vosk | frequency_hz=315.1 | rms=264 | updated_at=1777912070.989557
- [2026-05-05 00:27:53] operator / voice_transcript_partial / voice: say sentry do it
  meta: kind=partial | timestamp=1777912073.4951122 | source=vosk | frequency_hz=315.1 | rms=264 | updated_at=1777912070.989557
- [2026-05-05 00:27:53] operator / voice_transcript_partial / voice: say sentry do it e
  meta: kind=partial | timestamp=1777912073.752474 | source=vosk | frequency_hz=364.0 | rms=266 | updated_at=1777912073.738639
- [2026-05-05 00:27:53] operator / voice_transcript_partial / voice: say sentry do it e lion
  meta: kind=partial | timestamp=1777912073.996401 | source=vosk | frequency_hz=323.4 | rms=267 | updated_at=1777912073.9893792
- [2026-05-05 00:27:54] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:27:54] operator / voice_transcript_final / voice: say sentry delay
  meta: kind=final | timestamp=1777912074.5362465 | source=final | frequency_hz=332.0 | rms=278 | updated_at=1777912074.238908
- [2026-05-05 00:27:55] operator / voice_command / voice: say sentry delay
  meta: normalized=True
- [2026-05-05 00:27:58] operator / voice_transcript_partial / voice: silence
  meta: kind=partial | timestamp=1777912078.7631724 | source=vosk | frequency_hz=331.8 | rms=265 | updated_at=1777912077.7407372
- [2026-05-05 00:27:59] operator / voice_transcript_partial / voice: silence threshold
  meta: kind=partial | timestamp=1777912079.25329 | source=vosk | frequency_hz=331.8 | rms=265 | updated_at=1777912077.7407372
- [2026-05-05 00:28:00] operator / voice_transcript_final / voice: silence
  meta: kind=final | timestamp=1777912080.5396821 | source=final | frequency_hz=285.8 | rms=272 | updated_at=1777912080.239194
- [2026-05-05 00:28:01] operator / voice_command / voice: silence
  meta: normalized=True
- [2026-05-05 00:28:06] operator / voice_transcript_partial / voice: commands
  meta: kind=partial | timestamp=1777912086.74688 | source=vosk | frequency_hz=336.0 | rms=293 | updated_at=1777912085.9897888
- [2026-05-05 00:28:06] operator / voice_transcript_partial / voice: mode
  meta: kind=partial | timestamp=1777912086.9997642 | source=vosk | frequency_hz=336.0 | rms=293 | updated_at=1777912085.9897888
- [2026-05-05 00:28:07] operator / voice_transcript_partial / voice: mode disable
  meta: kind=partial | timestamp=1777912087.2530975 | source=vosk | frequency_hz=314.3 | rms=295 | updated_at=1777912087.243542
- [2026-05-05 00:28:07] operator / voice_transcript_partial / voice: mode
  meta: kind=partial | timestamp=1777912087.4966114 | source=vosk | frequency_hz=310.7 | rms=275 | updated_at=1777912087.4895985
- [2026-05-05 00:28:07] operator / voice_transcript_partial / voice: mode to sentry board
  meta: kind=partial | timestamp=1777912087.7494156 | source=vosk | frequency_hz=310.7 | rms=275 | updated_at=1777912087.4895985
- [2026-05-05 00:28:08] operator / voice_transcript_final / voice: mode to sentry board
  meta: kind=final | timestamp=1777912088.2494493 | source=final | frequency_hz=323.4 | rms=284 | updated_at=1777912088.2399302
- [2026-05-05 00:28:08] operator / voice_command / voice: mode to sentry board
  meta: normalized=True
- [2026-05-05 00:28:10] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912090.7471104 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:11] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912091.0101268 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:11] operator / voice_transcript_partial / voice: smart sentry decrease
  meta: kind=partial | timestamp=1777912091.518443 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:11] operator / voice_transcript_partial / voice: smart sentry the last
  meta: kind=partial | timestamp=1777912091.7596376 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:11] operator / voice_transcript_partial / voice: smart sentry the smart but
  meta: kind=partial | timestamp=1777912091.9958448 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:12] operator / voice_transcript_partial / voice: smart sentry the smart behaviour
  meta: kind=partial | timestamp=1777912092.2462099 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:13] operator / voice_transcript_partial / voice: smart sentry the smart sentry
  meta: kind=partial | timestamp=1777912093.3518972 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:13] operator / voice_transcript_partial / voice: smart sentry the smart sentry the
  meta: kind=partial | timestamp=1777912093.3591754 | source=vosk | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:13] operator / voice_transcript_final / voice: smart sentry the smart but say sentry
  meta: kind=final | timestamp=1777912093.615344 | source=final | frequency_hz=340.6 | rms=271 | updated_at=1777912089.4902742
- [2026-05-05 00:28:16] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777912096.6088977 | source=vosk | frequency_hz=315.4 | rms=279 | updated_at=1777912095.6118267
- [2026-05-05 00:28:17] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912097.1110616 | source=vosk | frequency_hz=304.4 | rms=268 | updated_at=1777912096.8530765
- [2026-05-05 00:28:17] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777912097.6096978 | source=vosk | frequency_hz=304.4 | rms=268 | updated_at=1777912096.8530765
- [2026-05-05 00:28:17] operator / voice_transcript_partial / voice: say serial
  meta: kind=partial | timestamp=1777912097.861779 | source=vosk | frequency_hz=304.4 | rms=268 | updated_at=1777912096.8530765
- [2026-05-05 00:28:18] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912098.1088989 | source=vosk | frequency_hz=304.4 | rms=268 | updated_at=1777912096.8530765
- [2026-05-05 00:28:18] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777912098.610715 | source=final | frequency_hz=304.4 | rms=268 | updated_at=1777912096.8530765
- [2026-05-05 00:28:21] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912101.373207 | source=vosk | frequency_hz=319.0 | rms=283 | updated_at=1777912100.6216083
- [2026-05-05 00:28:21] operator / voice_transcript_partial / voice: alion analyze
  meta: kind=partial | timestamp=1777912101.859487 | source=vosk | frequency_hz=351.5 | rms=327 | updated_at=1777912101.8530958
- [2026-05-05 00:28:22] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:28:22] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777912102.1172557 | source=vosk | frequency_hz=351.5 | rms=327 | updated_at=1777912101.8530958
- [2026-05-05 00:28:22] operator / voice_transcript_partial / voice: go mind
  meta: kind=partial | timestamp=1777912102.6088467 | source=vosk | frequency_hz=351.5 | rms=327 | updated_at=1777912101.8530958
- [2026-05-05 00:28:24] operator / voice_transcript_final / voice: go mind
  meta: kind=final | timestamp=1777912104.046987 | source=final | frequency_hz=351.5 | rms=327 | updated_at=1777912101.8530958
- [2026-05-05 00:28:25] operator / voice_command / voice: go mind
  meta: normalized=True
- [2026-05-05 00:28:25] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777912105.324953 | source=vosk | frequency_hz=351.5 | rms=327 | updated_at=1777912101.8530958
- [2026-05-05 00:28:26] operator / voice_transcript_partial / voice: queued tasks
  meta: kind=partial | timestamp=1777912106.5585587 | source=vosk | frequency_hz=351.5 | rms=327 | updated_at=1777912101.8530958
- [2026-05-05 00:28:26] operator / voice_transcript_partial / voice: who to
  meta: kind=partial | timestamp=1777912106.8057332 | source=vosk | frequency_hz=260.0 | rms=280 | updated_at=1777912106.798717
- [2026-05-05 00:28:27] operator / voice_transcript_partial / voice: who to go
  meta: kind=partial | timestamp=1777912107.0555673 | source=vosk | frequency_hz=269.8 | rms=265 | updated_at=1777912107.0489318
- [2026-05-05 00:28:27] operator / voice_transcript_final / voice: who to go
  meta: kind=final | timestamp=1777912107.8078706 | source=final | frequency_hz=269.8 | rms=265 | updated_at=1777912107.0489318
- [2026-05-05 00:28:28] operator / voice_command / voice: who to go
  meta: normalized=True
- [2026-05-05 00:28:32] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912112.567977 | source=vosk | frequency_hz=291.0 | rms=314 | updated_at=1777912112.0489268
- [2026-05-05 00:28:32] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777912112.8243494 | source=vosk | frequency_hz=291.0 | rms=314 | updated_at=1777912112.0489268
- [2026-05-05 00:28:33] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777912113.0583587 | source=vosk | frequency_hz=291.0 | rms=314 | updated_at=1777912112.0489268
- [2026-05-05 00:28:34] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:28:33] operator / voice_transcript_final / voice: it
  meta: kind=final | timestamp=1777912113.5656362 | source=final | frequency_hz=384.0 | rms=317 | updated_at=1777912113.5586166
- [2026-05-05 00:28:35] operator / voice_command / voice: it
  meta: normalized=True
- [2026-05-05 00:28:33] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912113.575897 | source=vosk | frequency_hz=354.6 | rms=302 | updated_at=1777912113.5676358
- [2026-05-05 00:28:34] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777912114.9484742 | source=final | frequency_hz=314.9 | rms=312 | updated_at=1777912114.0547862
- [2026-05-05 00:28:36] operator / voice_command / voice: the
  meta: normalized=True
- [2026-05-05 00:28:41] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912121.8316214 | source=vosk | frequency_hz=330.6 | rms=315 | updated_at=1777912121.3046105
- [2026-05-05 00:28:42] operator / voice_transcript_partial / voice: decrease brightness
  meta: kind=partial | timestamp=1777912122.5897262 | source=vosk | frequency_hz=338.1 | rms=386 | updated_at=1777912122.3055987
- [2026-05-05 00:28:42] operator / voice_transcript_final / voice: yourself
  meta: kind=final | timestamp=1777912122.8126447 | source=final | frequency_hz=313.6 | rms=326 | updated_at=1777912122.80463
- [2026-05-05 00:28:43] operator / voice_command / voice: yourself
  meta: normalized=True
- [2026-05-05 00:28:49] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777912129.8113403 | source=vosk | frequency_hz=350.9 | rms=328 | updated_at=1777912129.8048372
- [2026-05-05 00:28:50] operator / voice_transcript_final / voice: it again
  meta: kind=final | timestamp=1777912130.7358851 | source=final | frequency_hz=327.5 | rms=314 | updated_at=1777912130.0544233
- [2026-05-05 00:28:51] operator / voice_transcript_final / voice: tasks
  meta: kind=final | timestamp=1777912131.8857036 | source=final | frequency_hz=332.2 | rms=506 | updated_at=1777912131.8111105
- [2026-05-05 00:28:55] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777912135.5980043 | source=vosk | frequency_hz=245.2 | rms=289 | updated_at=1777912134.5851164
- [2026-05-05 00:29:01] operator / voice_transcript_partial / voice: same but
  meta: kind=partial | timestamp=1777912141.5948544 | source=vosk | frequency_hz=325.5 | rms=282 | updated_at=1777912140.0868428
- [2026-05-05 00:29:01] operator / voice_transcript_partial / voice: say that decrease
  meta: kind=partial | timestamp=1777912141.8440397 | source=vosk | frequency_hz=325.5 | rms=282 | updated_at=1777912140.0868428
- [2026-05-05 00:29:02] operator / voice_transcript_final / voice: say that
  meta: kind=final | timestamp=1777912142.102119 | source=final | frequency_hz=325.5 | rms=282 | updated_at=1777912140.0868428
- [2026-05-05 00:29:02] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912142.854027 | source=vosk | frequency_hz=400.0 | rms=287 | updated_at=1777912142.8356078
- [2026-05-05 00:29:07] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777912147.0923479 | source=final | frequency_hz=352.7 | rms=306 | updated_at=1777912147.0857637
- [2026-05-05 00:29:12] operator / voice_transcript_final / voice: last
  meta: kind=final | timestamp=1777912152.1359105 | source=final | frequency_hz=323.2 | rms=278 | updated_at=1777912151.5893686
- [2026-05-05 00:29:14] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777912154.843787 | source=vosk | frequency_hz=317.7 | rms=282 | updated_at=1777912154.0859048
- [2026-05-05 00:29:15] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777912155.5916498 | source=vosk | frequency_hz=320.0 | rms=284 | updated_at=1777912155.5861447
- [2026-05-05 00:29:16] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777912156.3554487 | source=final | frequency_hz=296.8 | rms=293 | updated_at=1777912156.0856686
- [2026-05-05 00:29:17] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:29:16] operator / voice_transcript_partial / voice: anything
  meta: kind=partial | timestamp=1777912156.8598943 | source=vosk | frequency_hz=296.8 | rms=293 | updated_at=1777912156.0856686
- [2026-05-05 00:29:17] operator / voice_transcript_partial / voice: elliot go
  meta: kind=partial | timestamp=1777912157.1172125 | source=vosk | frequency_hz=296.8 | rms=293 | updated_at=1777912156.0856686
- [2026-05-05 00:29:17] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912157.5924194 | source=vosk | frequency_hz=296.8 | rms=293 | updated_at=1777912156.0856686
- [2026-05-05 00:29:30] operator / voice_transcript_partial / voice: home override
  meta: kind=partial | timestamp=1777912170.7677116 | source=vosk | frequency_hz=249.0 | rms=283 | updated_at=1777912169.9875379
- [2026-05-05 00:29:31] operator / voice_transcript_final / voice: home override
  meta: kind=final | timestamp=1777912171.7652726 | source=final | frequency_hz=249.0 | rms=283 | updated_at=1777912169.9875379
- [2026-05-05 00:29:32] operator / voice_command / voice: home override
  meta: normalized=True
- [2026-05-05 00:29:34] assistant / spoken_confirmation / voice: I think I heard home. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:29:42] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912182.7439666 | source=vosk | frequency_hz=348.3 | rms=315 | updated_at=1777912182.7379568
- [2026-05-05 00:29:45] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777912185.5476341 | source=vosk | frequency_hz=249.3 | rms=301 | updated_at=1777912184.7378724
- [2026-05-05 00:29:46] operator / voice_transcript_partial / voice: connect serial
  meta: kind=partial | timestamp=1777912186.4923828 | source=vosk | frequency_hz=249.3 | rms=301 | updated_at=1777912184.7378724
- [2026-05-05 00:29:47] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777912187.4961026 | source=final | frequency_hz=366.6 | rms=304 | updated_at=1777912187.488592
- [2026-05-05 00:29:48] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 00:29:48] operator / voice_transcript_partial / voice: com
  meta: kind=partial | timestamp=1777912188.4921298 | source=vosk | frequency_hz=376.2 | rms=311 | updated_at=1777912188.4876242
- [2026-05-05 00:29:49] operator / voice_transcript_final / voice: com
  meta: kind=final | timestamp=1777912189.2440734 | source=final | frequency_hz=302.9 | rms=297 | updated_at=1777912189.2380626
- [2026-05-05 00:29:49] operator / voice_command / voice: com
  meta: normalized=True
- [2026-05-05 00:29:50] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:29:50] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:29:51] assistant / spoken_confirmation / voice: No confirmation received. I did not run home.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:31:59] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912319.309727 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:31:59] operator / voice_transcript_partial / voice: do it again
  meta: kind=partial | timestamp=1777912319.4308054 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:31:59] operator / voice_transcript_partial / voice: do it again a
  meta: kind=partial | timestamp=1777912319.9061608 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:00] operator / voice_transcript_partial / voice: do it again a lion
  meta: kind=partial | timestamp=1777912320.1580968 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:00] operator / voice_transcript_partial / voice: do it again a
  meta: kind=partial | timestamp=1777912320.407947 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:00] operator / voice_transcript_partial / voice: do it again a do
  meta: kind=partial | timestamp=1777912320.658345 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:01] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1777912321.2256508 | source=final | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:01] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-05 00:32:02] operator / voice_command / voice: standby guarding no app to talk
  meta: normalized=True
- [2026-05-05 00:32:03] operator / voice_transcript_partial / voice: theme
  meta: kind=partial | timestamp=1777912323.3490088 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:03] operator / voice_transcript_partial / voice: theme to
  meta: kind=partial | timestamp=1777912323.779886 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:03] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912323.901775 | source=vosk | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:04] operator / voice_transcript_final / voice: theme
  meta: kind=final | timestamp=1777912324.468502 | source=final | frequency_hz=325.3 | rms=244 | updated_at=1777912318.4015923
- [2026-05-05 00:32:06] operator / voice_command / voice: theme
  meta: normalized=True
- [2026-05-05 00:32:08] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:32:08] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:32:09] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777912329.0754743 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:09] operator / voice_transcript_partial / voice: repeat it be
  meta: kind=partial | timestamp=1777912329.5790265 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:09] operator / voice_transcript_partial / voice: repeat it the smart
  meta: kind=partial | timestamp=1777912329.8242147 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:10] operator / voice_transcript_partial / voice: repeat it be silence
  meta: kind=partial | timestamp=1777912330.0744476 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:10] operator / voice_transcript_partial / voice: repeat it the com
  meta: kind=partial | timestamp=1777912330.3479445 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:10] operator / voice_transcript_final / voice: repeat it be less
  meta: kind=final | timestamp=1777912330.5810971 | source=final | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:11] operator / voice_command / voice: repeat it be less
  meta: normalized=True
- [2026-05-05 00:32:10] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777912330.8255885 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:11] operator / voice_transcript_partial / voice: go what
  meta: kind=partial | timestamp=1777912331.073206 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:11] operator / voice_transcript_partial / voice: go what do
  meta: kind=partial | timestamp=1777912331.3419726 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:11] operator / voice_transcript_partial / voice: go what do it
  meta: kind=partial | timestamp=1777912331.5744522 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:11] operator / voice_transcript_partial / voice: go what do
  meta: kind=partial | timestamp=1777912331.824234 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:12] operator / voice_transcript_final / voice: go what do
  meta: kind=final | timestamp=1777912332.1054976 | source=final | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:13] operator / voice_command / voice: go what do
  meta: normalized=True
- [2026-05-05 00:32:12] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912332.5742798 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:13] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777912333.079712 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:13] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777912333.334232 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:14] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:32:13] operator / voice_transcript_partial / voice: repeat it again
  meta: kind=partial | timestamp=1777912333.5729175 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:14] operator / voice_transcript_final / voice: repeat it
  meta: kind=final | timestamp=1777912334.154608 | source=final | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:15] operator / voice_command / voice: repeat it
  meta: normalized=True
- [2026-05-05 00:32:14] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912334.3658864 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:14] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777912334.576149 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:15] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:32:15] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:32:15] operator / voice_transcript_partial / voice: boards and
  meta: kind=partial | timestamp=1777912335.0763733 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:15] operator / voice_transcript_partial / voice: elliot abort current
  meta: kind=partial | timestamp=1777912335.3319967 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:15] operator / voice_transcript_partial / voice: boards who
  meta: kind=partial | timestamp=1777912335.5753362 | source=vosk | frequency_hz=367.1 | rms=270 | updated_at=1777912327.8188128
- [2026-05-05 00:32:15] operator / voice_transcript_partial / voice: alien repeat it
  meta: kind=partial | timestamp=1777912335.8258908 | source=vosk | frequency_hz=404.0 | rms=296 | updated_at=1777912335.8198812
- [2026-05-05 00:32:16] operator / voice_transcript_partial / voice: alien who to the
  meta: kind=partial | timestamp=1777912336.0882468 | source=vosk | frequency_hz=404.0 | rms=296 | updated_at=1777912335.8198812
- [2026-05-05 00:32:16] operator / voice_transcript_partial / voice: alien who to the last
  meta: kind=partial | timestamp=1777912336.3247352 | source=vosk | frequency_hz=404.0 | rms=296 | updated_at=1777912335.8198812
- [2026-05-05 00:32:16] operator / voice_transcript_final / voice: who to the last
  meta: kind=final | timestamp=1777912336.8297994 | source=final | frequency_hz=404.0 | rms=296 | updated_at=1777912335.8198812
- [2026-05-05 00:32:17] operator / voice_command / voice: who to the last
  meta: normalized=True
- [2026-05-05 00:32:17] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912337.084169 | source=vosk | frequency_hz=404.0 | rms=296 | updated_at=1777912335.8198812
- [2026-05-05 00:32:17] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777912337.344008 | source=vosk | frequency_hz=404.0 | rms=296 | updated_at=1777912335.8198812
- [2026-05-05 00:32:21] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912341.5162117 | source=vosk | frequency_hz=326.1 | rms=284 | updated_at=1777912341.3199372
- [2026-05-05 00:32:22] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1777912342.6185627 | source=final | frequency_hz=326.1 | rms=284 | updated_at=1777912341.3199372
- [2026-05-05 00:32:24] operator / voice_command / voice: you
  meta: normalized=True
- [2026-05-05 00:32:22] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777912342.9806063 | source=vosk | frequency_hz=326.1 | rms=284 | updated_at=1777912341.3199372
- [2026-05-05 00:32:23] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777912343.8620884 | source=final | frequency_hz=320.0 | rms=269 | updated_at=1777912343.2295392
- [2026-05-05 00:32:25] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-05 00:33:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912403.803905 | source=vosk | frequency_hz=248.5 | rms=400 | updated_at=1777912402.2985396
- [2026-05-05 00:33:24] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777912404.556051 | source=final | frequency_hz=278.8 | rms=290 | updated_at=1777912404.2984307

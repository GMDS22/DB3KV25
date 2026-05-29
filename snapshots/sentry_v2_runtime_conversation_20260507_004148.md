# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-07 00:41:48
- Entries: 156
- Roles: {'assistant': 4, 'system': 1, 'operator': 151}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_final': 33, 'voice_transcript_partial': 116, 'voice_command': 2, 'spoken_confirmation': 2}
- Channels: {'text': 2, 'voice': 154}
- Latest operator request: acoustic guard
- Latest assistant message: Absolutely. Tell me a voice style like British male or British female.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-07 00:33:55] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-07 00:33:55] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-07 00:33:58] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778085238.5548391 | source=vosk
- [2026-05-07 00:34:19] operator / voice_transcript_final / voice: sound
  meta: kind=final | timestamp=1778085259.43323 | source=final | frequency_hz=320.0 | rms=402 | updated_at=1778085259.3374476
- [2026-05-07 00:34:32] operator / voice_transcript_partial / voice: hey turn
  meta: kind=partial | timestamp=1778085272.3435254 | source=vosk | frequency_hz=306.1 | rms=371 | updated_at=1778085272.3378437
- [2026-05-07 00:34:32] operator / voice_transcript_partial / voice: hey what
  meta: kind=partial | timestamp=1778085272.5959399 | source=vosk | frequency_hz=332.0 | rms=363 | updated_at=1778085272.5876908
- [2026-05-07 00:34:33] operator / voice_transcript_final / voice: hey what
  meta: kind=final | timestamp=1778085273.1937146 | source=final | frequency_hz=314.2 | rms=381 | updated_at=1778085273.0873368
- [2026-05-07 00:35:46] operator / voice_transcript_partial / voice: switching
  meta: kind=partial | timestamp=1778085346.348672 | source=vosk | frequency_hz=333.9 | rms=367 | updated_at=1778085345.3412857
- [2026-05-07 00:35:46] operator / voice_transcript_final / voice: switching
  meta: kind=final | timestamp=1778085346.9575987 | source=final | frequency_hz=289.2 | rms=363 | updated_at=1778085346.841387
- [2026-05-07 00:35:49] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1778085349.0984685 | source=vosk | frequency_hz=285.7 | rms=357 | updated_at=1778085348.3418024
- [2026-05-07 00:35:49] operator / voice_transcript_partial / voice: in servo a
  meta: kind=partial | timestamp=1778085349.8484392 | source=vosk | frequency_hz=316.6 | rms=376 | updated_at=1778085349.8414311
- [2026-05-07 00:35:50] operator / voice_transcript_final / voice: in switching
  meta: kind=final | timestamp=1778085350.472715 | source=final | frequency_hz=315.6 | rms=377 | updated_at=1778085350.3411782
- [2026-05-07 00:35:51] operator / voice_transcript_partial / voice: switching
  meta: kind=partial | timestamp=1778085351.5985599 | source=vosk | frequency_hz=317.1 | rms=368 | updated_at=1778085350.5917642
- [2026-05-07 00:35:51] operator / voice_transcript_partial / voice: switch
  meta: kind=partial | timestamp=1778085351.8489597 | source=vosk | frequency_hz=317.1 | rms=368 | updated_at=1778085350.5917642
- [2026-05-07 00:35:52] operator / voice_transcript_final / voice: switch
  meta: kind=final | timestamp=1778085352.459154 | source=final | frequency_hz=340.0 | rms=385 | updated_at=1778085352.0913036
- [2026-05-07 00:35:53] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1778085353.3478994 | source=vosk | frequency_hz=356.2 | rms=374 | updated_at=1778085353.341384
- [2026-05-07 00:35:54] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1778085354.2105348 | source=final | frequency_hz=291.3 | rms=374 | updated_at=1778085354.0916195
- [2026-05-07 00:36:00] operator / voice_transcript_partial / voice: training
  meta: kind=partial | timestamp=1778085360.1003985 | source=vosk | frequency_hz=342.5 | rms=376 | updated_at=1778085359.3459985
- [2026-05-07 00:36:00] operator / voice_transcript_partial / voice: trace
  meta: kind=partial | timestamp=1778085360.3512034 | source=vosk | frequency_hz=342.5 | rms=376 | updated_at=1778085359.3459985
- [2026-05-07 00:36:00] operator / voice_transcript_partial / voice: trace enabled
  meta: kind=partial | timestamp=1778085360.600304 | source=vosk | frequency_hz=342.5 | rms=376 | updated_at=1778085359.3459985
- [2026-05-07 00:36:00] operator / voice_transcript_final / voice: trace
  meta: kind=final | timestamp=1778085360.9621725 | source=final | frequency_hz=342.5 | rms=376 | updated_at=1778085359.3459985
- [2026-05-07 00:36:57] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1778085417.3506763 | source=vosk | frequency_hz=340.4 | rms=386 | updated_at=1778085416.5947552
- [2026-05-07 00:36:57] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1778085417.8521433 | source=vosk | frequency_hz=340.4 | rms=386 | updated_at=1778085416.5947552
- [2026-05-07 00:36:59] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778085419.1127186 | source=final | frequency_hz=295.9 | rms=364 | updated_at=1778085419.0968435
- [2026-05-07 00:36:59] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-07 00:37:00] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-07 00:37:15] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778085435.7178755 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:15] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778085435.9675684 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:16] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778085436.31625 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:16] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778085436.9722915 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:17] operator / voice_transcript_partial / voice: change your voice to anything
  meta: kind=partial | timestamp=1778085437.2226017 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:17] operator / voice_transcript_partial / voice: change your voice to e lion
  meta: kind=partial | timestamp=1778085437.4673877 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:17] operator / voice_transcript_partial / voice: change your voice to e the
  meta: kind=partial | timestamp=1778085437.727721 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:17] operator / voice_transcript_partial / voice: change your voice to e the window
  meta: kind=partial | timestamp=1778085437.991696 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:18] operator / voice_transcript_partial / voice: change your voice to e the window shortcuts
  meta: kind=partial | timestamp=1778085438.2236469 | source=vosk | frequency_hz=264.0 | rms=294 | updated_at=1778085424.9599788
- [2026-05-07 00:37:18] operator / voice_transcript_partial / voice: change your voice to e the window
  meta: kind=partial | timestamp=1778085438.469732 | source=vosk | frequency_hz=340.0 | rms=374 | updated_at=1778085438.4617128
- [2026-05-07 00:37:18] operator / voice_transcript_partial / voice: change your voice to e the window name
  meta: kind=partial | timestamp=1778085438.716351 | source=vosk | frequency_hz=340.0 | rms=374 | updated_at=1778085438.4617128
- [2026-05-07 00:37:19] operator / voice_transcript_final / voice: change your voice to e the window view
  meta: kind=final | timestamp=1778085439.6054862 | source=final | frequency_hz=340.0 | rms=374 | updated_at=1778085438.4617128
- [2026-05-07 00:37:20] operator / voice_command / voice: change your voice to e the window view
  meta: normalized=True
- [2026-05-07 00:37:20] assistant / spoken_confirmation / voice: Absolutely. Tell me a voice style like British male or British female.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-07 00:37:26] operator / voice_transcript_partial / voice: tell me voice style camera running
  meta: kind=partial | timestamp=1778085446.2240536 | source=vosk | frequency_hz=348.0 | rms=369 | updated_at=1778085442.2148206
- [2026-05-07 00:37:26] operator / voice_transcript_final / voice: tell me voice style camera
  meta: kind=final | timestamp=1778085446.677272 | source=final | frequency_hz=348.0 | rms=369 | updated_at=1778085442.2148206
- [2026-05-07 00:37:27] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778085447.9679534 | source=vosk | frequency_hz=348.0 | rms=369 | updated_at=1778085442.2148206
- [2026-05-07 00:37:28] operator / voice_transcript_partial / voice: change your to
  meta: kind=partial | timestamp=1778085448.2198408 | source=vosk | frequency_hz=348.0 | rms=369 | updated_at=1778085442.2148206
- [2026-05-07 00:37:28] operator / voice_transcript_partial / voice: change your to ml
  meta: kind=partial | timestamp=1778085448.7186646 | source=vosk | frequency_hz=348.0 | rms=369 | updated_at=1778085442.2148206
- [2026-05-07 00:37:29] operator / voice_transcript_partial / voice: change your to ml logging disabled
  meta: kind=partial | timestamp=1778085449.0091918 | source=vosk | frequency_hz=348.0 | rms=369 | updated_at=1778085442.2148206
- [2026-05-07 00:37:29] operator / voice_transcript_partial / voice: change your to media loop
  meta: kind=partial | timestamp=1778085449.2241435 | source=vosk | frequency_hz=420.0 | rms=372 | updated_at=1778085449.2161157
- [2026-05-07 00:37:30] operator / voice_transcript_final / voice: change your to ml media
  meta: kind=final | timestamp=1778085450.1483727 | source=final | frequency_hz=364.0 | rms=392 | updated_at=1778085449.7113721
- [2026-05-07 00:37:38] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778085458.4750247 | source=vosk | frequency_hz=328.4 | rms=360 | updated_at=1778085457.2109544
- [2026-05-07 00:37:38] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778085458.717024 | source=vosk | frequency_hz=328.4 | rms=360 | updated_at=1778085457.2109544
- [2026-05-07 00:37:39] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778085459.348735 | source=vosk | frequency_hz=328.4 | rms=360 | updated_at=1778085457.2109544
- [2026-05-07 00:37:39] operator / voice_transcript_partial / voice: change your voice to one
  meta: kind=partial | timestamp=1778085459.4721754 | source=vosk | frequency_hz=328.4 | rms=360 | updated_at=1778085457.2109544
- [2026-05-07 00:37:39] operator / voice_transcript_partial / voice: change your voice to one in human
  meta: kind=partial | timestamp=1778085459.9739983 | source=vosk | frequency_hz=328.4 | rms=360 | updated_at=1778085457.2109544
- [2026-05-07 00:37:40] operator / voice_transcript_partial / voice: change your voice to one alien
  meta: kind=partial | timestamp=1778085460.2248955 | source=vosk | frequency_hz=414.0 | rms=411 | updated_at=1778085460.214
- [2026-05-07 00:37:40] operator / voice_transcript_partial / voice: change your voice to one alien manual
  meta: kind=partial | timestamp=1778085460.4671068 | source=vosk | frequency_hz=414.0 | rms=411 | updated_at=1778085460.214
- [2026-05-07 00:38:24] operator / voice_transcript_partial / voice: the recognition
  meta: kind=partial | timestamp=1778085504.9724555 | source=vosk | frequency_hz=296.4 | rms=365 | updated_at=1778085498.2134335
- [2026-05-07 00:38:25] operator / voice_transcript_partial / voice: the recognition on
  meta: kind=partial | timestamp=1778085505.4726403 | source=vosk | frequency_hz=296.4 | rms=365 | updated_at=1778085498.2134335
- [2026-05-07 00:38:25] operator / voice_transcript_partial / voice: the run face
  meta: kind=partial | timestamp=1778085505.7356358 | source=vosk | frequency_hz=296.4 | rms=365 | updated_at=1778085498.2134335
- [2026-05-07 00:38:25] operator / voice_transcript_partial / voice: the run face id
  meta: kind=partial | timestamp=1778085505.9719243 | source=vosk | frequency_hz=296.4 | rms=365 | updated_at=1778085498.2134335
- [2026-05-07 00:38:26] operator / voice_transcript_partial / voice: the run face
  meta: kind=partial | timestamp=1778085506.2401745 | source=vosk | frequency_hz=296.4 | rms=365 | updated_at=1778085498.2134335
- [2026-05-07 00:38:26] operator / voice_transcript_final / voice: the recognition face
  meta: kind=final | timestamp=1778085506.873207 | source=final | frequency_hz=296.4 | rms=365 | updated_at=1778085498.2134335
- [2026-05-07 00:38:39] operator / voice_transcript_final / voice: greeting
  meta: kind=final | timestamp=1778085519.589947 | source=final | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:39] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778085519.725766 | source=vosk | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:40] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1778085520.2217226 | source=vosk | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:41] operator / voice_transcript_final / voice: face
  meta: kind=final | timestamp=1778085521.1433747 | source=final | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:41] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778085521.2264276 | source=vosk | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:41] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778085521.479776 | source=vosk | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:41] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778085521.9966707 | source=vosk | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:38:42] operator / voice_transcript_final / voice: current status
  meta: kind=final | timestamp=1778085522.323585 | source=final | frequency_hz=380.0 | rms=371 | updated_at=1778085514.217153
- [2026-05-07 00:39:00] operator / voice_transcript_partial / voice: sound of output e to
  meta: kind=partial | timestamp=1778085540.740069 | source=vosk | frequency_hz=348.0 | rms=363 | updated_at=1778085539.9758434
- [2026-05-07 00:39:01] operator / voice_transcript_final / voice: sound of output e to
  meta: kind=final | timestamp=1778085541.1360912 | source=final | frequency_hz=348.0 | rms=363 | updated_at=1778085539.9758434
- [2026-05-07 00:39:02] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778085542.9867532 | source=vosk | frequency_hz=348.0 | rms=363 | updated_at=1778085539.9758434
- [2026-05-07 00:39:03] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778085543.2335637 | source=vosk | frequency_hz=348.0 | rms=363 | updated_at=1778085539.9758434
- [2026-05-07 00:39:04] operator / voice_transcript_final / voice: current status speech
  meta: kind=final | timestamp=1778085544.1493473 | source=final | frequency_hz=348.0 | rms=363 | updated_at=1778085539.9758434
- [2026-05-07 00:39:07] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1778085547.5041826 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:07] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778085547.7322226 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:08] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778085548.2328324 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:08] operator / voice_transcript_final / voice: acoustic guard
  meta: kind=final | timestamp=1778085548.8422012 | source=final | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:10] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1778085550.9829867 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:11] operator / voice_transcript_partial / voice: one hello
  meta: kind=partial | timestamp=1778085551.4856863 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:11] operator / voice_transcript_partial / voice: one disable the
  meta: kind=partial | timestamp=1778085551.733867 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:12] operator / voice_transcript_final / voice: one disable the
  meta: kind=final | timestamp=1778085552.9416685 | source=final | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:13] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778085553.0332272 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:13] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778085553.2343285 | source=vosk | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:14] operator / voice_transcript_final / voice: current status
  meta: kind=final | timestamp=1778085554.4233177 | source=final | frequency_hz=340.3 | rms=357 | updated_at=1778085545.2352626
- [2026-05-07 00:39:28] operator / voice_transcript_partial / voice: speech
  meta: kind=partial | timestamp=1778085568.0065162 | source=vosk | frequency_hz=296.8 | rms=366 | updated_at=1778085562.9901683
- [2026-05-07 00:39:28] operator / voice_transcript_partial / voice: speech lion
  meta: kind=partial | timestamp=1778085568.2527006 | source=vosk | frequency_hz=362.0 | rms=378 | updated_at=1778085568.2402961
- [2026-05-07 00:39:28] operator / voice_transcript_final / voice: speech
  meta: kind=final | timestamp=1778085568.598506 | source=final | frequency_hz=362.0 | rms=378 | updated_at=1778085568.2402961
- [2026-05-07 00:39:28] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778085568.9929967 | source=vosk | frequency_hz=362.0 | rms=378 | updated_at=1778085568.2402961
- [2026-05-07 00:39:30] operator / voice_transcript_final / voice: current status
  meta: kind=final | timestamp=1778085570.1266868 | source=final | frequency_hz=362.0 | rms=378 | updated_at=1778085568.2402961
- [2026-05-07 00:39:44] operator / voice_transcript_partial / voice: order
  meta: kind=partial | timestamp=1778085584.9954226 | source=vosk | frequency_hz=291.1 | rms=363 | updated_at=1778085579.23765
- [2026-05-07 00:39:45] operator / voice_transcript_partial / voice: order off face
  meta: kind=partial | timestamp=1778085585.7730682 | source=vosk | frequency_hz=291.1 | rms=363 | updated_at=1778085579.23765
- [2026-05-07 00:39:46] operator / voice_transcript_partial / voice: order off face current
  meta: kind=partial | timestamp=1778085586.7436619 | source=vosk | frequency_hz=321.8 | rms=359 | updated_at=1778085586.2389216
- [2026-05-07 00:39:46] operator / voice_transcript_partial / voice: order off face current status
  meta: kind=partial | timestamp=1778085586.99637 | source=vosk | frequency_hz=321.8 | rms=359 | updated_at=1778085586.2389216
- [2026-05-07 00:39:48] operator / voice_transcript_final / voice: order off face current status
  meta: kind=final | timestamp=1778085588.1980362 | source=final | frequency_hz=321.8 | rms=359 | updated_at=1778085586.2389216
- [2026-05-07 00:40:03] operator / voice_transcript_partial / voice: activate
  meta: kind=partial | timestamp=1778085603.519605 | source=vosk | frequency_hz=270.4 | rms=374 | updated_at=1778085597.758111
- [2026-05-07 00:40:04] operator / voice_transcript_partial / voice: activate current
  meta: kind=partial | timestamp=1778085604.2651446 | source=vosk | frequency_hz=260.0 | rms=353 | updated_at=1778085603.7624755
- [2026-05-07 00:40:04] operator / voice_transcript_partial / voice: activate current status
  meta: kind=partial | timestamp=1778085604.5150306 | source=vosk | frequency_hz=260.0 | rms=353 | updated_at=1778085603.7624755
- [2026-05-07 00:40:05] operator / voice_transcript_partial / voice: activate current status engaging scope
  meta: kind=partial | timestamp=1778085605.697197 | source=vosk | frequency_hz=260.0 | rms=353 | updated_at=1778085603.7624755
- [2026-05-07 00:40:06] operator / voice_transcript_final / voice: activate current status engaging
  meta: kind=final | timestamp=1778085606.452888 | source=final | frequency_hz=260.0 | rms=353 | updated_at=1778085603.7624755
- [2026-05-07 00:40:09] operator / voice_transcript_partial / voice: active
  meta: kind=partial | timestamp=1778085609.0332847 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:09] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778085609.523383 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:10] operator / voice_transcript_partial / voice: detection on
  meta: kind=partial | timestamp=1778085610.0200496 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:10] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778085610.278278 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:10] operator / voice_transcript_final / voice: detection
  meta: kind=final | timestamp=1778085610.6506536 | source=final | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:13] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778085613.3648593 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:13] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1778085613.531347 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:14] operator / voice_transcript_partial / voice: face hello
  meta: kind=partial | timestamp=1778085614.2723002 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:14] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778085614.5302005 | source=vosk | frequency_hz=359.9 | rms=360 | updated_at=1778085607.7585506
- [2026-05-07 00:40:15] operator / voice_transcript_partial / voice: current status guard
  meta: kind=partial | timestamp=1778085615.0200903 | source=vosk | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:15] operator / voice_transcript_partial / voice: current status guarding mode
  meta: kind=partial | timestamp=1778085615.2700965 | source=vosk | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:16] operator / voice_transcript_final / voice: face current status guard
  meta: kind=final | timestamp=1778085616.297427 | source=final | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:17] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778085617.6717932 | source=vosk | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:19] operator / voice_transcript_partial / voice: output
  meta: kind=partial | timestamp=1778085619.9158816 | source=vosk | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:20] operator / voice_transcript_partial / voice: acoustic voice cleanup
  meta: kind=partial | timestamp=1778085620.1631408 | source=vosk | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:20] operator / voice_transcript_partial / voice: output
  meta: kind=partial | timestamp=1778085620.4386332 | source=vosk | frequency_hz=272.0 | rms=380 | updated_at=1778085615.0100684
- [2026-05-07 00:40:20] operator / voice_transcript_final / voice: output
  meta: kind=final | timestamp=1778085620.8390975 | source=final | frequency_hz=416.0 | rms=370 | updated_at=1778085620.6566656
- [2026-05-07 00:40:21] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778085621.7333086 | source=vosk | frequency_hz=416.0 | rms=370 | updated_at=1778085620.6566656
- [2026-05-07 00:40:21] operator / voice_transcript_partial / voice: setting drafts
  meta: kind=partial | timestamp=1778085621.755746 | source=vosk | frequency_hz=416.0 | rms=370 | updated_at=1778085620.6566656
- [2026-05-07 00:40:29] operator / voice_transcript_partial / voice: to anything
  meta: kind=partial | timestamp=1778085629.6741054 | source=vosk | frequency_hz=256.0 | rms=368 | updated_at=1778085624.4034889
- [2026-05-07 00:40:31] operator / voice_transcript_partial / voice: is the current
  meta: kind=partial | timestamp=1778085631.4218543 | source=vosk | frequency_hz=256.0 | rms=368 | updated_at=1778085624.4034889
- [2026-05-07 00:40:32] operator / voice_transcript_partial / voice: is the current status
  meta: kind=partial | timestamp=1778085632.130844 | source=vosk | frequency_hz=256.0 | rms=368 | updated_at=1778085624.4034889
- [2026-05-07 00:40:32] operator / voice_transcript_partial / voice: is the current
  meta: kind=partial | timestamp=1778085632.1774046 | source=vosk | frequency_hz=256.0 | rms=368 | updated_at=1778085624.4034889
- [2026-05-07 00:40:32] operator / voice_transcript_final / voice: event the current
  meta: kind=final | timestamp=1778085632.647533 | source=final | frequency_hz=256.0 | rms=368 | updated_at=1778085624.4034889
- [2026-05-07 00:40:45] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778085645.194571 | source=vosk | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:40:45] operator / voice_transcript_partial / voice: the invert
  meta: kind=partial | timestamp=1778085645.6737175 | source=vosk | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:40:46] operator / voice_transcript_final / voice: theme
  meta: kind=final | timestamp=1778085646.0904195 | source=final | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:40:47] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778085647.171181 | source=vosk | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:40:47] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778085647.421674 | source=vosk | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:40:48] operator / voice_transcript_partial / voice: current status engaging scope
  meta: kind=partial | timestamp=1778085648.4225106 | source=vosk | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:40:49] operator / voice_transcript_final / voice: current status engaging
  meta: kind=final | timestamp=1778085649.444757 | source=final | frequency_hz=298.4 | rms=363 | updated_at=1778085640.688426
- [2026-05-07 00:41:03] operator / voice_transcript_partial / voice: disable the off
  meta: kind=partial | timestamp=1778085663.1951551 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:03] operator / voice_transcript_partial / voice: disable the known face
  meta: kind=partial | timestamp=1778085663.442524 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:04] operator / voice_transcript_partial / voice: disable the known face hello
  meta: kind=partial | timestamp=1778085664.1920273 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:04] operator / voice_transcript_partial / voice: disable the known face current status
  meta: kind=partial | timestamp=1778085664.4475427 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:04] operator / voice_transcript_partial / voice: disable the known face greeting
  meta: kind=partial | timestamp=1778085664.941942 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:05] operator / voice_transcript_partial / voice: disable the known face greeting gesture
  meta: kind=partial | timestamp=1778085665.2097797 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:05] operator / voice_transcript_partial / voice: disable the known face greeting
  meta: kind=partial | timestamp=1778085665.450811 | source=vosk | frequency_hz=280.0 | rms=365 | updated_at=1778085661.6900258
- [2026-05-07 00:41:05] operator / voice_transcript_final / voice: hey disable the face current greeting
  meta: kind=final | timestamp=1778085665.8595843 | source=final | frequency_hz=330.0 | rms=409 | updated_at=1778085665.6855023
- [2026-05-07 00:41:17] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778085677.44452 | source=vosk | frequency_hz=350.0 | rms=389 | updated_at=1778085672.443358
- [2026-05-07 00:41:17] operator / voice_transcript_partial / voice: face greeting
  meta: kind=partial | timestamp=1778085677.7132478 | source=vosk | frequency_hz=350.0 | rms=389 | updated_at=1778085672.443358
- [2026-05-07 00:41:17] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1778085677.9641652 | source=vosk | frequency_hz=350.0 | rms=389 | updated_at=1778085672.443358
- [2026-05-07 00:41:18] operator / voice_transcript_final / voice: the display
  meta: kind=final | timestamp=1778085678.3063002 | source=final | frequency_hz=350.0 | rms=389 | updated_at=1778085672.443358
- [2026-05-07 00:41:28] operator / voice_transcript_partial / voice: blink status
  meta: kind=partial | timestamp=1778085688.4575644 | source=vosk | frequency_hz=336.0 | rms=363 | updated_at=1778085687.4468098
- [2026-05-07 00:41:28] operator / voice_transcript_partial / voice: blink status of
  meta: kind=partial | timestamp=1778085688.9573352 | source=vosk | frequency_hz=336.0 | rms=363 | updated_at=1778085687.4468098
- [2026-05-07 00:41:29] operator / voice_transcript_partial / voice: blink status of face
  meta: kind=partial | timestamp=1778085689.2505126 | source=vosk | frequency_hz=336.0 | rms=363 | updated_at=1778085687.4468098
- [2026-05-07 00:41:29] operator / voice_transcript_partial / voice: blink status of face lion
  meta: kind=partial | timestamp=1778085689.720161 | source=vosk | frequency_hz=296.6 | rms=361 | updated_at=1778085689.70951
- [2026-05-07 00:41:30] operator / voice_transcript_partial / voice: blink status of face lion current
  meta: kind=partial | timestamp=1778085690.2045062 | source=vosk | frequency_hz=296.6 | rms=361 | updated_at=1778085689.70951
- [2026-05-07 00:41:30] operator / voice_transcript_partial / voice: blink status of face lion current status
  meta: kind=partial | timestamp=1778085690.455485 | source=vosk | frequency_hz=296.6 | rms=361 | updated_at=1778085689.70951
- [2026-05-07 00:41:31] operator / voice_transcript_partial / voice: blink status of face lion current status engaging scope
  meta: kind=partial | timestamp=1778085691.4546752 | source=vosk | frequency_hz=300.0 | rms=360 | updated_at=1778085691.446106
- [2026-05-07 00:41:32] operator / voice_transcript_partial / voice: blink status of face lion current status engaging acoustic
  meta: kind=partial | timestamp=1778085692.2227223 | source=vosk | frequency_hz=300.0 | rms=360 | updated_at=1778085691.446106
- [2026-05-07 00:41:32] operator / voice_transcript_partial / voice: blink status of face lion current status engaging acoustic the threat
  meta: kind=partial | timestamp=1778085692.7027404 | source=vosk | frequency_hz=300.0 | rms=360 | updated_at=1778085691.446106
- [2026-05-07 00:41:32] operator / voice_transcript_partial / voice: blink status of face lion current status engaging acoustic
  meta: kind=partial | timestamp=1778085692.9642687 | source=vosk | frequency_hz=300.0 | rms=360 | updated_at=1778085691.446106
- [2026-05-07 00:41:39] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778085699.2074537 | source=vosk | frequency_hz=264.4 | rms=372 | updated_at=1778085698.4571953
- [2026-05-07 00:41:39] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778085699.4958985 | source=vosk | frequency_hz=264.4 | rms=372 | updated_at=1778085698.4571953
- [2026-05-07 00:41:40] operator / voice_transcript_final / voice: acoustic guard
  meta: kind=final | timestamp=1778085700.0658307 | source=final | frequency_hz=302.5 | rms=369 | updated_at=1778085699.950089

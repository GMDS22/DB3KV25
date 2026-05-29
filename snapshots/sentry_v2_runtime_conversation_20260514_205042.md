# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-14 20:50:42
- Entries: 158
- Roles: {'assistant': 2, 'system': 102, 'operator': 54}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 102, 'voice_transcript_partial': 49, 'voice_transcript_final': 5}
- Channels: {'text': 2, 'voice': 156}
- Latest operator request: really
- Latest assistant message: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- Assistant text replies were generated without matching spoken assistant lines. Inspect human voice availability or auto-speak configuration.

## Timeline

- [2026-05-14 20:45:36] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-14 20:45:36] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-14 20:45:39] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778762739.3025098 | source=vosk
- [2026-05-14 20:45:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762740.1761196 | source=vosk | frequency_hz=250.0 | rms=1601 | updated_at=1778762740.1761196
- [2026-05-14 20:45:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762742.5975068 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762742.5975068 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762746.1830158 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762746.1830158 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:47] operator / voice_transcript_partial / voice: online now say the command run the
  meta: kind=partial | timestamp=1778762747.4630308 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:47] operator / voice_transcript_partial / voice: online now say the command run this march
  meta: kind=partial | timestamp=1778762747.711194 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:47] operator / voice_transcript_partial / voice: online now say the command run the smarts and
  meta: kind=partial | timestamp=1778762747.955993 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:48] operator / voice_transcript_partial / voice: online now say the command run the smarts and three
  meta: kind=partial | timestamp=1778762748.270771 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:49] operator / voice_transcript_final / voice: online now say the command run the smarts and three
  meta: kind=final | timestamp=1778762749.2135494 | source=final | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762749.5119298 | source=vosk | frequency_hz=263.3 | rms=1493 | updated_at=1778762740.4260776
- [2026-05-14 20:45:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762752.762094 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762768.01244 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762768.5125034 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762768.7624826 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:08] operator / voice_transcript_partial / voice: we
  meta: kind=partial | timestamp=1778762768.791031 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:09] operator / voice_transcript_partial / voice: we spoke
  meta: kind=partial | timestamp=1778762769.0265868 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762769.512622 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762771.262478 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:11] operator / voice_transcript_partial / voice: we saw
  meta: kind=partial | timestamp=1778762771.4105735 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762772.0139291 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762773.763138 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762774.5126362 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762775.0126672 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:15] operator / voice_transcript_partial / voice: we swore
  meta: kind=partial | timestamp=1778762775.039078 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762775.5132852 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762777.7630332 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:17] operator / voice_transcript_partial / voice: we swore whistle
  meta: kind=partial | timestamp=1778762777.8555195 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762778.5123599 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762786.7628295 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:26] operator / voice_transcript_partial / voice: we saw missy
  meta: kind=partial | timestamp=1778762786.8463886 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762787.5133004 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762791.2632515 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:31] operator / voice_transcript_partial / voice: we saw missy poorly
  meta: kind=partial | timestamp=1778762791.3471477 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:31] operator / voice_transcript_partial / voice: we saw missy poorly it
  meta: kind=partial | timestamp=1778762791.564548 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762792.0134926 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762792.263347 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:32] operator / voice_transcript_partial / voice: we swore western border illegally
  meta: kind=partial | timestamp=1778762792.3242512 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:32] operator / voice_transcript_partial / voice: we swore western border area
  meta: kind=partial | timestamp=1778762792.548435 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:32] operator / voice_transcript_partial / voice: we swore western border area under smart
  meta: kind=partial | timestamp=1778762792.8031616 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762793.2630422 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762806.7632658 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:46] operator / voice_transcript_partial / voice: we swore western border area under smarts and
  meta: kind=partial | timestamp=1778762806.78985 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762807.2636788 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762808.0130522 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:48] operator / voice_transcript_partial / voice: we swore western border area under smarts and julia
  meta: kind=partial | timestamp=1778762808.110801 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:48] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did
  meta: kind=partial | timestamp=1778762808.3728392 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:48] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you
  meta: kind=partial | timestamp=1778762808.5671535 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762809.0134964 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762811.2645164 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:51] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen
  meta: kind=partial | timestamp=1778762811.3331294 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762812.01395 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762816.7639682 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:56] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen why
  meta: kind=partial | timestamp=1778762816.8667734 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:57] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the
  meta: kind=partial | timestamp=1778762817.1159005 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:57] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always
  meta: kind=partial | timestamp=1778762817.3150866 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:57] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always tell us
  meta: kind=partial | timestamp=1778762817.8068876 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762818.513956 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762818.7637677 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:58] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice of
  meta: kind=partial | timestamp=1778762818.791378 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:59] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the
  meta: kind=partial | timestamp=1778762819.0431178 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:46:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762819.5134308 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:47:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762822.5135715 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:47:03] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the table
  meta: kind=partial | timestamp=1778762823.3338356 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:47:03] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the table block
  meta: kind=partial | timestamp=1778762823.4014418 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:47:03] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the table brooklyn or
  meta: kind=partial | timestamp=1778762823.465074 | source=vosk | frequency_hz=332.6 | rms=449 | updated_at=1778762750.762518
- [2026-05-14 20:47:03] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the table brooklyn
  meta: kind=partial | timestamp=1778762823.8706295 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:04] operator / voice_transcript_partial / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the table brooklyn are all
  meta: kind=partial | timestamp=1778762824.1216347 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:04] operator / voice_transcript_final / voice: we swore western border area under smarts and julian where did you listen what in the always still a slice the table brooklyn all
  meta: kind=final | timestamp=1778762824.917435 | source=final | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762825.0378327 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:06] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1778762826.8756964 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:07] operator / voice_transcript_partial / voice: it is
  meta: kind=partial | timestamp=1778762827.1237051 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:07] operator / voice_transcript_partial / voice: it is go
  meta: kind=partial | timestamp=1778762827.3558674 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:07] operator / voice_transcript_partial / voice: it is going to
  meta: kind=partial | timestamp=1778762827.6180754 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762828.83701 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762829.5845895 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:09] operator / voice_transcript_partial / voice: it is go to
  meta: kind=partial | timestamp=1778762829.8631237 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:10] operator / voice_transcript_partial / voice: it is going to really
  meta: kind=partial | timestamp=1778762830.3871186 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762830.8359544 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762831.085052 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:11] operator / voice_transcript_partial / voice: it is going to be really challenging
  meta: kind=partial | timestamp=1778762831.3983455 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:11] operator / voice_transcript_partial / voice: it is going to be really challenging to
  meta: kind=partial | timestamp=1778762831.8499496 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762832.3346615 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762832.8382287 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:12] operator / voice_transcript_partial / voice: it is going to be really challenging
  meta: kind=partial | timestamp=1778762832.901763 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762833.3349273 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762839.5851681 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:19] operator / voice_transcript_partial / voice: it is going to be really challenging did you do to
  meta: kind=partial | timestamp=1778762839.8582544 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:20] operator / voice_transcript_partial / voice: it is going to be really challenging digit lead
  meta: kind=partial | timestamp=1778762840.15329 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:20] operator / voice_transcript_partial / voice: it is going to be really challenging digital speedy
  meta: kind=partial | timestamp=1778762840.4081619 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:20] operator / voice_transcript_partial / voice: it is going to be really challenging digital speedy spacetime
  meta: kind=partial | timestamp=1778762840.6014163 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762841.0848603 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762843.585155 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:23] operator / voice_transcript_partial / voice: it is going to be really challenging digital speedy specific
  meta: kind=partial | timestamp=1778762843.5976558 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:24] operator / voice_transcript_partial / voice: it is going to be really challenging digital speedy specific spot
  meta: kind=partial | timestamp=1778762844.1173851 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:24] operator / voice_transcript_partial / voice: it is going to be really challenging digital speedy specific
  meta: kind=partial | timestamp=1778762844.636136 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762845.0865111 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762850.585035 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:30] operator / voice_transcript_partial / voice: it is going to be really challenging digital speedy specific sponsorships
  meta: kind=partial | timestamp=1778762850.6165679 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762851.0877156 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762854.8361654 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762855.3353126 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762856.335791 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762856.8351352 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762864.5850375 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762865.0859003 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762865.5855367 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:45] operator / voice_transcript_final / voice: it is going to be really challenging digital speedy specific sponsorships
  meta: kind=final | timestamp=1778762865.912315 | source=final | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762866.0325987 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:47:46] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778762866.5855677 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762888.3361282 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762889.3363347 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762908.8365111 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762909.3361468 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762912.585967 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762913.0864978 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762913.5859053 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762914.3366995 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762915.086445 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762915.586821 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762927.086722 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:48:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762927.5864224 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762949.087201 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762949.8371475 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762950.5866237 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762951.0870464 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762959.8383408 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762960.5872908 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762960.8371847 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762961.3375971 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762965.0869417 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762965.5868874 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762969.0871513 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762969.587477 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762973.8369887 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762974.3369555 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762974.5874083 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762975.087748 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762977.8373616 | source=vosk | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:38] operator / voice_transcript_final / voice: she
  meta: kind=final | timestamp=1778762978.877554 | source=final | frequency_hz=160.0 | rms=1602 | updated_at=1778762823.834854
- [2026-05-14 20:49:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762979.4207892 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762979.9204342 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762995.4207816 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:55] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1778762995.4551365 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762996.1709192 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762996.6711462 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:57] operator / voice_transcript_final / voice: really
  meta: kind=final | timestamp=1778762997.1458025 | source=final | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762998.671062 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778762999.4286773 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:49:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778762999.9292796 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:50:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778763000.4287589 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:50:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778763010.1794512 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:50:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778763010.679141 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:50:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778763019.4291277 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892
- [2026-05-14 20:50:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778763019.929252 | source=vosk | frequency_hz=218.0 | rms=1604 | updated_at=1778762979.4207892

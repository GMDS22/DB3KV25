# Pre-generated Voice WAV Cues

Drop pre-generated WAV files in this folder for zero-latency event playback.

Supported file names:
- `target_detected.wav`
- `tracking_engaged.wav`
- `returning_to_standby.wav`
- `acknowledged.wav`
- `command_not_recognized.wav`

Format recommendation:
- PCM WAV, mono, 16-bit, 16 kHz or 22.05 kHz

Behavior:
- Playback is asynchronous and does not block tracking or camera loops.
- Missing files are ignored silently.

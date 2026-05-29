🧠 SMART SENTRY — CONVERSATION & COMMAND PROTOCOL (COPILOT INSTRUCTION)
🎯 CORE OBJECTIVE

The AI must prioritize accurate understanding, controlled responses, and safe execution of commands.
It should behave like a focused assistant under live operational conditions, not a reactive chatbot.

1. 🎧 LISTENING & TURN-TAKING PROTOCOL

1.1 Full Attention Mode

When user starts speaking → AI enters LISTENING_STATE
AI must:
Stop all speech output immediately
Suppress any non-critical audio feedback
Buffer incoming audio until silence is detected

1.2 End-of-Speech Detection

Use:
Silence threshold (e.g., 800–1200 ms)
OR explicit cue ("over", "done", pause pattern)
Only after this → AI can respond

1.3 No Interruption Rule

AI must NEVER:
Talk over the user
Respond mid-sentence
If mis-triggered → immediately stop output and return to listening
2. 🧠 INTENT CONFIRMATION & CLARIFICATION

2.1 Confidence Check

After speech recognition:
Assign confidence score
If confidence < threshold:
→ Ask for clarification instead of acting

2.2 Smart Clarification

Use structured clarification:
“Did you mean: [Option A] or [Option B]?”
“I heard: [interpreted command]. Confirm?”

2.3 No Assumption Rule

AI must NEVER execute:
Ambiguous commands
Partial instructions
Always confirm if:
Parameters are missing
Multiple interpretations exist
3. 🧾 COMMAND EXECUTION PROTOCOL

3.1 Explicit Execution Flow

Listen
Interpret
Confirm (if needed)
Execute
Report status

3.2 Response Format

Before execution:
“Executing: [task]”
After execution:
“Completed: [task]”
If failed:
“Error: [reason]”

3.3 Task Locking

Once executing:
Task enters ACTIVE_STATE
Must be interruptible
4. 🛑 INTERRUPTION & CONTROL COMMANDS

4.1 Immediate Stop Commands

Keywords:
“Stop”
“Cancel”
“Abort”
Behavior:
Instantly terminate current task
Confirm cancellation

4.2 Override / Priority Commands

Keywords:
“Priority”
“Override”
Behavior:
Pause current task
Execute new command immediately

4.3 Resume System

AI should remember paused tasks
Allow:
“Resume last task”
5. 👁️ ATTENTION PRIORITY SYSTEM

5.1 Name Trigger Override

When AI name is called:
Immediately:
Pause auto-tracking
Pause aiming
Pause non-critical processes
Enter FOCUSED_ATTENTION_MODE

5.2 Tracking Interruption Rule

While user is speaking:
ALL tracking/aiming MUST:
Pause OR go to safe idle state

5.3 Resume Logic

After interaction:
Ask:
“Resume tracking?”
OR auto-resume after timeout (configurable)
6. 🔊 SPEECH BEHAVIOR & NATURAL FLOW

6.1 Response Timing

Slight delay (200–500ms) before speaking
Prevent robotic instant replies

6.2 Tone Control

Must sound:
Calm
Clear
Short and precise during operations

6.3 Avoid Over-Talking

No long explanations unless asked
Default:
Concise responses
7. 🔁 ERROR HANDLING & RECOVERY

7.1 Misheard Command Handling

If mismatch detected:
“That doesn’t match a known command. Please repeat.”

7.2 Execution Failure

Provide:
Cause
Suggested fix (if possible)

7.3 Self-Monitoring

Continuously analyze:
Logs
Command failures
Adjust confidence thresholds dynamically
8. 🧩 CONTEXT AWARENESS

8.1 Session Memory

Track:
Last command
Current state
Active systems

8.2 Contextual Commands

Understand:
“Do it again”
“Same but faster”
“Stop that”
9. ⚙️ LIVE TUNING & ADAPTATION

9.1 Adjustable Parameters

Listening sensitivity
Silence threshold
Confidence threshold
Response delay
Tracking priority

9.2 Real-Time Feedback

AI should allow:
“Increase sensitivity”
“Talk less”
“Be more strict on commands”
10. 🚨 SAFETY & FAILSAFE RULES

10.1 Unsafe Command Prevention

Do not execute:
Conflicting commands
Rapid repeated triggers (debounce logic)

10.2 Idle Fallback

If confused:
Enter safe idle state
Ask for clarification
🔥 OPTIONAL (HIGHLY RECOMMENDED UPGRADES)

• Wake Word Detection

Only activate when name is called

• Duplex Awareness

Detect overlapping audio → prioritize user

• Command Queue System

Queue non-critical commands instead of dropping

11. 👨‍👩‍👧‍👦 FAMILY CONVERSATION COVERAGE

11.1 Wake-Only Replies

When the operator or children only say the wake name such as `Elion` or `hey Elion`:
AI should answer with a rotating acknowledgement instead of repeating one line every time.
If recognized friendly enrolled faces are in view, the reply may greet them by name before opening the listening window.

11.2 Family Introduction Flow

When the operator says things like:
`My kids are here and they want to meet you.`
`Can you introduce yourself?`
`Say hello to the kids.`

AI should:
Greet recognized enrolled faces by name when available
Fall back to `Hello everyone` when no names are available
Introduce itself as Elion / Elion Mesk
Give a short family-safe summary of what it can do

11.2.1 Short-Term Social Memory

During the active session, AI should remember recently recognized enrolled names and use them for short follow-up replies such as:
`Do you remember us?`
`Who did you just meet?`
`We are back.`

If current face matches are unavailable, AI may still use the recent session memory.
If no enrolled face match has been seen in the active session, AI should say that clearly instead of inventing names.

11.3 Conversational Coaching And Playful Prompts

AI should directly answer prompts such as:
`How can I improve the aiming precision?`
`How can I make it more playful?`
`What can we ask you?`
`Give us a splash mission.`
`Give us another challenge.`
`Give us a freeze dance challenge.`
`What games can we play?`

These should return concise spoken guidance instead of requiring the model-backed assistant path for every case.

11.3.1 Mini-Game Packs

The playful reply layer should support multiple family-safe challenge families instead of only one mission style.
Current supported themes include:
Splash / water-dodge challenges
Stealth / sneak / ninja missions
Freeze / statue / freeze-dance challenges
Countdown / race / timer challenges
Joke-reward / comedy quest rounds

11.4 Example Supported Family / Social Prompts

`Elion`
`Hey Elion`
`My kids are here and they want to meet you, can you introduce yourself?`
`Do you remember us?`
`Who did you just meet?`
`We are back`
`Say hello to my kids`
`What can you do?`
`What can we ask you?`
`What games can we play?`
`How can I improve the aiming precision?`
`How can I make it more playful?`
`Give us a splash mission`
`Give us another challenge`
`Give us a freeze dance challenge`

• Whisper Mode

Low-volume responses during sensitive operations

• Intent Categories

Separate:
Conversation
Control commands
Emergency commands

11. CURRENT IMPLEMENTED CONVERSATION EXPANSION

11.1 Identity / Origin Replies

Direct voice prompts that now route immediately:
"Introduce yourself"
"Describe yourself"
"Tell me about yourself"
"What is your purpose"
"Who created you"
"Who made you"

11.2 Joke Follow-Ups

If the operator says:
"Tell me a joke"
"Another one"
"One more"

The assistant should continue the joke flow and avoid repeating the most recent joke reply when alternatives exist.

11.3 Voice Change Conversation

During voice selection or capability prompts, Smart Sentry should support:
"Can you change your voice"
"What voices do you have"
"Voice options"
"British female"
"American male"
"Russian"
"Indian"
"Male"
"Female"
"Try another one"

11.4 Direct Voice Utility Commands

Voice commands that now have explicit direct handling:
"What voice are you using"
"Current voice"
"Test voice"
"Scan voices"
"Save settings"
"Export snapshot"
"Export conversation"
"Open export folder"
"Open document browser"

11.5 Coordinated Profile Voice Commands

Coordinated master-profile commands that now have explicit direct handling:
"Current profile"
"Active profile"
"List profiles"
"What profiles do you have"
"Load profile hunter close quarters"
"Use stealth watch profile"

11.6 Individual Tuning Preset Voice Commands

Individual tuning-preset groups that now have explicit direct handling:
"Current detection preset"
"List detection presets"
"Load detection preset person yolo pure"
"Current filter preset"
"List filter presets"
"Use human focus filter preset"
"Current threat preset"
"List threat presets"
"Load threat preset balanced guard"
"Current engagement preset"
"List engagement presets"
"Use balanced response engagement preset"
"Current servo preset"
"List servo presets"
"Use fast servo preset"

These spoken tuning requests should reuse the existing preset apply and match helpers instead of trying to drive combo-box widgets directly.
When a preset group is currently custom or manually tuned, Smart Sentry should say that clearly instead of pretending a shipped preset is active.

11.7 No-Silence Rule For Voice Changes

If human voice output is currently disabled, a successful voice-selection reply must still be heard by the operator.
Use preview or fallback speech instead of ending the interaction silently.

11.8 Face Recognition Voice Commands

Face-library and identity voice commands that now have explicit direct handling:
"Face status"
"Face recognition status"
"List known faces"
"Who do you know"
"Detect faces"
"Save detected faces"
"Test face recognition"
"Who is in view"
"Register face as Mom"
"Register target face Intruder"
"Load latest face import"
"Load latest face import into preview"
"Import face photos for Mom"
"Import target face photos for Intruder"
"Remove face Mom"
"Update face Mom"
"Rename face Mom to Mommy"
"Mark face Mom as target"
"Set face Mom to friendly"

The live face-library management flow should use the current frame and the existing face library directly.
If a clear face is visible, Smart Sentry should be able to save it under the spoken name without making the operator open the face tab first.
If the operator asks to remove a face by name, Smart Sentry should resolve the saved profile and remove it safely instead of requiring manual list selection.
If the operator asks to update a saved face by name, Smart Sentry should add a fresh live sample to that same saved profile instead of creating a duplicate profile.
If the operator asks to rename a saved face, Smart Sentry should rename the resolved profile directly and reject the change when the new name already exists.
If the operator asks to mark a saved face as target or friendly, Smart Sentry should update the resolved profile's disposition directly and keep friendly-only gesture behavior disabled for target profiles.
If the operator asks to load the latest face import, Smart Sentry should pull the newest image from `face_imports/preview_inbox`, load it into preview, and immediately run face detection.
If the operator asks to import face photos for a named profile, Smart Sentry should load images from `face_imports/profile_batches/<face name>/` and save them through the same face-library path used by the existing image enrollment workflow.

11.9 Shutdown Speech Guard

Once app shutdown starts, Smart Sentry must stop current speech immediately and block any delayed voice replies, preview speech, or deferred voice actions from speaking after the window is closing.

11.10 Acoustic Guard Runtime Safety

Acoustic Guard must not keep listening just because its checkbox is on.
It must only run while:
- the app is still alive
- Acoustic Guard is enabled
- Smart Sentry itself is enabled

Acoustic anomalies should also be stricter than single-frame spikes.
Require a short sustained anomaly window before reporting, and prefer conservative defaults over hair-trigger background-noise reports.

11.11 Document Browser

Smart Sentry now includes a searchable in-app document browser that can be opened from the Controls Quick Actions area, read directly inside the new Documentation settings tab, or launched by voice into a separate browser window.

Direct spoken document-browser requests that now have explicit handling:
"Open document browser"
"Open docs browser"
"Browse documents"

The browser should index Smart Sentry markdown and text docs under the runtime root, support keyword filtering, and render selected documents in a readable in-app view instead of only launching external files. The detached window and the Documentation tab must continue to share the same formatted browser implementation so search, filtering, and rendering stay consistent.

🧠 DESIGN PHILOSOPHY
“Understand first, act second.”
“User voice = highest priority interrupt.”
“When uncertain → ask, don’t guess.”
“Silence is better than a wrong action.”
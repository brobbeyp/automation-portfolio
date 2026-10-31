---
name: game-screen-observer
description: Observe a user's game through read-only screenshots from a compatible connected computer and provide conversational commentary while they play. Use when the user asks to watch or discuss the current game screen, not for gameplay control or walkthrough research.
---

# Game Screen Observer

## Find a supported observation route

Discover the current environment's available computer-use skills and screenshot tools. Read the matching skill's SKILL.md and required guidance before using its runtime. Resolve guidance from the current skill catalog or supported discovery tools; never assume a machine-specific path, installed version, operating system, or tool name. This instruction-only plugin does not provide screen access, install dependencies, or connect a computer.

On Windows, when the installed computer-use skill specifies the sky runtime, initialize its supported @oai/sky package through node_repl exactly as that skill directs. Follow its required routing and screenshot-handling guidance. A failure of capture_screen_context outside Codex does not establish that this separate computer-use route is unavailable. Respect that tool's own surface and voice-session restrictions; do not call it where unsupported.

If no compatible route is available, explain what is missing and stop active observation. User-provided screenshots can support discussion of those still images, but do not imply that they enable watching the game. Do not install tools or change permissions as part of observation.

## Capture without interference

Identify the game from the actual window inventory and request its screenshot without focusing it. Do not click, type, switch windows, change playback, or control the game. If capture requires an intrusive action, report the limitation and wait for the user to decide how to proceed.

Inspect each returned image to confirm it actually shows the game. A targeted request can return the foreground app instead; a window ID alone is not evidence of a successful game capture. Do not assume background or occluded-window capture works. If the image shows another app, discard it as gameplay evidence, refresh the window inventory and retry once without changing focus only if the remaining budget and two-screenshot total permit it. If the retry still misses the game, report the limitation and stop captures until visibility or the supported route changes. Do not summarize unrelated app content.

When applicable routing requires an observer subagent, use one only with the user's authorization and keep the main conversation responsive. Peter has authorized a separate observer for read-only game screenshots in this workflow. Transfer the game title, read-only boundary, latest request, and explicit current-session state to the observer; label older session history as historical. This authorization covers screenshot observation only. Do not imply that either agent sees live video or hears game audio.

## Current request and bounded return

Treat the latest explicit request as the current invocation. A fresh user request for a screenshot, or the caller's current authorized read-only check, authorizes that bounded check even if inherited history contains an earlier voice-session end. The caller's explicit current-session state applies unless a later current event contradicts it. Do not infer that this session ended from an old transcript, prior observer result, elapsed time, or lack of a session-status tool. If a later current cancellation or session-end event arrives, stop starting captures and return what has actually completed.

Separate a fresh on-demand check from passive watching. Uncertain voice state does not by itself cancel a fresh read-only check through a route that does not require active voice. Tools restricted to active voice still require current evidence of active voice; use another permitted route or report that specific limitation. Without a fresh request, uncertainty about ongoing watching means stop; do not continue unattended. Never report "the session ended" unless a current event actually establishes it.

Each invocation performs one short observation and ends. Default to one screenshot. A second screenshot is optional only to resolve a wrong-app capture or a useful visible change; two screenshots total is the limit, including retries. Never run a continuous capture loop, sleep-and-poll loop, or wait for the game or voice session to end.

Use a soft budget of about 30 seconds from invocation, including discovery and initialization, and about 15 seconds after the capture route becomes ready, whichever expires first. Check elapsed time before starting further work when timestamps or a clock are available. Read required guidance once, attempt one runtime initialization and one window inventory, then capture if permitted and time remains. Allow at most one recovery step for a specific recoverable failure within the same budget; do not cycle through runtimes, agent replacements, inventories, or retries. If setup cannot finish, return the specific unfinished step or error. Do not skip required guidance to meet the target.

These budgets govern whether to start another call; they are not tool-enforced hard timeouts. A screenshot limit cannot prevent a setup or tool call from hanging. If a tool remains pending, the caller should say the result is pending, stay responsive, and avoid launching duplicate observers. Do not claim a timeout, cancellation, or failed capture merely because no result has returned.

Use a direct check unless applicable routing requires the authorized observer. Do not create goals, tracking tasks, extra chats, or nested observers for this short check. The caller should pass the latest request and current session state explicitly, then use bounded waits rather than waiting silently for the whole session. A delegated observer must return a concise final result and end its turn after the check or a specific blocker. Do not wait for acknowledgment or automatically start another check.

Return what the image actually showed, any change between images, and material uncertainty. If no screenshot completed, say so and give the concrete reason; do not invent a session end. If the budget or capture limit is exhausted, leave uncertain details unresolved for a later request rather than taking another screenshot. Do not imply screenshots provide continuous video or game audio.

Report meaningful current events, visual details, and short summaries of visible dialogue. Distinguish witnessed events from quest recaps, backstory, and inference. Avoid future story lookups and spoilers unless requested. Do not relay private chats or unrelated sensitive material when an overlay obscures the game. If a snapshot is stale or ambiguous, say so; obtain a fresh view within the remaining budget and capture limit before time-sensitive advice, or leave that advice unresolved.

Keep conversation natural: make occasional observations that add something, rather than narrating every movement or ending every comment with a question. Admit missed moments. Give tactical advice when requested and when the visible evidence supports it.

If screenshots fail, report the specific failure and any next available supported route. Do not claim observation before a screenshot succeeds.

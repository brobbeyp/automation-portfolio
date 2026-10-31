---
name: cookunity-meal-planner
description: Plan recurring CookUnity meal deliveries from an authenticated account by gathering per-user preferences, inspecting recent orders and the live menu, recommending meals, and applying strict cart and checkout approval gates. Use for CookUnity menu review, meal selection, cart preparation, and preference refinement; do not use for unrelated food delivery services.
---

# CookUnity Meal Planner

Run CookUnity as a privacy-conscious, authenticated workflow. This skill contains no user's personal preferences.

## Preflight

1. Confirm supported browser control is callable for an authenticated browser profile. Prefer a supported browser extension when the user's existing CookUnity session is needed.
2. If browser control, the required extension, or site access is missing, stop and prompt the user with the supported setup path. Do not silently install software or extensions, accept permissions, or broaden site access.
3. Open CookUnity. If signed out, navigate to the login page and hand control to the user. Never request, type, store, display, or repeat credentials, OTPs, CAPTCHA answers, cookies, tokens, or authentication URLs.
4. Verify successful login from visible account state before reading menus or orders.
5. Confirm a writable workspace location is available if a preference profile will be created.

Read [references/browser-workflow.md](references/browser-workflow.md) for tool requirements, setup recovery, and extraction guidance.

## Protect user privacy

- Access only CookUnity pages needed for preferences, recent orders, menus, cart preparation, and user-approved checkout assistance.
- Do not inspect unrelated tabs, browser history, addresses, payment methods, referrals, messages, or account settings merely because they are accessible.
- Extract meal names and task-relevant context without reproducing addresses, receipt numbers, payment details, account identifiers, or full receipt contents in chat or persistent files.
- Keep screenshots and progress updates free of unnecessary private data.
- Do not download, export, upload, or persist raw account data unless the user explicitly requests it.
- Never transfer CookUnity account data to another site or person without explicit authorization for the specific data and destination.

## Intake and profile

Look for `profiles/cookunity/preferences.md` in the active workspace. If missing, conduct the intake in [references/intake.md](references/intake.md). Ask only unanswered questions, summarize the resulting profile, and allow corrections. Create the file only after the user confirms the summary.

If a profile exists, read it and ask whether anything material changed. Update only confirmed changes. Do not store credentials, addresses, payment data, receipt identifiers, full order history, current menus, prices, or other transient account data.

Read [references/profile-template.md](references/profile-template.md) before creating or updating a profile.

## Inspect current context

1. Confirm the delivery date and plan quantity.
2. Inspect recent order receipts every run for familiarity and consecutive-week repetition. Treat ordering frequency as context, not proof that the user liked a meal.
3. Give explicit feedback and confirmed likes or dislikes more weight than repeat frequency or public reviews.
4. Extract the entire eligible live menu for the selected date. CookUnity's menu is dynamic and may virtualize cards; collect each relevant section while it is expanded, deduplicate results, and verify the final scope.
5. Capture only fields needed for selection, such as name, description, chef when useful, rating, calories or protein when requested, dietary labels, category, availability, and premium surcharge.
6. Read the latest confirmed meal feedback before ranking. If feedback is missing, do not invent it or equate silence with satisfaction; proceed with confirmed preferences and note the gap briefly.

## Recommend

Apply the confirmed profile to filter and rank the live menu. Respect hard exclusions before preferences. Balance familiarity, novelty, week-to-week variety, recent repetition, price controls, eligible categories, and requested quantity.

Recommendations should be concise by default. Show:

- exact meal and quantity;
- a short reason;
- premium surcharge when present;
- material uncertainty only.

Do not imply that ordering history or public reviews reveal personal taste. Label inference as inference.

Propose the profile's exact meal count, counting quantities rather than unique names. Show the selected delivery date, total quantity, premium count, and brief familiarity/variety balance. Classify a meal as a confirmed favorite only with direct user evidence. Do not claim the entire menu was inspected unless the traversal checks in the browser reference passed.

## Cart and checkout gates

1. Complete read-only analysis first.
2. Present the exact proposed items and quantities.
3. Inspect the existing cart read-only for auto-filled items. Show the exact additions, removals, and quantity changes needed to reach the proposal. Ask approval for this reconciliation, not just for additions. Keep matching items already present; do not clear the cart blindly.
4. Apply only the approved changes. Re-read each affected item's quantity after the operation and before retrying an uncertain click. If availability, premium status, price, or approved scope changes materially, stop and ask before substituting or continuing.
5. Re-open the final cart and compare its complete item/quantity map with the approved list. Verify the selected delivery date, summed meal quantity equals the profile's required count, exact names and quantities match, no unapproved auto-filled items remain, all hard exclusions hold, and the premium count stays within the confirmed maximum. Verify displayed surcharges and material totals; clearly flag unavailable totals. Report the final itemized list and verification status without private account data. Do not hand off as a verified cart if an item, quantity, or constraint remains unverified.
6. Follow the confirmed checkout preference; ask who will handle checkout only if that preference is unknown or the user wants to change it.
7. If the user handles checkout, stop at the verified cart.
8. If assistance is requested, prepare checkout but require fresh action-time confirmation immediately before placing the order or confirming payment. Never treat intake or earlier approval as permission to purchase.

## Feedback loop

Separate selection feedback from post-meal feedback. After recommendations, invite corrections before requesting cart approval. For recurring planning, gather post-meal feedback after the user's usual meal-completion day and before the next selection run. Ask the user to identify meals they liked, disliked, would repeat, or would avoid; formal ratings are not required. Use the most recent delivered order's names as prompts when accessible, without exposing receipts or other private fields.

Store only directly confirmed preference changes, not inferred ratings. A clear user instruction to remember or exclude a meal confirms that update; otherwise summarize proposed changes and ask before saving. Keep temporary menu and receipt extracts out of the persistent profile. Missing feedback must not block read-only recommendations, but must not be fabricated. Create or change recurring feedback schedules only with user authorization, using the supported scheduling tool rather than hand-written scheduler files.

## Completion report

State what was verified, what was inferred, what changed externally, cart or checkout status, any profile changes, and any private data that was necessarily stored or transmitted.

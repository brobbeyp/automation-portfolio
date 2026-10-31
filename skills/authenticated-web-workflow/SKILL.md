---
name: authenticated-web-workflow
description: Run repeatable, authenticated, multi-step website workflows that require prerequisite checks, user login, preference intake, approval gates, result verification, and feedback-driven adjustment. Use for recurring work on signed-in websites; do not use for simple public-page lookups or one-off browsing.
---

# Authenticated Web Workflow

Use a shared lifecycle while keeping each website's rules and each user's preferences separate.

## Protect privacy by default

Use data minimization throughout the workflow:

- Access only the pages, records, history, files, and account fields needed for the current outcome.
- Do not inspect browser history, unrelated tabs, unrelated account areas, contacts, messages, or stored files merely because they are accessible.
- Avoid reproducing private data in chat, logs, screenshots, filenames, profiles, or deliverables. Summarize or redact addresses, receipt numbers, account identifiers, payment details, authentication parameters, and other sensitive fields unless the user specifically needs them.
- Never expose passwords, OTPs, recovery codes, session tokens, cookies, authorization URLs, or security answers. Hand authentication to the user.
- Do not transfer data from one site, account, file, or person to another without explicit authorization for the specific data and destination.
- Prefer the least-permissive site access that can complete the task. Do not request all-sites access, browsing history, uploads, or broad account permissions unless the workflow demonstrably requires them.
- Keep persistent profiles minimal. Store only confirmed preferences needed for future runs, not raw page captures, complete histories, addresses, payment information, credentials, or transient account data.
- Avoid retaining temporary extracts after they stop being useful. Do not create downloadable files containing private account data unless the user requests them.

When showing proof of work, choose a view that verifies the result while revealing the minimum necessary personal information. If private data cannot be avoided, warn the user before displaying or transmitting it.

## Start with a preflight

1. Define the requested outcome and distinguish read-only inspection from actions that change external state.
2. Identify the required browser, extension, plugin, connector, files, account access, and site permissions.
3. Verify that required capabilities are actually callable. An installed-looking integration or mentioned tab is not proof of usable access.
4. If something is missing, stop the affected work and give the user the shortest supported setup path. Do not silently install software, extensions, or grant permissions.
5. Navigate to the site's login page when needed, then hand control to the user for passwords, OTPs, CAPTCHAs, and other authentication secrets. Verify login before continuing.

Read [references/preflight.md](references/preflight.md) when setup, installation, authentication, or tool availability needs handling.

## Gather and confirm preferences

Look for a site-specific user profile outside this installed skill. If none exists, ask only the intake questions needed for the current workflow. Separate:

- hard restrictions and non-negotiable limits;
- preferences and ranking criteria;
- acceptable inferences;
- authorization boundaries;
- desired output detail;
- actions requiring confirmation.

Summarize the answers and allow corrections before creating a profile. Never ship or bake one user's preferences into this reusable skill. Create or update a profile only after the user confirms its contents. On later runs, read the profile and ask whether anything material changed instead of repeating the full intake.

Read [references/profiles.md](references/profiles.md) before creating or updating a preference profile.

## Inspect live context

Use the authenticated site as the source of truth for current availability, account state, history, costs, and constraints. Prefer structured page data or rendered DOM extraction over repetitive manual clicking when the site is dynamic. Treat historical behavior as context, not proof of preference. Give explicit user feedback more weight than frequency, public ratings, or model inference.

Collect only the fields needed for the decision. Extract summaries or task-relevant records instead of copying complete account pages. Keep sensitive values out of tool output when they are not necessary for reasoning or verification.

Verify collection completeness for the task's scope. Dynamic pages may require scrolling, expanded sections, pagination, or load-more controls; one visible result set is not necessarily the full dataset. Compare observed counts where available and disclose incomplete coverage rather than declaring an item absent after a partial search.

Keep site-specific selectors, terminology, intake extensions, and interpretation rules in a site adapter outside the general instructions. Read [references/site-adapters.md](references/site-adapters.md) when creating or using an adapter.

## Prepare, approve, execute, verify

1. Do read-only collection and analysis first.
2. Present a concise proposed result, including material costs, uncertainty, and consequences.
3. Ask for approval immediately before any consequential external action. Identify the exact items, data, destination, quantities, or changes involved.
4. Perform only the approved actions. Do not treat intake preferences as standing authorization for later mutations.
5. Require fresh action-time confirmation for purchases, checkout, submissions, deletion, permission changes, messages, uploads, or other high-impact final actions.
6. Verify the resulting website state. Do not equate an attempted click or request with success.

When the site has pre-existing or auto-generated selections, compare them with the approved target and obtain approval for the necessary removals as well as additions. Preserve matching selections. Inspect state before retrying an uncertain mutation to avoid duplicate actions. Before handoff, verify the complete final result against the approved target, including quantities, constraints, extra or missing items, and material costs. Report remaining uncertainty instead of labeling a partial check complete.

If the user declines, changes scope, or interrupts browser control, stop the affected action and preserve the current state when practical.

## Learn from feedback

After presenting or executing the result, ask for relevant feedback when it will improve the recurring workflow. Distinguish direct feedback from inference. Propose profile changes and update them only after confirmation. Keep transient site data, menus, prices, and availability out of persistent preference profiles.

For recurring tasks, distinguish immediate review from feedback after the user has experienced the result. Agree on a useful feedback window before the next planning run; schedule it only when authorized. Ask concise outcome-specific questions rather than requiring formal ratings. Carry forward confirmed feedback, and never infer satisfaction from silence or completion history.

## Completion standard

Report:

- what was verified;
- what was inferred;
- what changed externally;
- what remains unverified or needs user action;
- whether any profile was created or updated;
- any private data that was necessarily stored or transmitted.

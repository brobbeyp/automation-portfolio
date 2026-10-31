# Per-user preference profiles

Store confirmed user preferences outside the installed skill package. Prefer a site-specific path in the active workspace, such as:

```text
profiles/<site-name>/preferences.md
```

Do not create a profile until the user confirms the intake summary. Do not overwrite an existing profile without confirming material changes.

Apply data minimization. A preference profile is not an account archive. Do not include passwords, authentication secrets, payment details, full addresses, receipt or order identifiers, browsing history, raw page extracts, medical or legal records, or unrelated personal details. If a sensitive preference is genuinely necessary, explain why and ask whether the user wants it persisted; otherwise use it only for the current session.

Keep profiles local to the intended workspace or user-selected location. Do not upload, share, or copy a profile to another service or account without explicit authorization for that destination.

## Suggested fields

```markdown
# <Site> workflow preferences

## Goal and frequency
- Primary outcome:
- Typical cadence:

## Hard restrictions
- Absolute exclusions:
- Legal, financial, health, or account limits:

## Preferences
- Preferred options:
- Options to limit:
- Variety or repetition rules:
- Familiar versus exploratory balance:

## Cost controls
- Budget:
- Allowed surcharges or premium options:

## Scope
- Eligible categories:
- Excluded categories:

## Authorization boundaries
- Read-only access allowed:
- Actions requiring exact-item confirmation:
- Final actions the user will perform personally:

## Output
- Desired explanation length:
- Required comparison fields:

## Confirmed feedback
- Confirmed likes:
- Confirmed dislikes:
- Other direct feedback:
```

Keep dynamic availability, prices, current menus, account balances, order contents, and other transient facts out of the profile. Read those live each run.

When updating a profile, write the smallest confirmed change and preserve unrelated fields. Summaries should avoid exposing private profile contents unless the user asks to review them.

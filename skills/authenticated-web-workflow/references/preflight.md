# Preflight and authentication

Use this checklist before operating an authenticated website.

## Capability check

- Identify the supported browser or site connector required by the workflow.
- Confirm the capability is callable and can see the intended tab or account surface.
- Confirm the site is not blocked by browser or workspace policy.
- Confirm a writable location exists if the workflow uses a persistent profile.
- Identify optional helpers separately from required dependencies.
- Request only the narrowest site, account, file, and browser permissions needed for the task.

If a required tool is unavailable, explain exactly what is missing and how the user can enable or install it. Do not invent dependency metadata for tools the skill system cannot declare.

## Authentication boundary

Navigate to the correct login page and ask the user to take over. Do not request, read, type, store, or repeat passwords, OTPs, recovery codes, or CAPTCHA answers. After the user returns control, verify login using visible account or page state without exposing unnecessary personal information.

Do not include authentication callback URLs, session parameters, account addresses, or other incidental private values in progress updates or final responses.

## Installation boundary

Do not silently install browsers, extensions, plugins, or software; accept broad permissions; bypass security interstitials; or weaken security settings. Prompt the user with the exact required component and supported setup path.

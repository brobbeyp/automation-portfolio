# Browser tools and CookUnity extraction

## Required capabilities

- ChatGPT or Codex desktop environment with browser control.
- A supported browser extension when the user's existing signed-in profile is required.
- An authenticated CookUnity session, completed by the user.
- Rendered-page or DOM inspection and browser interaction.
- Local file read/write access for an optional confirmed preference profile.

If a required capability is unavailable, prompt for its supported setup. Do not invent unsupported skill dependency metadata or silently install a browser or extension.

## Login

Open CookUnity and navigate to its login page. Hand control to the user for credentials, OTPs, CAPTCHAs, or identity-provider selection. Verify login without exposing callback URLs, tokens, addresses, or other incidental private values.

## Recent orders

- Use CookUnity's Orders area and read recent receipt panels.
- Collect only delivery date and meal names or quantities needed for comparison.
- Do not reproduce delivery addresses, receipt numbers, payment data, discounts, or complete financial records.
- Use order repetition as familiarity evidence only. A `Rate Order` control or public meal review is not evidence of the user's preference.

## Menu extraction

- Use the selected delivery date's Full Menu.
- CookUnity may virtualize cards and unmount them when another section opens. Capture each eligible section while it is expanded.
- Prefer semantic labels and stable card attributes over coordinates or brittle source ordering.
- Deduplicate by meal identity or normalized name.
- Exclude categories and items according to the confirmed profile.
- Preserve name, description, relevant nutrition, rating, labels, category, availability, and premium surcharge when present.
- Verify the extraction scope and report categories that could not be read.

### Completeness and search checks

- Traverse every eligible section from top to bottom, including pagination, load-more controls, nested scroll containers, and offscreen or virtualized cards. Capture cards during traversal; a single DOM snapshot may contain only currently mounted cards.
- Wait for rendered results after each section, filter, or search change. Compare any displayed result count against unique captured meals. Finish only after reaching an observed end and resolving count discrepancies; if no count exists, report the traversal basis rather than claiming count-backed completeness.
- Search is a locator aid, not a substitute for the full-menu inventory. For a requested meal, inspect the entire search result area, including below the fold. Try a distinctive shortened title and check the relevant full-menu section before declaring it unavailable.
- Normalize case, whitespace, and straight/curly apostrophes for matching, but retain exact displayed titles and distinguish genuinely different meal variants. Prefer stable product identity when available.
- If results are incomplete, say which scope is unverified. Never turn an incomplete search into a confident absence claim.

## Approved cart reconciliation

1. Read the complete existing cart and the selected delivery date before changing anything. Auto-filled items are not user-approved recommendations.
2. Calculate item/quantity differences against the exact approved target. Obtain approval for removals as well as additions; retain correct existing quantities.
3. Apply changes one at a time using freshly inspected controls. After each operation, verify the affected quantity. Before retrying a timeout or ambiguous result, inspect state to avoid duplicate additions or removals.
4. Stop for user direction if a requested replacement is unavailable, a premium or price changes materially, or an action would exceed approved scope. Never select an unsolicited substitute.
5. Re-open and traverse the entire cart, not just its counter or first visible rows. Compare item identities and quantities to the approved map in both directions: no missing approved items and no extra items.
6. Check summed meal quantities, delivery date, exclusions, eligible categories, premium count, displayed surcharges, and material totals. A counter of 12 alone is not proof of the correct 12 meals.
7. Hand back an itemized verified cart only when these checks pass. Explicitly state any cost field not displayed and leave checkout to the user when that is their preference. Do not change auto-order or subscription settings without separate authorization.

## Safety and recovery

- Do not activate `Add`, `Add meal`, cart, rating, referral, subscription, or checkout controls during read-only extraction.
- If navigation accidentally opens a detail page, return to the menu and re-establish the selected date before continuing.
- If page structure changes, inspect the visible state and rediscover semantic elements. Do not blindly reuse stale indexes, coordinates, selectors, or authentication URLs.
- Verify cart state before and after any approved mutation.

# Site adapters

A site adapter captures website-specific behavior without narrowing the general workflow. Store adapters outside the reusable core or as separate focused references when packaging known sites.

An adapter should define only what materially changes execution:

- site and account surface;
- required browser, extension, plugin, connector, or permissions;
- supported login handoff;
- site-specific intake questions;
- relevant live history or account context;
- reliable read-only extraction method;
- fields to collect;
- interpretation and ranking rules;
- mutations the workflow may propose;
- approval gates and final-action boundary;
- verification signals;
- recovery behavior when the page changes or data is incomplete.

Do not store user-specific preferences, credentials, stale prices, current inventories, or temporary selectors presented as permanent facts. Prefer accessible labels, roles, and stable semantic attributes. Treat CSS selectors as implementation details that may require rediscovery.

## Adapter outcome

At runtime, combine:

1. the general lifecycle from `SKILL.md`;
2. the selected site's adapter;
3. the confirmed per-user profile;
4. live website state;
5. the user's current request and approvals.

When these conflict, current user instructions and safety boundaries take precedence over stored preferences and historical behavior.

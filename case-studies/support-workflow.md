# Human-reviewed Support Workflow

Derived from existing ticket-planning, combined planning/drafting, and release-checking instruction skills inspected locally. Raw originals contain organization-specific identifiers and policies and are withheld. This generalized case study is not a runnable replacement or measured outcome report.

Support analysts need to reconcile incident reports, engineering work, releases, and deployment evidence before recommending action or writing a customer update.

1. Confirm the operator and available read-only integrations; report missing access.
2. Read the target incident and perform bounded research on relevant engineering work and related incidents.
3. Separate observed facts, hypotheses, confidence, and missing information.
4. Produce a structured brief: environment, versions, evidence, proposed next steps, customer-safe facts, unresolved questions.
5. Draft only from that brief; keep internal hypotheses and other customers' information out of external replies.
6. Leave posting and ticket changes to human review. These skills provide plans and drafts rather than changing production systems.

A companion release-check design reconciles linked fixes with deployment evidence. A closed engineering issue or planned release is insufficient proof of installation. Partial fixes, conflicting sources, and incompatible release branches require explicit handling. Organization policies must be configured and verified rather than assumed universal.

Fictional example: SUP-101 reports failed sign-ins in test. A linked fix is closed, but installation evidence is unavailable. The brief marks deployment unverified rather than telling the customer the fix is installed. After a compatible deployed version is verified, the analyst can review a draft testing request.

The artifacts establish design, not runtime effectiveness. This export did not access workplace systems, verify connector permissions, run these workflows, or measure accuracy or time savings. No internal scoring formulas, staff mappings, tenant IDs, ticket examples, or private links are reproduced.

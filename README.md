# Automation & AI Workflow Portfolio
### Peter Brobbey

This portfolio collects projects from my work with Python, API integration, and practical AI workflows. These workflows are minor examples to solve everyday problems I encountered: reviewing support tickets, planning meals, and making an AI assistant more useful during a game.

The common thread is reliability: checking the information going in, making clear decisions about what happens next, and verifying the result.

## What's inside

### Ticket Review Workflow
**Python · APIs · JSON · Testing · OpenAI**

A learning project that explores how to turn a support incident into a useful recommendation.

The Python code handles two related tasks: converting API data into validated tickets for simple classification, and requesting an AI review of an incident. The review includes a recommendation, a quote from the original message as evidence, and a follow-up question when more information is needed.

The project includes input validation, error handling, response parsing, and tests. It uses fictional incidents and a simplified review policy.

[Explore the code and setup guide →](projects/ticket-review-workflow/README.md)

### CookUnity Meal Planner
**Personalization · Browser Workflows · Feedback**

A custom assistant skill for making weekly meal selection more deliberate.

It lays out how to review the current menu, account for confirmed likes and dislikes, balance familiar meals with new choices, and check that the final cart matches the approved selection. Feedback from meals informs future recommendations.

The design also handles practical complications: changing menus, repeated meals, premium charges, and items already in the cart. Ordering stays under the user's control.

[Explore the meal-planning skill →](skills/cookunity-meal-planner/SKILL.md)

### Authenticated Web Workflow
**Reusable Workflow Design · Privacy · Verification**

A reusable foundation for assistant tasks on websites where the user is signed in.

It defines the steps around the actual task: checking access, gathering preferences, reading current information, presenting a proposal, obtaining approval, and verifying what changed. Site-specific rules and personal preferences are kept separate so the approach can be adapted.

[Explore the workflow and reference guides →](skills/authenticated-web-workflow/SKILL.md)

### Game Screen Observer
**Computer Use · Visual Context · Conversational Design**

A skill designed to let an assistant discuss what's happening in a game from screenshots, while the player keeps control.

It specifies how to check that a screenshot actually shows the game, comment on visible events, avoid unwanted spoilers, and stop when capture fails. Observations are brief and bounded; the skill does not provide continuous video or audio access.

[Explore the observer skill →](skills/game-screen-observer/SKILL.md)

### Support Workflow Case Study
**Troubleshooting · Research · Planning · Customer Communication**

A generalized look at support-assistant workflows I've designed for researching tickets, preparing action plans, drafting updates, and checking release information.

The design separates investigation from writing: first establish the facts and unresolved questions, then draft from that brief. It also distinguishes a completed engineering fix from evidence that the fix was actually deployed.

This public case study describes the architecture with a fictional example. Workplace-specific instructions and records remain private.

[Read the case study →](case-studies/support-workflow.md)

## About the work

This is a growing portfolio of learning projects and workflow designs developed with AI assistance. I use AI for guided development, review, troubleshooting, and documentation.

The ticket project contains executable Python. The custom skills are written instructions that guide an assistant with compatible tools; they are not standalone applications. Each project has its own limits, and inclusion here does not imply production readiness.

For setup instructions, start with the [ticket workflow guide](projects/ticket-review-workflow/README.md). For the checks performed on this collection and the work intentionally left out, see [verification notes](docs/VERIFICATION.md) and [repository scope](docs/SCOPE.md).

# Ticket Review Workflow

A Python project exploring how software and AI can help review support incidents. It combines a conventional data-processing path with a model-assisted review path, making it possible to compare simple classification rules with recommendations generated from an incident description.

The work includes adapting API responses into ticket records, validating input, handling failures, parsing model output, and checking that supporting evidence appears in the original message. Assertion scripts exercise the individual pieces and the ticket-processing pipeline.

**What this demonstrates:** connecting Python functions into a workflow, integrating an AI API, and checking data at the boundaries between components. The project uses fictional incidents and a simplified policy as a learning environment.

## Implementation overview

Educational Python work using fictional incidents:

1. API response -> check JSON media type -> adapt post to ticket -> validate fields and IDs -> classify message.
2. Incident -> model request -> remove supported JSON fence -> parse JSON -> validate recommendation and exact evidence quote -> display review.

post_adapter.py maps integer IDs and string bodies, rejecting booleans as IDs. content_type_check.py normalizes the JSON media type. session_07.py validates ticket structure and unique IDs, then classifies the exact word outage. review_workflow.py makes a model request with timeout and no automatic retries, parses the output, and calls review_validator.py to check fields, recommendation, and quoted evidence.

## Setup and checks

Verified on Python 3.13.5. From this directory:

    python -m venv .venv
    # Activate .venv with the command for your shell.
    python -m pip install -r requirements.txt
    python run_checks.py

The runner executes existing assertion scripts directly; it makes no model requests and fetches no web pages. Seven checks need only the standard library. The parsing check needs the OpenAI dependency because of its module import.

## Optional demonstrations

Running python http_practice.py fetches a public sample API. This was not run for the export.

To run session_07.py, create fictional tickets.json data:

    [{"id":"DEMO-1","message":"Network outage"}]

Running python session_07.py creates ticket_report.json and refuses to overwrite an existing report.

Running python review_workflow.py runs a fixed offline simulation. Setting `text = request_review_text(message, load_review_prompt())` in run_review runs a live mode with a call to an OpenAI model with real API requests. Configure OPENAI_API_KEY privately in the environment and review the configured model/cost before use. No paid requests were run for this export.

test_review_evaluation.py is a demonstration with a deliberately failing stub, not a passing regression test. It is excluded from the runner and may print ERROR or FAIL by design.

## Known limits

Exact-word classification is a learning exercise, not a production incident policy. Empty messages produce an invalid classification. Substring evidence matching does not prove correct reasoning. The validator does not fully enforce the prompt's follow-up-question rule. JSON-fence handling supports a narrow format. No deployment or production-readiness claim is made.

Source files are unchanged. The runner, dependency note, and portfolio documentation were added for this export.

## Run Guides

[Review workflow and Evaluator instructions](EVALUATOR_RUN.md)
[Source-honesty grader instructions](SOURCE_HONESTY_RUN.md)

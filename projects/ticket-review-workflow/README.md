# Ticket Review Workflow

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

Running python review_workflow.py makes a paid model request. Configure OPENAI_API_KEY privately in the environment and review the configured model/cost before use. No paid requests were run for this export.

test_review_evaluation.py is a demonstration with a deliberately failing stub, not a passing regression test. It is excluded from the runner and may print ERROR or FAIL by design.

## Known limits

Exact-word classification is a learning exercise, not a production incident policy. Empty messages produce an invalid classification. Substring evidence matching does not prove correct reasoning. The validator does not fully enforce the prompt's follow-up-question rule. JSON-fence handling supports a narrow format. No deployment or production-readiness claim is made.

Source files are unchanged. The runner, dependency note, and portfolio documentation were added for this export.

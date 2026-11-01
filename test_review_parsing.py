from review_workflow import unraw_review_text

assert (
    unraw_review_text('{"recommendation": "Urgent review"}')
    == '{"recommendation": "Urgent review"}'
)  # Test 1: Plain JSON stays unchanged
assert (
    unraw_review_text('```json\n{"recommendation": "Urgent review"}\n```')
    == '{"recommendation": "Urgent review"}'
)  # Test 2: JSON with Markdown fence becomes plain JSON
assert (
    unraw_review_text("") == ""
)  # Test 3: Empty strings returns an empty string without an error

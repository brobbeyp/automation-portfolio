from review_validator import validate_review

message = "One user cannot sign in."

try:
    validate_review(
        {
            "evidence": " ",
            "recommendation": "Not urgent under this policy",
            "follow_up_question": "",
        },
        message,
    )
except ValueError as error:
    assert str(error) == "Evidence is empty or only whitespace"
    print("Caught ValueError, evidence is empty or contains spaces.", error)
else:
    raise AssertionError(
        "Failed to catch Value Error, input string is empty or contains spaces"
    )

try:
    validate_review(
        {
            "evidence": "Nobody can access the app.",
            "recommendation": "Not urgent under this policy",
            "follow_up_question": "",
        },
        message,
    )
except ValueError as error:
    assert str(error) == "Original evidence string does not appear in 'message'"
    print("Caught ValueError, evidence is not in message.", error)
else:
    raise AssertionError("Failed to catch Value Error, evidence is not in message")

try:
    validate_review(
        {
            "evidence": "One user",
            "recommendation": "Not urgent under this policy",
        },
        message,
    )
except ValueError as error:
    assert str(error) == "follow up question is missing"
    print("Caught follow up question is missing.", error)
else:
    raise AssertionError("Failed to catch missing follow up question")

try:
    validate_review(
        {
            "evidence": "One user",
            "recommendation": "Not urgent under this policy",
            "follow_up_question": 123,
        },
        message,
    )
except ValueError as error:
    assert str(error) == "Follow up question is not a string"
    print("Caught follow_up_question wrong type.", error)
else:
    raise AssertionError("Failed to catch missing follow up question")

assert validate_review(
    {
        "evidence": "One user",
        "recommendation": "Not urgent under this policy",
        "follow_up_question": "",
    },
    message,
) == {
    "evidence": "One user",
    "recommendation": "Not urgent under this policy",
    "follow_up_question": "",
}

from review_validator import validate_review

message = "One user cannot sign in."

try:
    validate_review(
        {"evidence": " ", "recommendation": "Not urgent under this policy"}, message
    )
except ValueError as error:
    print("Caught ValueError, evidence is empty or contains spaces")
else:
    raise AssertionError(
        "Failed to catch Value Error, input string is empty or contains spaces"
    )

try:
    validate_review(
        {
            "evidence": "Nobody can access the app.",
            "recommendation": "Not urgent under this policy",
        },
        message,
    )
except ValueError as error:
    print("Caught ValueError, evidence is not in message")
else:
    raise AssertionError("Failed to catch Value Error, evidence is not in message")

assert validate_review(
    {"evidence": "One user", "recommendation": "Not urgent under this policy"}, message
) == {"evidence": "One user", "recommendation": "Not urgent under this policy"}

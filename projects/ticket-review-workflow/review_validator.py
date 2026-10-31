def validate_review(review, message):

    if not isinstance(review, dict):  # Checking review type
        raise ValueError("Review is not a dict")

    elif not "recommendation" in review:  # Checking key existence
        raise ValueError("review is missing a recommendation")
    elif not isinstance(review["recommendation"], str):  # Checking correct type
        raise ValueError("recommendation is not a string")
    elif review["recommendation"] not in (  # Checking allowed value
        "Urgent review",
        "Not urgent under this policy",
        "Insufficient information",
    ):
        raise ValueError("recommendation does not match a permitted string exactly")

    elif not "evidence" in review:
        raise ValueError("review is missing evidence")
    elif not isinstance(review["evidence"], str):
        raise ValueError("Evidence is not a string")

    elif not "follow_up_question" in review:
        raise ValueError("follow up question is missing")
    elif not isinstance(review["follow_up_question"], str):
        raise ValueError("Follow up question is not a string")

    evidence = review["evidence"]
    if evidence.strip() == "":
        raise ValueError("Evidence is empty or only whitespace")
    elif evidence not in message:
        raise ValueError("Original evidence string does not appear in 'message'")
    else:
        return review

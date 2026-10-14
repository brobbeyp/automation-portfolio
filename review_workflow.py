from review_validator import validate_review


def simulate_review(message):
    result = {
        "recommendation": "Insufficient information",
        "evidence": "Users cannot sign in.",
        "follow_up_question": "Can anyone still sign in?",
    }

    return result


def run_review(message):
    return validate_review(simulate_review(message), message)


if __name__ == "__main__":
    message = "Users cannot sign in."
    try:
        result = run_review(message)
    except ValueError as error:
        print("Review rejected:", error)
    else:
        print("SIMULATED REVIEW\n")

        print("Recommendation: ", result["recommendation"])
        print("Evidence: ", result["evidence"])
        print("Follow up question: ", result["follow_up_question"])

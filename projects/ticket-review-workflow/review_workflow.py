from pathlib import Path
from review_validator import validate_review
from openai import OpenAI, APIConnectionError, APIStatusError
import json


def simulate_review(message, prompt):
    # test_case_1 = '```json\n{\n  "recommendation": "Urgent review",\n  "evidence": "All users cannot access the service.",\n  "follow_up_question": ""\n}\n```'
    # return test_case_1

    result = {
        "recommendation": "Insufficient information",
        "evidence": "Users cannot sign in.",
        "follow_up_question": "Can anyone still sign in?",
    }
    return json.dumps(result)


def load_review_prompt():
    path = Path(__file__).with_name("review_prompt.txt")
    text = path.read_text(encoding="utf-8")
    return text


def request_review_text(message, prompt):
    client = OpenAI(timeout=20, max_retries=0)
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=prompt,
        input=message,
        max_output_tokens=300,
        store=False,
    )

    print("Response status:", response.status)
    print("Token usage:", response.usage)

    return response.output_text


def unraw_review_text(text):
    text = text.strip()
    lines = text.splitlines()
    if lines and lines[0] == "```json" and lines[-1] == "```":
        return "\n".join(lines[1:-1])
    else:
        return text


def run_review(message):
    text = request_review_text(message, load_review_prompt())  # Real GPT Request

    # text = simulate_review(message, load_review_prompt()) #Simulated GPT Request

    print("Raw response:", repr(text))
    print("Unraw response:", unraw_review_text(text))

    parsed = json.loads(unraw_review_text(text))
    return validate_review(parsed, message)


if __name__ == "__main__":
    message = "Users cannot sign in."
    try:
        result = run_review(message)
    except APIConnectionError as error:
        print("Could not connect to the review API:", error)
    except APIStatusError as error:
        print("Review API rejected the request:", error.status_code)
    except json.JSONDecodeError as error:
        print("Review response is not valid JSON:", error)
    except ValueError as error:
        print("Review rejected:", error)
    else:
        print("MODEL REVIEW\n")

        print("Recommendation: ", result["recommendation"])
        print("Evidence: ", result["evidence"])
        print("Follow up question: ", result["follow_up_question"])

import json
from post_adapter import post_to_ticket

# Expected Error Tests

try:
    json.loads("")
except json.JSONDecodeError as error:
    print("Expected Error Test 1: Success. Caught empty body string", error)
else:
    raise AssertionError(
        "Expected Error Test 1: Failure. Failed to catch empty body string"
    )

emptyDict = json.loads("{}")
try:
    post_to_ticket(emptyDict)
except ValueError as error:
    print("Expected Error Test 2: Success. Caught dict missing required fields", error)
else:
    raise AssertionError(
        "Expected Error Test 2: Failure. Failed to catch dict missing required fields"
    )

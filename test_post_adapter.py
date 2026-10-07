from post_adapter import post_to_ticket

# Success Tests
assert post_to_ticket({"id": 8, "body": "Network outage"}) == {
    "id": "T-8",
    "message": "Network outage",
}

assert post_to_ticket({"id": 8, "body": ""}) == {"id": "T-8", "message": ""}


# Expected-Error Tests
try:
    post_to_ticket({"id": True, "body": "Network outage"})
except ValueError as error:
    print("Expected Error Test 1: Caught 'id' wrong type. ", error)
else:
    raise AssertionError("Expected Error Test 1: Failed to catch 'id' wrong type")

try:
    post_to_ticket({"id": 8, "body": ["This is a string inside a list"]})
except ValueError as error:
    print("Expected Error Test 2: Caught 'body' wrong type. ", error)
else:
    raise AssertionError("Expected Error Test 2: Failed to catch 'body' wrong type")

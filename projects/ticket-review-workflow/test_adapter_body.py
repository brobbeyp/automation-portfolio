from post_adapter import post_to_ticket

assert post_to_ticket({"id": 8, "body": "This is a success case"}) == {
    "id": "T-8",
    "message": "This is a success case",
}

try:
    post_to_ticket({"id": 8, "body": 4})
except ValueError as error:
    print("Caught body incorrect type", error)
else:
    raise AssertionError("Failed to catch body incorrect type")

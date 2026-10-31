from post_adapter import post_to_ticket
from session_07 import classify_tickets

post = {"id": 42, "body": "  NETWORK OUTAGE  "}

assert classify_tickets([post_to_ticket(post)]) == [
    {"id": "T-42", "classification": "urgent"}
]

empty_post = {"id": 43, "body": ""}
assert classify_tickets([post_to_ticket(empty_post)]) == [
    {"id": "T-43", "classification": "invalid"}
]
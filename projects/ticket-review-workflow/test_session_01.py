from session_01 import assess_action

assert assess_action("send a message") == "approval required"
assert assess_action("delete a file") == "approval required"
## assert assess_action("grow a plant") == "approval required"
assert assess_action("") == "invalid"
assert assess_action("LeArN PytHoN") == "safe to plan"

actual = assess_action("grow a plant")
expected = "safe to plan"
assert actual == expected, f"Expected {expected}, but got {actual}"

assert assess_action("pay,buy") == "approval required"
assert assess_action("show the repayment schedule") == "safe to plan"
assert assess_action("pay!") == "approval required"
assert assess_action("!") == "invalid"
print("All tests passed")

def testPath(tickets):
    raise ValueError("False ValueError: This error always triggers")

try:
    testPath([{"id": "T-103"}])
except ValueError as error:
    print(error)
else:
    raise AssertionError("Expected ValueError: Ticket is missing 'message'")

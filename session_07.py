import json


def classify_ticket(
    message,
):  # Classifies a single ticket's message as invalid, urgent, or normal.
    message = message.lower().strip().split()
    if message == []:
        return "invalid"
    elif "outage" in message:
        return "urgent"
    else:
        return "normal"


def classify_messages(messages):  # Classifies several ticket's messages at once
    results = []
    for message in messages:
        results.append(classify_ticket(message))
    return results


def classify_tickets(
    tickets,
):  # returns a list of dictionaries that include the ticket's ID and Classification, JSON object

    results = []
    seen_ids = set()

    if not isinstance(tickets, list):  # Validates that the ticket is a l
        raise ValueError("Tickets must be a list")

    for ticket in tickets:  # Validates that the ticket has the appropriate fields
        if not isinstance(ticket, dict):
            raise ValueError("Ticket is not a dictionary")
        if "message" not in ticket:
            raise ValueError("Ticket is missing 'message'")
        elif "id" not in ticket:
            raise ValueError("Ticket is missing 'id'")
        elif not isinstance(ticket["message"], str):
            raise ValueError("Ticket 'message' must be a string")
        elif not isinstance(ticket["id"], str):
            raise ValueError("Ticket 'id' must be a string")

        else:  # Seen ID Check
            if ticket["id"] in seen_ids:
                raise ValueError("Ticket 'id' must not be a duplicate")
            else:
                seen_ids.add(ticket["id"])

                results.append(
                    {
                        "id": ticket["id"],
                        "classification": classify_ticket(ticket["message"]),
                    }
                )

    return results


if __name__ == "__main__":
    try:
        with open(
            "tickets.json", "r", encoding="utf-8"
        ) as file:  # Loading the tickets from the JSON file
            loaded_tickets = json.load(file)

        classified_tickets = classify_tickets(loaded_tickets)
        print("Loaded tickets:", classified_tickets)

        with open(
            "ticket_report.json", "x", encoding="utf-8"
        ) as report_file:  # Writing the results to a new file
            json.dump(classified_tickets, report_file, indent=2)

    except ValueError as error:  # Exception branch for input ValueError
        print(error)
    except FileExistsError:  # Exception branch for FileExistsError
        print("Report already exists; choose a new output filename.")

    assert classify_messages([]) == []
    assert classify_messages(
        ["The Network has an outage", "Please reset my password", "    "]
    ) == ["urgent", "normal", "invalid"]

    assert classify_tickets([]) == []

    assert classify_tickets(
        [
            {"id": "1", "message": "This is an outage"},
            {"id": "2", "message": "This is a normal ticket"},
        ]
    ) == [
        {"id": "1", "classification": "urgent"},
        {"id": "2", "classification": "normal"},
    ]

    assert classify_ticket("") == "invalid"
    assert classify_ticket("There has been an outage") == "urgent"
    assert classify_ticket("This is a fake outages message") == "normal"
    assert classify_ticket("  OUTAGE  ") == "urgent"

    # Direct Tests with Expected Errors
    print("** DIRECT TESTS **\n")
    try:
        classify_tickets([{"id": "T-103"}])
    except ValueError:
        print("Caught the expected ValueError:  Ticket is missing 'message'")
    else:
        raise AssertionError("Expected ValueError: Ticket is missing 'message'")

    try:
        classify_tickets([{"message": "There is an outage"}])
    except ValueError:
        print("Caught the expected ValueError: Ticket is missing 'id'")
    else:
        raise AssertionError("Expected ValueError: Ticket is missing 'id'")

    try:
        classify_tickets([{"id": "T-104", "message": 42}])
    except ValueError:
        print("Caught the expected ValueError: Ticket 'message' must be a string")
    else:
        raise AssertionError("Expected ValueError")

    try:
        classify_tickets([{"id": 42, "message": "Everything is all normal"}])
    except ValueError:
        print("Caught the expected ValueError: Ticket 'id' must be a string")
    else:
        raise AssertionError("Expected ValueError: Ticket 'id' must be a string")

    try:
        classify_tickets({"id": "T-105", "message": "Network outage"})
    except ValueError:
        print("Caught the expected ValueError: Tickets must be a list")
    else:
        raise AssertionError("Expected ValueError: Tickets must be a list")

    try:
        classify_tickets([42])
    except ValueError:
        print("Caught the expected ValueError: Ticket must be a dict")
    else:
        raise AssertionError("Expected ValueError: Ticket must be a dict")

    try:
        classify_tickets(
            [
                {"id": "T-101", "message": "This is the normal original ticket"},
                {"id": "T-101", "message": "This is the second outage ticket"},
            ]
        )
    except ValueError:
        print("Caught the expected ValueError: Ticket 'id' must not be a duplicate")
    else:
        raise AssertionError("Expected ValueError: Ticket 'id' must not be a duplicate")

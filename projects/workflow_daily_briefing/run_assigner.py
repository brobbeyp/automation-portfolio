def assign_item(item):
    if item["due_date"]:
        return "deadline"
    elif ("#focus" in item["tags"]) or item["focus-today"] == True:
        return "focus"
    else:
        return "other"


def urgency_response(item):
    item["focus-today"] = False
    return item


def run_assigner(item):
    item = urgency_response(item)
    item["assignment"] = assign_item(item)
    return item


if __name__ == "__main__":
    testCase = {
        "text": "Prepare for Ronco today.",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
    }
    testCase2 = {
        "text": "Submit a form by tomorrow",
        "due_date": "2026-11-04",
        "tags": [],
        "source": "daily-note.md",
    }
    testCase3 = {
        "text": "Define the first Workspace dashboard workflow",
        "due_date": None,
        "tags": ["#focus"],
        "source": "daily-note.md",
    }
    testCase4 = {
        "text": "Go to the park",
        "due_date": "2026-11-04",
        "tags": ["#focus"],
        "source": "daily-note.md",
    }
    testCase5 = {
        "text": "Add new functionality to the life dashboard",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
        "focus-today": True,
    }

    assert run_assigner(testCase) == {
        "text": "Prepare for Ronco today.",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "other",
    }
    assert run_assigner(testCase2) == {
        "text": "Submit a form by tomorrow",
        "due_date": "2026-11-04",
        "tags": [],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "deadline",
    }
    assert run_assigner(testCase3) == {
        "text": "Define the first Workspace dashboard workflow",
        "due_date": None,
        "tags": ["#focus"],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "focus",
    }
    assert run_assigner(testCase4) == {
        "text": "Go to the park",
        "due_date": "2026-11-04",
        "tags": ["#focus"],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "deadline",
    }
    assert assign_item(testCase5) == "focus"
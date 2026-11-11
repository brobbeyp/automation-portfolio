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


def run_multiple_assigners(cases):

    assignedCases = []

    for case in cases:
        caseCopy = case.copy()
        assignedCases.append(run_assigner(caseCopy))
    return assignedCases


def test_mutation(case):
    original = case.copy()
    run_multiple_assigners([case])
    assert (case) == original
    return case


def group_tasks(tasks):
    result = {"deadline": [], "focus": [], "other": []}

    for task in tasks:
        if task["assignment"] == "deadline":
            result["deadline"].append(task)
        elif task["assignment"] == "focus":
            result["focus"].append(task)
        else:
            result["other"].append(task)
    return result


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
    testCase6 = {
        "text": "This case tests if the original item is mutated",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
        "focus-today": True,
    }
    testCase7 = {
        "text": "This case tests if order works in group_tasks",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
        "assignment": "other",
        "focus-today": False,
    }
    testCase8 = {
        "text": "This second case tests if order works in group_tasks",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
        "assignment": "other",
        "focus-today": False,
    }
    testCase9 = {
        "text": "This case tests that routing still works in group_tasks",
        "due_date": "2026-11-04",
        "tags": [],
        "source": "daily-note.md",
        "assignment": "deadline",
        "focus-today": False,
    }
    testCase10 = {
        "text": "This case tests that routing still works in group_tasks",
        "due_date": "",
        "tags": [],
        "source": "daily-note.md",
        "assignment": "focus",
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

    assert (run_multiple_assigners([])) == []

    assert (run_multiple_assigners([testCase, testCase2, testCase3])) == [
        {
            "text": "Prepare for Ronco today.",
            "due_date": None,
            "tags": [],
            "source": "daily-note.md",
            "focus-today": False,
            "assignment": "other",
        },
        {
            "text": "Submit a form by tomorrow",
            "due_date": "2026-11-04",
            "tags": [],
            "source": "daily-note.md",
            "focus-today": False,
            "assignment": "deadline",
        },
        {
            "text": "Define the first Workspace dashboard workflow",
            "due_date": None,
            "tags": ["#focus"],
            "source": "daily-note.md",
            "focus-today": False,
            "assignment": "focus",
        },
    ]

    test_mutation(testCase6)

    assert (group_tasks([])) == {"deadline": [], "focus": [], "other": []}

    assert (group_tasks([testCase7, testCase8, testCase9, testCase10])) == {
        "deadline": [testCase9],
        "focus": [testCase10],
        "other": [
            testCase7,
            testCase8,
        ],
    }

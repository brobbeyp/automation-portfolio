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


def test_run_mutation(cases):
    casesCopy = [case.copy() for case in cases]

    test_run(cases)

    for i in range(len(cases)):
        assert (cases[i]) == casesCopy[i]


def test_display(tasks):
    group = group_tasks(tasks)
    display = display_tasks(group)
    return display


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


def display_tasks(groupedTasks):
    punctuation = ["?", ".", "!"]

    deadline = "Tasks with a deadline:"
    if groupedTasks["deadline"] == []:
        deadline += " None."
    for task in groupedTasks["deadline"]:
        if task["text"][-1:] in punctuation:
            deadline += f" {task['text']}"
        else:
            deadline += f" {task['text']}."

    focus = "Today's Focus:"
    if groupedTasks["focus"] == []:
        focus += " None."
    for task in groupedTasks["focus"]:
        if task["text"][-1:] in punctuation:
            focus += f" {task['text']}"
        else:
            focus += f" {task['text']}."

    other = "Other tasks:"
    if groupedTasks["other"] == []:
        other += " None."
    for task in groupedTasks["other"]:
        if task["text"][-1:] in punctuation:
            other += f" {task['text']}"
        else:
            other += f" {task['text']}."
    return f"Hello, Peter! Today's tasks are as follows:\n{deadline}\n{focus}\n{other}"


def test_run(tasks):
    assignedTasks = run_multiple_assigners(tasks)
    groupedTasks = group_tasks(assignedTasks)
    return display_tasks(groupedTasks)


if __name__ == "__main__":
    testCase = {
        "text": "Prepare for Ronco today",
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
    testCase11 = {
        "text": "This case tests displaying grouped tasks as a readable briefing, routed to deadline",
        "due_date": "2026-11-04",
        "tags": [],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "deadline",
    }
    testCase12 = {
        "text": "This case tests displaying grouped tasks as a readable briefing, routed to other",
        "due_date": "",
        "tags": [],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "other",
    }
    testCase13 = {
        "text": "This case tests displaying grouped tasks as a readable briefing, routed to other also, and confirms order is preserved",
        "due_date": "",
        "tags": [],
        "source": "daily-note.md",
        "focus-today": False,
        "assignment": "other",
    }
    testCase14 = {
        "text": "This case tests displaying grouped tasks as a readable brief, routed to focus",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
        "focus-today": True,
        "assignment": "focus",
    }
    testCase15 = {
        "text": "Test full run, routed to other",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
    }
    testCase16 = {
        "text": "Test full run, routed to deadline",
        "due_date": "2026-11-04",
        "tags": [],
        "source": "daily-note.md",
    }
    testCase17 = {
        "text": "Test full run, routed to focus",
        "due_date": None,
        "tags": ["#focus"],
        "source": "daily-note.md",
    }
    testCase18 = {
        "text": "Test full run, routed to focus, checking order",
        "due_date": None,
        "tags": ["#focus"],
        "source": "daily-note.md",
    }
    testCase19 = {
        "text": "Test full run, routed to focus, checking that punctuation is preserved!",
        "due_date": None,
        "tags": [],
        "source": "daily-note.md",
    }
    testCase20 = {
        "text": "Test full run, routed to focus, checking that punctuation is preserved?",
        "due_date": "2026-11-13",
        "tags": [],
        "source": "daily-note.md",
    }
    testCase21 = {
        "text": "Test full run, routed to focus, checking that punctuation is preserved.",
        "due_date": None,
        "tags": ["#focus"],
        "source": "daily-note.md",
    }
    assert run_assigner(testCase) == {
        "text": "Prepare for Ronco today",
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
            "text": "Prepare for Ronco today",
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

    assert (test_display([])) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: None.\n"
        "Today's Focus: None.\n"
        "Other tasks: None."
    )

    assert (test_display([testCase14, testCase13, testCase12, testCase11])) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: This case tests displaying grouped tasks as a readable briefing, routed to deadline.\n"
        "Today's Focus: This case tests displaying grouped tasks as a readable brief, routed to focus.\n"
        "Other tasks: This case tests displaying grouped tasks as a readable briefing, routed to other also, and confirms order is preserved. This case tests displaying grouped tasks as a readable briefing, routed to other."
    )

    assert (test_run([])) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: None.\n"
        "Today's Focus: None.\n"
        "Other tasks: None."
    )

    assert (test_run([testCase15, testCase16, testCase18, testCase17])) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: Test full run, routed to deadline.\n"
        "Today's Focus: Test full run, routed to focus, checking order. Test full run, routed to focus.\n"
        "Other tasks: Test full run, routed to other."
    )

    test_run_mutation([testCase15, testCase16, testCase18, testCase17])

    assert test_run([testCase19]) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: None.\n"
        "Today's Focus: None.\n"
        "Other tasks: Test full run, routed to focus, checking that punctuation is preserved!"
    )
    assert test_run([testCase20]) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: Test full run, routed to focus, checking that punctuation is preserved?\n"
        "Today's Focus: None.\n"
        "Other tasks: None."
    )
    assert test_run([testCase21]) == (
        "Hello, Peter! Today's tasks are as follows:\n"
        "Tasks with a deadline: None.\n"
        "Today's Focus: Test full run, routed to focus, checking that punctuation is preserved.\n"
        "Other tasks: None."
    )

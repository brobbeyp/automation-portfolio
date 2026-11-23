## Daily Briefing Tool

### Description:
- The Daily Briefing tool reads a JSON file of task records, assigns each task to a deadline, focus, or other category, and prints a human-readable briefing.

### Author:
- Peter Brobbey, Date: 11.22.26

### Input:
- The tool accepts a JSON document with an array of dictionaries. Each dictionary must contain the `text`, `due_date`, `tags`, and `source` fields. The tool verifies that the document is a list containing dictionaries. The tool then verifies that all four required fields exist.

- Files containing malformed JSON raise a `ValueError` and files missing required fields raise a `ValueError` that names the missing field.

- Running `run_assigner.py` executes the built-in assertions and prints the briefing for the hard-coded fixture path.


### Output:
- A successful run outputs the following briefing string:

```
Hello, Peter! Today's tasks are as follows:
Tasks with a deadline: None.
Today's Focus: None.
Other tasks: None.
```
- For testCase.json:
 ```json
  [
    {
        "text": "Prepare for Ronco today",
        "due_date": null,
        "tags": [],
        "source": "daily-note.md"
    }
  ]
```
- The tool's expected output is:

```
Hello, Peter! Today's tasks are as follows:
Tasks with a deadline: None.
Today's Focus: None.
Other tasks: Prepare for Ronco today.
```
- For multiple tasks in a single document, such as testCase5.json:
```json
[
    {
        "text": "First task, routed to other",
        "due_date": null,
        "tags": [],
        "source": "daily-note.md"
    },
    {
        "text": "Second task, routed to other",
        "due_date": null,
        "tags": [],
        "source": "daily-note.md"
    },
    {
        "text": "Third task, routed to deadline",
        "due_date": "2026-11-04",
        "tags": [],
        "source": "daily-note.md"
    },
    {
        "text": "Fourth task, routed to focus",
        "due_date": null,
        "tags": [
            "#focus"
        ],
        "source": "daily-note.md"
    }
]
```
- The expected output is:
```
Hello, Peter! Today's tasks are as follows:
Tasks with a deadline: Third task, routed to deadline.
Today's Focus: Fourth task, routed to focus.
Other tasks: First task, routed to other. Second task, routed to other.
```

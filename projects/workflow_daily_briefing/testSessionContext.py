from sessionContext import (
    testGenerateContext,
    testGenerateContextString,
    buildSessionStartResponse,
)

if __name__ == "__main__":
    assert (testGenerateContext("testCase.json")) == [
        "C:\\Users\\brobb\\Documents\\Workspace\\Code\\Tutor\\AGENTS.md",
        "C:\\Users\\brobb\\Documents\\Workspace\\Code\\Tutor\\PROGRESS.md",
        "C:\\Users\\brobb\\Documents\\Workspace\\AGENTS.md",
    ]

    assert (testGenerateContext("testCase2.json")) == []

    assert (testGenerateContext("testCase3.json")) == [
        "C:\\Users\\brobb\\Documents\\Workspace\\Code\\Tutor\\projects\\workflow_daily_briefing\\PROGRESS.md",
        "C:\\Users\\brobb\\Documents\\Workspace\\Code\\Tutor\\AGENTS.md",
        "C:\\Users\\brobb\\Documents\\Workspace\\Code\\Tutor\\PROGRESS.md",
        "C:\\Users\\brobb\\Documents\\Workspace\\AGENTS.md",
    ]

    assert (testGenerateContext("testCase4.json")) == []

    expected = (
        # Single path expected output
        "Session context discovered, nearest folder first:\n"
        "\n"
        r"C:\Users\brobb\Documents\Workspace\AGENTS.md"
        "\nPurpose: Instructions applicable to work under this folder."
    )
    assert testGenerateContextString("testCase5.json") == expected

    expectedEmpty = "No context files found within the Workspace boundary."  # Empty case expected output
    assert testGenerateContextString("testCase4.json") == expectedEmpty

    expectedMultiplePaths = (
        "Session context discovered, nearest folder first:\n"
        "\n"
        r"C:\Users\brobb\Documents\Workspace\Code\Tutor\AGENTS.md"
        "\nPurpose: Instructions applicable to work under this folder.\n\n"
        r"C:\Users\brobb\Documents\Workspace\Code\Tutor\PROGRESS.md"
        "\nPurpose: Project checkpoint, recent evidence, and next steps.\n\n"
        r"C:\Users\brobb\Documents\Workspace\AGENTS.md"
        "\nPurpose: Instructions applicable to work under this folder.\n\n"
        r"C:\Users\brobb\Documents\Workspace\AGENTS.md"
        "\nPurpose: Instructions applicable to work under this folder."
    )
    assert (testGenerateContextString("testCase6.json")) == expectedMultiplePaths

    testEvent = {
        "hook_event_name": "SessionStart",
        "source": "startup",
        "cwd": "C:/Users/brobb/Documents/Workspace",
    }

    expectedSessionStartResponse = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": expected,
        }
    }

    assert buildSessionStartResponse(testEvent) == expectedSessionStartResponse

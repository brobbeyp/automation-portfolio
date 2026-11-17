import json
from pathlib import Path

index = {
    "AGENTS.md": "Instructions applicable to work under this folder.",
    "PROGRESS.md": "Project checkpoint, recent evidence, and next steps.",
}


def loadCase(
    caseFileName,
):  # loads a JSON case document as an object, accepts file name in same cwd
    with open(caseFileName, "r", encoding="utf-8") as file:
        case = json.load(file)
    return case


def generateContext(
    cwd,
):  # Accepts a current working directory string, iterates across the current and parent folders until the limit folder and returns a list of path strings for AGENTS/PROGRESS.MD files if present.

    limit = Path("C:/Users/brobb/Documents/Workspace").resolve()
    cwdPath = Path(cwd).resolve()
    result = []

    if cwdPath.is_relative_to(limit):  # Checks if the cwdPath is under the limit
        while (
            cwdPath != limit
        ):  # While not at the limit, check if the path for each source in index exists. If it does, add those paths as strings to the result list. Then change the cwdPath to the parent and repeat.
            for source in index:
                sourcePath = cwdPath / source

                if sourcePath.is_file():  # Check if source file exists in the current path and add it to result if it does
                    result.append(
                        str(
                            sourcePath
                        )  # Convert Path object to a string and append to the result
                    )

            cwdPath = cwdPath.parent

        if cwdPath == limit:  # At the limit, do a final check and add that to result
            for source in index:
                sourcePath = cwdPath / source

                if sourcePath.is_file():  # Check if source file exists in the current path and add it to result if it does
                    result.append(
                        str(
                            sourcePath
                        )  # Convert Path object to a string and append to the result
                    )

    return result


def generateContextString(paths):
    if paths == []:
        return "No context files found within the Workspace boundary."

    result = "Session context discovered, nearest folder first:"
    for path in paths:
        result += "\n\n" + path

        if Path(path).name in index:
            result += "\nPurpose: " + index[Path(path).name]

    return result


def testGenerateContext(filename):
    case = loadCase(filename)  # Select a case to load
    caseCWD = case["cwd"]  # Select the current working directory

    return generateContext(
        caseCWD
    )  # Pass the cwd str to workspaceContext, which returns a list of path strings


def testGenerateContextString(filename):
    context = testGenerateContext(filename)
    return generateContextString(context)


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

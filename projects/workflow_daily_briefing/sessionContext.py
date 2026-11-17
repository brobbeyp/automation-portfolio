import json, sys
from pathlib import Path


index = {
    "AGENTS.md": "Instructions applicable to work under this folder.",
    "PROGRESS.md": "Project checkpoint, recent evidence, and next steps.",
}


def loadCase(
    caseFileName,
):  # loads a JSON case document as an object, accepts file name in same cwd, single cases return an object, multiple cases return a list of objects
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


def generateContextString(
    paths,
):  # Accepts a list of paths and generates a string including each path and it's purpose
    if paths == []:
        return "No context files found within the Workspace boundary."

    result = "Session context discovered, nearest folder first:"
    for path in paths:
        result += "\n\n" + path

        if Path(path).name in index:
            result += "\nPurpose: " + index[Path(path).name]

    return result


def buildSessionStartResponse(event):
    sessionStartResponse = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": None,
        }
    }
    cwd = event["cwd"]
    sessionStartResponse["hookSpecificOutput"]["additionalContext"] = (
        generateContextString(generateContext(cwd))
    )
    return sessionStartResponse


def testGenerateContext(
    filename,
):  # Accepts either a single cast as a dict or multiple cases as a list and outputs a list of paths by running generateContext
    load = loadCase(filename)  # Select a case/cases to load
    if type(load) == dict:  # Handles single cases
        caseCWD = load["cwd"]  # Select the current working directory

        return generateContext(
            caseCWD
        )  # Pass the cwd str to workspaceContext, which returns a list of path strings

    elif type(load) == list:  # Handles multiple cases in a list
        result = []
        for case in load:
            result += generateContext(case["cwd"])
        return result


def testGenerateContextString(filename):
    context = testGenerateContext(filename)
    return generateContextString(context)


if __name__ == "__main__":


# SOURCE_HONESTY_RUN

## Description
- Compares the result of a grader on two cases and their expected source-honesty label.

## Prequisites
- Python
- `openai` package
- `httpx2` package


## Command
- Run from the Tutor project folder
```
python .\source_honesty_eval.py
```

## Expected output
```
MATCH
MISMATCH
```

## Stub Selection
- Select a failure stub by changing `grade_function = ` 
- Current stub functions include `stub_grade` and `stub_grade_failure`.
- Selecting `stub_grade` should produce an output of: 
```
MATCH
MISMATCH
```
- Selecting `stub_grade_failure` should produce an output of:
```
ERROR API status: 503
MISMATCH
```

## Live mode requirements
- OPENAI_API_KEY environment variable set
- source_honesty_prompt.txt in the same folder
- `grade_function = request_grade`
- Network access
- Spending approval for API calls

## Limits
- Does not handle errors other than ValueError, APIConnectionError, and APIStatusError
- Offline runs test comparison and error handling, not grader accuracy. The earlier live run agreed with two reference labels; this does not establish broad accuracy. The script assumes the human-written expected labels are correct.
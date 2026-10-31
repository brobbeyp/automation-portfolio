from content_type_check import require_json_content_type

# Success Tests
assert require_json_content_type("application/json") == "application/json"
assert (
    require_json_content_type(" Application/JSON ; charset=utf-8 ")
    == "application/json"
)

# Expected-Error Tests
try:
    require_json_content_type("text/html")
except ValueError as error:
    print("HTML rejected: ", error)
else:
    raise AssertionError("Failed Expected-Error Test for 'text/html'")

try:
    require_json_content_type("")
except ValueError as error:
    print("Missing header rejected:", error)
else:
    raise AssertionError("Failed Expected-Error Test for ''")

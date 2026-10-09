import json
from session_07 import classify_tickets
from post_adapter import post_to_ticket
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from content_type_check import require_json_content_type

try:
    url = "https://jsonplaceholder.typicode.com/posts/1"

    with urlopen(url, timeout=10) as response:
        status = response.status
        print("HTTP Status is: ", status)

        content_type = response.headers.get("Content-Type", "")
        print("Content-Type is: ", content_type)
        media_type = require_json_content_type(content_type)

        post = json.load(response)


except HTTPError as error:  # Catch HTTPErrors like 404
    print("HTTP request failed:", error.code, error.reason)
except URLError as error:  # Catch connection disconnect
    print("Connection failed:", error.reason)
except TimeoutError as error:  # Catch timeout errors
    print("Network operation timed out:", error)
except json.JSONDecodeError as error:  # Catch invalid JSON
    print("Response contains invalid JSON:", error)
else:
    print("This post's type is: ", type(post), "\nThis post's content is: ", post)

    try:
        result = [post_to_ticket(post)]  # Mapping
    except ValueError as error:
        print("Invalid post data:", error)
    else:
        print("Results: ", result)

        classified_tickets = classify_tickets(result)  # Classification
        print("Tickets after classification are: ", classified_tickets)

from urllib.request import urlopen
import json
from content_type_check import require_json_content_type

url = "https://jsonplaceholder.typicode.com/posts/1"
with urlopen(url, timeout=10) as response:
    status = response.status
    print("HTTP Status is: ", status)

    content_type = response.headers.get("Content-Type", "")
    print("Content-Type is: ", content_type)
    media_type = require_json_content_type(content_type)

    post = json.load(response)


print("This post's type is: ", type(post), "\nThis post's content is: ", post)

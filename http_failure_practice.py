import json
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    url = "https://jsonplaceholder.typicode.com/posts/999999"
    with urlopen(url, timeout=10) as response:
        print(response.status)
        print(response.headers.get("Content-Type"))

        post = json.load(response)

    print("This post's type is: ", type(post), "\nThis post's content is: ", post)
except HTTPError as error:
    print(error.code, error.reason)

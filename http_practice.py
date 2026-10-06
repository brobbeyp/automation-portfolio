from urllib.request import urlopen
import json

url = "https://jsonplaceholder.typicode.com/posts/1"
with urlopen(url, timeout=10) as response:
    print(response.status)
    print(response.headers.get("Content-Type"))

    post = json.load(response)

print(type(post), post)

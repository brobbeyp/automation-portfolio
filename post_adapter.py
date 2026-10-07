
def post_to_ticket(post):
    required_fields = ["id", "body"]

    if not isinstance(post, dict):
        raise ValueError("Post is not a 'dict'")

    field_check = [field in post for field in required_fields]
    if False in field_check:
        raise ValueError("A required field is missing")

    if not isinstance(post["id"], int) or isinstance(post["id"], bool):
        raise ValueError("Post 'id' must be an integer")

    if not isinstance(post["body"], str):
        raise ValueError("Post 'body' must be a string")

    result = {
        "id": "T-" + str(post["id"]),
        "message": post["body"],
    }

    return result

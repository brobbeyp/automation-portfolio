def require_json_content_type(content_type):
    media_type = content_type.split(";")[0]
    media_type = media_type.strip().lower()
    if not media_type == "application/json":
        raise ValueError("The Content-Type is not JSON")
    else:
        return media_type

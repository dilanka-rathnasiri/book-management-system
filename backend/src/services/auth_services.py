from fastapi import Request


def validate_request(request: Request) -> bool:
    if "authorization" in request.headers:
        auth_header = request.headers["authorization"]
    elif "Authorization" in request.headers:
        auth_header = request.headers["Authorization"]
    else:
        return False

    if auth_header == "Bearer dilanka":
        return True

    return False

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class AuthorizationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "authorization" in request.headers:
            auth_header = request.headers["authorization"]
        elif "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
        else:
            return Response(
                status_code=401,
                content='{"message": "Unauthorized"}',
                media_type="application/json",
            )

        if auth_header == "Bearer dilanka":
            response = await call_next(request)
            return response

        return Response(
            status_code=401,
            content='{"message": "Unauthorized"}',
            media_type="application/json",
        )

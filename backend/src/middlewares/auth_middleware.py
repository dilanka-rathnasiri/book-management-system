from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from services import auth_services, file_services


class AuthorizationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Skip authorization for auth controller endpoints
        skip_urls: list[str] = [
            "/auth/validate",
            "/",
        ]

        # add static file routes to skip list
        skip_urls.extend(file_services.get_static_file_routes())

        if request.url.path in skip_urls:
            response = await call_next(request)
            return response

        if auth_services.validate_request(request):
            response = await call_next(request)
            return response

        return Response(
            status_code=401,
            content='{"message": "Unauthorized"}',
            media_type="application/json",
        )

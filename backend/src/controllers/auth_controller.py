from fastapi import APIRouter, Request, Response

from services import auth_services

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/validate")
async def get_books(request: Request) -> Response:
    if auth_services.validate_request(request):
        return Response(
            status_code=200,
            content='{"message": "authorized"}',
            media_type="application/json",
        )
    return Response(
        status_code=401,
        content='{"message": "Unauthorized"}',
        media_type="application/json",
    )

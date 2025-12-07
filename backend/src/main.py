import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from controllers.auth_controller import auth_router
from controllers.book_controller import book_router
from middlewares.auth_middleware import AuthorizationMiddleware
from utils.logger import get_logger


def main() -> None:
    if "SERVER_PORT" in os.environ:
        server_port = int(os.environ["SERVER_PORT"])
    else:
        server_port = 8000

    # Initialize the custom logger
    get_logger()

    app: FastAPI = FastAPI()

    app.add_middleware(AuthorizationMiddleware)

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router)
    app.include_router(book_router)

    # Mount static files
    app.mount("/", StaticFiles(directory="static", html=True), name="static")

    uvicorn.run(app, host="0.0.0.0", port=server_port, log_config=None)


if __name__ == "__main__":
    main()

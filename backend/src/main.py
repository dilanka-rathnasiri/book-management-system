import os
from typing import Dict

import uvicorn
from fastapi import FastAPI

from controllers.book_controller import book_router
from middlewares.auth_middleware import AuthorizationMiddleware


def main() -> None:
    if "SERVER_PORT" in os.environ:
        server_port = int(os.environ["SERVER_PORT"])
    else:
        server_port = 8000

    app: FastAPI = FastAPI()

    app.add_middleware(AuthorizationMiddleware)
    app.include_router(book_router)
    uvicorn.run(app, host="0.0.0.0", port=server_port, log_config=None)


if __name__ == "__main__":
    main()

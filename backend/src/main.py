import uvicorn
from fastapi import FastAPI

from connections.Db import Db
from controllers.book_controller import book_router
from utils.logger import logger as logging


def main() -> None:
    Db.init()
    Db.create_tables()  # todo: try to remove this later
    try:
        app: FastAPI = FastAPI()

        # app.add_middleware(AuthorizationMiddleware)
        app.include_router(book_router)
        uvicorn.run(app, host="0.0.0.0", log_config=None)
    except Exception as e:
        logging.exception(e)
    finally:
        Db.close()


if __name__ == "__main__":
    main()

import os


class Configs:
    host: str = os.environ["HOST"]
    port: int = int(os.environ["PORT"])
    username: str = os.environ["USERNAME"]
    password: str = os.environ["PASSWORD"]
    database: str = os.environ["DATABASE"]
    db_url: str = f"postgresql+psycopg://{username}:{password}@{host}:{port}/{database}"

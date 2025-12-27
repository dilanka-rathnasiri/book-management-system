from sqlmodel import Session, SQLModel, create_engine

from services.config_services import Configs


class Db:
    @classmethod
    def init(cls):
        """Initialize PostgresSQL database connection and SQLModel engine"""

        cls.__engine = create_engine(Configs.db_url, echo=True)

    @classmethod
    def create_tables(cls):
        """Create all database tables from SQLModel metadata"""
        SQLModel.metadata.create_all(cls.__engine)

    @classmethod
    def get_new_session(cls) -> Session:
        """Return database connection for working with the database"""
        return Session(cls.__engine)

    @classmethod
    def close(cls):
        """Close all database connections and SQLModel engines"""
        cls.__engine.dispose()

from sqlmodel import Field, SQLModel


class BookORM(SQLModel, table=True):
    __tablename__ = "book"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    author: str
    year: int
    category: str

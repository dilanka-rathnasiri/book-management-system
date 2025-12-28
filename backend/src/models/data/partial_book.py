from pydantic import BaseModel


class PartialBook(BaseModel):
    """Partial model for book updates - all fields are optional"""

    title: str | None = None
    description: str | None = None
    author: str | None = None
    year: int | None = None
    category: str | None = None

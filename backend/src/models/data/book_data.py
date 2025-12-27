from pydantic import BaseModel


class BookData(BaseModel):
    id: int
    title: str
    description: str
    author: str
    year: int
    category: str

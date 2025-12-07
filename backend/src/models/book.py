from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    description: str
    author: str
    year: int
    category: str

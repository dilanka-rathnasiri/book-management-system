import json

from fastapi import APIRouter, Response

from models.book import Book

book_router = APIRouter()


@book_router.get("/books")
async def get_books() -> Response:
    books = [
        Book(
            id=1,
            title="The Great Gatsby",
            description="A classic American novel",
            author="F. Scott Fitzgerald",
            year=1925,
            category="Fiction",
        ),
        Book(
            id=2,
            title="To Kill a Mockingbird",
            description="A story of racial injustice",
            author="Harper Lee",
            year=1960,
            category="Fiction",
        ),
        Book(
            id=3,
            title="1984",
            description="A dystopian social science fiction novel",
            author="George Orwell",
            year=1949,
            category="Science Fiction",
        ),
        Book(
            id=4,
            title="Pride and Prejudice",
            description="A romantic novel of manners",
            author="Jane Austen",
            year=1813,
            category="Romance",
        ),
    ]

    return Response(
        status_code=200,
        content=json.dumps([book.model_dump() for book in books]),
        media_type="application/json",
    )

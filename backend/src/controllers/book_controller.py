from fastapi import APIRouter, HTTPException

import services.book_services as book_services
from models.data.book_data import BookData
from models.data.partial_book import PartialBook

book_router = APIRouter()


@book_router.get("/books")
async def get_books() -> list[BookData]:
    return book_services.get_all_books()


@book_router.get("/books/{book_id}")
async def get_book_by_id(book_id: int) -> BookData:
    book = book_services.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.post("/books")
async def add_new_book(partial_book: PartialBook) -> BookData:
    return book_services.create_book(partial_book)


@book_router.put("/books/{book_id}")
async def update_book(book_id: int, partial_book: PartialBook) -> BookData:
    updated_book = book_services.update_book(book_id, partial_book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@book_router.delete("/books/{book_id}")
async def delete_book(book_id: int) -> BookData:
    deleted_book = book_services.delete_book(book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book

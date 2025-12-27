from sqlmodel import select

from connections.Db import Db
from models.data.book_data import BookData
from models.orm.book_orm import BookORM


def get_all_books() -> list[BookData]:
    """Get all books from database"""
    with Db.get_new_session() as session:
        stmt = select(BookORM)
        results = session.exec(stmt)

        return [
            BookData(
                id=result.id,
                title=result.title,
                description=result.description,
                author=result.author,
                year=result.year,
                category=result.category,
            )
            for result in results
        ]


def get_book_by_id(book_id: int) -> BookData | None:
    """Get a specific book by ID"""
    with Db.get_new_session() as session:
        result = session.get(BookORM, book_id)

        if not result:
            return None

        return BookData(
            id=result.id,
            title=result.title,
            description=result.description,
            author=result.author,
            year=result.year,
            category=result.category,
        )


def create_book(book: BookData) -> BookData:
    """Create a new book"""
    with Db.get_new_session() as session:
        book_orm = BookORM(
            title=book.title,
            description=book.description,
            author=book.author,
            year=book.year,
            category=book.category,
        )
        session.add(book_orm)
        session.commit()
        session.refresh(book_orm)

        return BookData(
            id=book_orm.id,
            title=book_orm.title,
            description=book_orm.description,
            author=book_orm.author,
            year=book_orm.year,
            category=book_orm.category,
        )


def update_book(book_id: int, book: BookData) -> BookData | None:
    """Update an existing book"""
    with Db.get_new_session() as session:
        result = session.get(BookORM, book_id)

        if not result:
            return None

        result.title = book.title
        result.description = book.description
        result.author = book.author
        result.year = book.year
        result.category = book.category
        session.commit()

        return book


def delete_book(book_id: int) -> BookData | None:
    """Delete a book"""
    with Db.get_new_session() as session:
        book_orm = session.get(BookORM, book_id)

        if not book_orm:
            return None

        book = BookData(
            id=book_orm.id,
            title=book_orm.title,
            description=book_orm.description,
            author=book_orm.author,
            year=book_orm.year,
            category=book_orm.category,
        )
        session.delete(book_orm)
        session.commit()
        return book

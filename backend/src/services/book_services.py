from sqlmodel import select

from connections.Db import Db
from models.data.book_data import BookData
from models.data.partial_book import PartialBook
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


def create_book(partial_book: PartialBook) -> BookData:
    """Create a new book"""
    with Db.get_new_session() as session:
        book_orm = BookORM(
            title=partial_book.title,
            description=partial_book.description,
            author=partial_book.author,
            year=partial_book.year,
            category=partial_book.category,
        )
        session.add(book_orm)
        session.commit()
        session.refresh(book_orm)

        # todo: try to simplify
        return BookData(
            id=book_orm.id,
            title=book_orm.title,
            description=book_orm.description,
            author=book_orm.author,
            year=book_orm.year,
            category=book_orm.category,
        )


def update_book(book_id: int, partial_book: PartialBook) -> BookData | None:
    """Update an existing book"""
    with Db.get_new_session() as session:
        book_orm = session.get(BookORM, book_id)

        if not book_orm:
            return None

        book_orm.title = partial_book.title
        book_orm.description = partial_book.description
        book_orm.author = partial_book.author
        book_orm.year = partial_book.year
        book_orm.category = partial_book.category
        session.commit()
        session.refresh(book_orm)

        # todo: try to simplify
        return BookData(
            id=book_orm.id,
            title=book_orm.title,
            description=book_orm.description,
            author=book_orm.author,
            year=book_orm.year,
            category=book_orm.category,
        )


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

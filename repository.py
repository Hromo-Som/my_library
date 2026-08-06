from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.books import BookModel
from schemas.books import SBookAdd


class BookRepository:

    @classmethod
    async def book_add(cls,
                       book_data: SBookAdd,
                       session: AsyncSession) -> BookModel:
        book_dict = book_data.model_dump()
        book_model = BookModel(**book_dict)
        session.add(book_model)
        await session.commit()
        await session.refresh(book_model)
        return book_model

    @classmethod
    async def get_all_books(cls, session: AsyncSession):
        query = select(BookModel)
        res = await session.execute(query)
        books = res.scalars().all()
        return books

    @classmethod
    async def get_book(cls, book_id: int, session: AsyncSession):
        query = select(BookModel).where(BookModel.id == book_id)
        res = await session.execute(query)
        book = res.scalars().first()
        return book

    @classmethod
    async def update_book(cls,
                          book_id: int,
                          book_data: SBookAdd,
                          session: AsyncSession):
        query = select(BookModel).where(BookModel.id == book_id)
        res = await session.execute(query)
        book = res.scalars().first()
        book_dict = book_data.model_dump()
        for item, value in book_dict.items():
            setattr(book, item, value)
        return book

    @classmethod
    async def delete_book(cls, book_id: int, session: AsyncSession):
        query = delete(BookModel).where(BookModel.id == book_id)
        await session.execute(query)
        await session.commit()

from fastapi import APIRouter, HTTPException, status

from database import SessionDep
from repository import BookRepository
from schemas.books import SBook, SBookAdd


router = APIRouter(prefix='/books', tags=['Книги'])


@router.post('', response_model=SBook, status_code=status.HTTP_201_CREATED)
async def add_book(book: SBookAdd, session: SessionDep):
    try:
        book_model = await BookRepository.book_add(book, session)
        return book_model
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e))


@router.get('', response_model=list[SBook], status_code=status.HTTP_200_OK)
async def get_all_books(session: SessionDep):
    try:
        books = await BookRepository.get_all_books(session)
        return books
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e))


@router.get('/{id}', response_model=SBook, status_code=status.HTTP_200_OK)
async def get_book(id: int, session: SessionDep):
    try:
        book = await BookRepository.get_book(id, session)
        return book
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Книга с id = {id} не найдена')


@router.put('/{id}', response_model=SBook, status_code=status.HTTP_200_OK)
async def update_book(id: int, book: SBookAdd, session: SessionDep):
    try:
        book_model = await BookRepository.update_book(id, book, session)
        return book_model
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Книга с id = {id} не найдена')


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int, session: SessionDep) -> None:
    try:
        await BookRepository.delete_book(id, session)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Книга с id = {id} не найдена')

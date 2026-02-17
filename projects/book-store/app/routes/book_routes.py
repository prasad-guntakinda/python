from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book_schema import BookCreate
from app.services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.add_book(db, book)

@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return book_service.list_books(db)

@router.delete("/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    return book_service.remove_book(db, book_id)

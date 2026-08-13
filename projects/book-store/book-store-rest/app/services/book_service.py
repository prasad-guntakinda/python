from sqlalchemy.orm import Session
from app.repository import book_repo

def add_book(db: Session, book):
    return book_repo.create_book(db, book)

def list_books(db: Session):
    return book_repo.get_all_books(db)

def remove_book(db: Session, book_id: int):
    return book_repo.delete_book(db, book_id)

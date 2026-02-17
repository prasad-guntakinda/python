
from sqlalchemy.orm import Session
from app.models.book import Book

def create_book(db: Session, book):
    obj = Book(**book.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def delete_book(db: Session, book_id: int):
    obj = db.query(Book).filter(Book.id == book_id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

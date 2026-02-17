from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    price: int
    stock: int

class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True

from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel
app = FastAPI()

class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    published_date: str

class BookRead(BaseModel):
    id: int
    title: str
    author: str
    published_date: str

    class Config:
        orm_mode = True

@app.post("/books", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = model.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books", response_model=list[BookRead])
def get_books(db: Session = Depends(get_db)):
    books = db.query(model.Book).all()
    return books
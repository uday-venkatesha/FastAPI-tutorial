from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

app=FastAPI()

books= [
    {"id":1, "title": "Book 1", "author": "Author 1", "year": 2021},
    {"id":2, "title": "Book 2", "author": "Author 2", "year": 2020},
    {"id":3, "title": "Book 3", "author": "Author 3", "year": 2019}
]

@app.get("/book")
def read_books():
    return books


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    
@app.post("/book")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

@app.get("/book/{book_id}")
def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
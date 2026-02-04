from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "uday"}

@app.get("/print")
def print_message():
    return {"message": "This is a printed message"}

@app.get("/print/{name}")
def print_name(name: str):
    return {"message": f"This is a printed message for {name}"}

@app.get("/greet/")
def greet_name(name: str, age: Optional[int] = None):
    return {"Messeage": f"Hello {name} and you are {age} years old"}


class books(BaseModel):
    title: str
    author: str
    year: int
    
@app.post("/books/")
def create_book(book: books):
     return {
        "title": book.title,
        "author": book.author,
        "year": book.year
    }
     
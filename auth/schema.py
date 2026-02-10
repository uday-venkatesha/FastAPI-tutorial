from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str
class UserLogin (BaseModel):
    username: str
    password: str
    


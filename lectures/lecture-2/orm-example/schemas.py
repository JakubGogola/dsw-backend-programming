from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UserBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Updated from orm_mode which is deprecated

class ErrorResponse(BaseModel):
    detail: str

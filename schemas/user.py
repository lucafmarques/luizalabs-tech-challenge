from typing import List

from pydantic import BaseModel, EmailStr
from uuid import uuid4, UUID

from .product import Product

class UserBase(BaseModel):
    email: EmailStr

class UserUpdate(UserBase):
    email: EmailStr = EmailStr("")
    username: str = ""

    class Config:
        orm_mode = True

class User(UserBase):
    username: str
    favorites: List[Product] = []

    class Config:
        orm_mode = True
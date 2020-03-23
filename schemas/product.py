from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str
    image: str
    price: str

    class Config:
        orm_mode = True
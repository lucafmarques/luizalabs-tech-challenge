from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str
    image: str
    price: float

    class Config:
        orm_mode = True
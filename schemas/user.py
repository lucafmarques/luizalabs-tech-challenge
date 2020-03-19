from pydantic import BaseModel, EmailStr, UUID4
from uuid import uuid4, UUID

class UserBase(BaseModel):
    id: UUID
    username: str
    email: EmailStr
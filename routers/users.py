from fastapi import APIRouter, HTTPException
from schemas.user import UserBase

router = APIRouter()

@router.get("/")
async def get_users():
    return [{
        "id": "1",
        "username": "lucafmarques",
        "email": "lucafmarqs@gmail.com"
    }]

@router.post("/new")
def new_user(user: UserBase):
    return user


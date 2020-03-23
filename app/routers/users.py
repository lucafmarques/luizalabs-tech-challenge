from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.product import Product
from schemas.user import User, UserUpdate
from models.user import get_user_by_email, create_user, delete_user, update_user_info, get_users, remove_user_favorites

from utils.utils import db_session, valid_product

router = APIRouter()

@router.get("/")
async def all_users(db: Session = Depends(db_session)):
    return get_users(db)

@router.post("/", response_model=User)
async def new_user(user: User, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        return JSONResponse({
            "message": "Email already registered.",
        }, status_code=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(
        create_user(db, user).json(),
        status_code=status.HTTP_201_CREATED)

@router.get("/{email}", response_model=User)
async def get_user(email: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, email)
    if db_user is None:
        return JSONResponse({
            "message": "No user with that email.",
        }, status_code=status.HTTP_400_BAD_REQUEST)
    
    user = {
        "uuid": str(db_user.uuid),
        "email": db_user.email,
        "username": db_user.username,
        "favorites": db_user.favorites,
    }

    return JSONResponse(user, status_code=status.HTTP_200_OK)

@router.patch("/{email}", response_model=User)
async def update_user(email: str, user: UserUpdate, db: Session = Depends(db_session)):
    user, ok = update_user_info(db, email, user)
    if not ok: 
        return JSONResponse({
            "message": "Couldn't update user info."
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return JSONResponse(
        user.json(),
        status_code=status.HTTP_200_OK)


@router.delete("/{email}")
async def remove_user(email: str, db: Session = Depends(db_session)):
    msg, ok = delete_user(db, email)
    if not ok:
        return JSONResponse({
            "message": "Operation failed.",
            "error": msg,
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return JSONResponse({
        "message": msg,
    }, status_code=status.HTTP_200_OK)
    
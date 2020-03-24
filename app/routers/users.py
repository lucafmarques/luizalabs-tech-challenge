from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from schemas.user import User, UserUpdate
from models.user import get_user_by_email, create_user, delete_user, update_user_info, get_users, remove_user_favorites
from utils.utils import db_session, valid_product

router = APIRouter()

@router.get("/")
async def all_users(db: Session = Depends(db_session)):
    return await get_users(db)

@router.post("/", response_model=User)
async def new_user(user: User, db: Session = Depends(db_session)):
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        return JSONResponse({
            "msg": "Email already registered.",
        }, status_code=status.HTTP_400_BAD_REQUEST)

    new_user = await create_user(db, user)
    return JSONResponse(
        new_user.json(),
        status_code=status.HTTP_201_CREATED)

@router.get("/{user_email}", response_model=User)
async def get_user(user_email: str, db: Session = Depends(db_session)):
    db_user = await get_user_by_email(db, user_email)
    if db_user is None:
        return JSONResponse({
            "msg": "No user with that email.",
        }, status_code=status.HTTP_400_BAD_REQUEST)

    for id in db_user.favorites:
        product_data, ok = valid_product(id)
        if not ok:
            remove_user_favorites(db, db_user, id)
            continue
    
    user = {
        "uuid": str(db_user.uuid),
        "email": db_user.email,
        "username": db_user.username,
        "favorites": db_user.favorites,
    }

    return JSONResponse(user, status_code=status.HTTP_200_OK)

@router.patch("/{user_email}", response_model=User)
async def update_user(user_email: str, user: UserUpdate, db: Session = Depends(db_session)):
    user, ok = await update_user_info(db, user_email, user)
    if not ok: 
        return JSONResponse({
            "msg": "Couldn't update user info."
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return JSONResponse(
        user.json(),
        status_code=status.HTTP_200_OK)


@router.delete("/{user_email}")
async def remove_user(user_email: str, db: Session = Depends(db_session)):
    msg, ok = await delete_user(db, user_email)
    if not ok:
        return JSONResponse({
            "msg": "Operation failed.",
            "err": msg,
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return JSONResponse({
        "msg": msg,
    }, status_code=status.HTTP_200_OK)
    
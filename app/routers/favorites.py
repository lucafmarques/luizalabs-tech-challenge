from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models.user import get_user_by_email, add_to_favorites, remove_user_favorites
from utils.utils import db_session, valid_product

router = APIRouter()

@router.post("/{user_email}/{product_id}")
async def add_favorite(user_email: str, product_id: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user_email)
    if db_user is None:
        return JSONResponse({
            "message": "User doesn't exist"
        }, status_code=status.HTTP_400_BAD_REQUEST)
    
    _, ok = valid_product(product_id) 
    if not ok:
        return JSONResponse({
            "message": "No product with that ID"
        }, status_code=status.HTTP_400_BAD_REQUEST)
    
    user, ok = add_to_favorites(db, db_user, product_id)
    if not ok:
        return JSONResponse({
            "message": "Operation failed"
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return JSONResponse({
        "message": "Item added to user favorites."
    }, status_code=status.HTTP_200_OK)

@router.get("/{user_email}")
async def get_favorites(user_email: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user_email)
    if db_user is None:
        return JSONResponse({
            "message": "User doesn't exist"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse({
        "uuid": str(db_user.uuid),
        "favorites": db_user.favorites
    }, status_code=status.HTTP_200_OK)

@router.delete("/{user_email}/{product_id}")
async def remove_favorite(user_email: str, product_id: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user_email)
    if db_user is None:
        return JSONResponse({
            "message": "User doesn't exist"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    remove_user_favorites(db, db_user, product_id)

    return JSONResponse({
        "message": "Item removed from user favorites."
    }, status_code=status.HTTP_200_OK)
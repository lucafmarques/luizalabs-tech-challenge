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
            "msg": "User doesn't exist"
        }, status_code=status.HTTP_400_BAD_REQUEST)
    
    _, ok = valid_product(product_id) 
    if not ok:
        return JSONResponse({
            "msg": "No product with that ID"
        }, status_code=status.HTTP_400_BAD_REQUEST)
    
    user, ok = add_to_favorites(db, db_user, product_id)
    if not ok:
        return JSONResponse({
            "msg": "Item already in user favorites."
        }, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse({
        "msg": "Item added to user favorites."
    }, status_code=status.HTTP_200_OK)

@router.get("/{user_email}")
async def get_favorites(user_email: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user_email)
    if db_user is None:
        return JSONResponse({
            "msg": "User doesn't exist"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    products = []
    for id in db_user.favorites:
        product_data, ok = valid_product(id)
        if not ok:
            remove_user_favorites(db, db_user, id)
            continue
        
        products.append(product_data)

    return JSONResponse({
        "email": db_user.email,
        "favorites": products
    }, status_code=status.HTTP_200_OK)

@router.delete("/{user_email}/{product_id}")
async def remove_favorite(user_email: str, product_id: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user_email)
    if db_user is None:
        return JSONResponse({
            "msg": "User doesn't exist"
        }, status_code=status.HTTP_400_BAD_REQUEST)

    remove_user_favorites(db, db_user, product_id)

    return JSONResponse({
        "msg": "Item removed from user favorites."
    }, status_code=status.HTTP_200_OK)
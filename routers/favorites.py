from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from models.user import get_user_by_email, add_to_favorites
from utils.utils import db_session, valid_product

router = APIRouter()

@router.post("/{user_email}/{product_id}")
async def add_favorite(user_email: str, product_id: str, db: Session = Depends(db_session)):
    db_user = get_user_by_email(db, user_email)
    if not db_user:
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
    
    return user.json()
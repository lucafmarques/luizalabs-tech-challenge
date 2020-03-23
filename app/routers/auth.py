from datetime import timedelta

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from config import config
from utils.auth import create_access_token, authenticate_user
from schemas.token import Token

ACCESS_TOKEN_EXPIRE = 30

router = APIRouter()

@router.post("/token")
async def gen_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(config.ADMIN, form_data.username, form_data.password)
    if not user:
        return JSONResponse({
            "msg": "No user with those credentials."
        }, status_code=status.HTTP_401_UNAUTHORIZED)
    
    token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    token = create_access_token(
        data={"sub": user.username},
        expires_delta=token_expire,
    )

    return JSONResponse({
        "access_token": token.decode("utf-8"),
        "token_type": "bearer"
    }, status_code=status.HTTP_201_CREATED)

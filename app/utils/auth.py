import jwt
from datetime import datetime, timedelta

from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from config import config, AuthUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def authenticate_user(user: AuthUser, username: str, password: str):
    if username != user.username or password != user.password:
        return False
    return user

def valid_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            return False
    except jwt.PyJWTError:
        return False
    
    return True
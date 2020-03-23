from fastapi import Depends, Header, FastAPI, HTTPException, status

from utils.utils import valid_token
from routers import users, auth, favorites
from db import db, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

async def auth_token(token: str = Header(...)):
    if not valid_token(token):
        raise HTTPException(status_code=400, detail="X-Token header is invalid.")

app.include_router(
    users.router,
    prefix="/users",
    # dependencies=[Depends(auth_token)],
    responses={
        404: {'error': 'Path not found'}
    }
)
app.include_router(
    favorites.router,
    prefix="/fav",
    responses={
        404: {'error': 'Path not found'}
    }
)
app.include_router(
    auth.router,
    prefix="/auth",
    responses={
        404: {'error': 'Path not found'}
    }
)

@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
from uuid import uuid4
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session
from schemas.user import UserUpdate, User as UserCreate
from .mutable import MutableList

from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), unique=True, nullable=False)
    username = Column(String, index=True)
    email = Column(String, index=True)
    favorites = Column(MutableList.as_mutable(ARRAY(String)))

    def json(self):
        return {
            "uuid": str(self.uuid),
            "email": self.email,
            "username": self.username,
            "favorites": self.favorites
        }


async def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


async def get_users(db: Session):
    return db.query(User).all()


async def create_user(db: Session, user: UserCreate):
    user = User(uuid=uuid4(), email=user.email, username=user.username, favorites=[])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def update_user_info(db: Session, email: str, user: UserUpdate):
    db_user = await get_user_by_email(db, email)
    if db_user is None:
        return None, False
    db_user.email = user.email or db_user.email
    db_user.username = user.username or db_user.username
    
    db.commit()
    db.refresh(db_user)
    
    return db_user, True


async def delete_user(db: Session, email: str):
    user = get_user_by_email(db, email)
    try:
        db.delete(user)
    except Exception as e:
        return e, False

    db.commit()
    return "User deleted.", True

async def add_to_favorites(db: Session, db_user: User, product: str):
    if product in db_user.favorites:
        return db_user, False
    
    db_user.favorites.append(product)
    db.commit()
    db.refresh(db_user) 
    
    return db_user, True

async def remove_user_favorites(db: Session, db_user: User, product: str):
    db_user.favorites.remove(product)
    db.commit()

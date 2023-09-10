from user.schemas import UserCreate
from sqlalchemy.orm.session import Session
from appcore.dbmodel import DbUser
from auth.hashing import Hash
from fastapi import HTTPException, status
from datetime import datetime

def create_user(db: Session, request: UserCreate):
    new_user = DbUser(
        username = request.username,
        username_h = request.username_h,
        email = request.email,
        password = Hash.bcrypt(request.password),
        role = "user",
        created_time = datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User {username} not found')
    return user
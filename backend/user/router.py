from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from user.schemas import UserDisplay, UserCreate
from appcore.db import get_db
from user.crud import create_user

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user_router.post('', response_model=UserDisplay)
def new_user(request: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, request)
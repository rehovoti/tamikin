from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    username_h: str
    email: str

class UserCreate(UserBase):
        password: str

class UserDisplay(UserBase):
    class Config():
        form_attributes = True

# User for PostDisplay
# class User(BaseModel):
#     username: str
#     class Config():
#         form_attributes = True

class UserAuth(BaseModel):
    id: int
    username: str
    username_h: str
    email: str

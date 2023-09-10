from fastapi.exceptions import HTTPException
from fastapi import status
from user.schemas import UserAuth

def assure_admin(user: UserAuth):
    if user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Admins only allowed to add products"
        )
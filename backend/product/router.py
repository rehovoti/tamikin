from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from product.schemas import ProductBase
from appcore.db import get_db
from product import crud as product_crud
from typing import List
import random
import string
import shutil
from user.schemas import UserAuth
from auth.oauth2 import get_current_user
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from appcore.helper import assure_admin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

product_router = APIRouter(
    prefix="/product",
    tags=["product"]
)

image_url_types = ['absolute', 'relative']

@product_router.post('', response_model=ProductBase)
def create_product(
    token: Annotated[str, Depends(oauth2_scheme)],
    request: ProductBase, 
    db: Session = Depends(get_db), 
    current_user: UserAuth = Depends(get_current_user)):
        assure_admin(current_user)
        if not request.image_url_type in image_url_types:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Parameter image_url_type can be 'absolute' or 'relative'"
                )
        return product_crud.create(db, request)

@product_router.get('/all', response_model=List[ProductBase])
def products(db: Session = Depends(get_db)):
    return product_crud.get_all(db)

@product_router.post('/image')
def upload_image(
    image: UploadFile = File(...), 
    current_user: UserAuth = Depends(get_current_user)):
        assure_admin(current_user)
        letters = string.ascii_letters
        rand_str = ''.join(random.choice(letters) for i in range(6))
        new = f'_{rand_str}.'
        filename = new.join(image.filename.rsplit('.', 1))
        path = f'images/{filename}'
        with open(path, "w+b") as buffer:
            shutil.copyfileobj(image.file, buffer)
        return {'filename': path}

@product_router.delete('/delete/{id}')
def delete(
    id: int, 
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user)):
        assure_admin(current_user)
        return product_crud.delete(db, id)
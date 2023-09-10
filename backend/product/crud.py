from product.schemas import ProductBase
from sqlalchemy.orm.session import Session
from appcore.dbmodel import DbProduct
import datetime
from fastapi import HTTPException, status

def create(db: Session, request: ProductBase):
    new_product = DbProduct(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        description = request.description,
        description_h = request.description_h,
        created_time = datetime.datetime.now(),
        title = request.title,
        title_h = request.title_h
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all(db: Session):
    return db.query(DbProduct).all()

def delete(db: Session, id: int):
    product = db.query(DbProduct).filter(DbProduct.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Product not found')
    db.delete(product)
    db.commit()
    return 'ok'
from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    title: str
    title_h: str
    image_url: str
    image_url_type: str
    description: str
    description_h: str
    
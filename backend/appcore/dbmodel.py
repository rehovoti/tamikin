from appcore.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    username_h = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)
    created_time = Column(DateTime)

class DbProduct(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    title_h = Column(String)
    image_url = Column(String)
    image_url_type = Column(String)
    description = Column(String)
    description_h = Column(String)
    created_time = Column(DateTime)


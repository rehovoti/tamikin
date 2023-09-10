from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:unix11@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
def get_db():
    try:
        yield session
    finally:
        session.close()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from appcore.db import engine, Base
from user.router import user_router
from auth.authentication import auth_router
from product.router import product_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(product_router)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)

Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
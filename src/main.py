from fastapi import FastAPI
from src import database
from src.routes import user_router

app = FastAPI()
database.create_database()

app.include_router(user_router.router)

from fastapi import FastAPI
from src import database
from src.routes import user_router
from src.routes import character_router

app = FastAPI()
database.create_database()

app.include_router(user_router.router)
app.include_router(character_router.router)

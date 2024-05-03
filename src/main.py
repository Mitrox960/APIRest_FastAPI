from fastapi import FastAPI
from src.application.interfaces.rest.user_controller import router as user_router
from src.settings import settings

app = FastAPI()

app.include_router(user_router, prefix=settings.api_v1_str)

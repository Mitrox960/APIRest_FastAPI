from fastapi import APIRouter
from src.controllers import user_controller
from src.models.usersModel import UserCreate, User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session

router = APIRouter()

@router.post("/create_account", response_model=User)
def create_account(user_create: UserCreate, db: Session = Depends(get_session)):
    return user_controller.create_account(user_create, db)
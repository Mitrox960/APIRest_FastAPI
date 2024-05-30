from fastapi import APIRouter
from src.controllers import user_controller
from src.models.usersModel import UserCreate, User
from src.models.charactersModel import Characters
from src.models.statsModel import Statistiques
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session

router = APIRouter()

@router.post("/create_account")
def create_account(user_create: UserCreate, character_create : Characters, stats : Statistiques, db: Session = Depends(get_session)):
    return user_controller.create_account(user_create, character_create, stats, db)

@router.get("/get_all_account")
def create_account(db: Session = Depends(get_session)):
    return user_controller.get_all_account(db)

@router.delete("/delete_account/{id}")
def delete_stats(id: int, db: Session = Depends(get_session)):
    return user_controller.delete_account(id, db)

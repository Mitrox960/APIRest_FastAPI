from fastapi import APIRouter
from src.controllers import character_controller
from src.models.charactersModel import CharacterCreate, Characters
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session

router = APIRouter()

@router.post("/create_character", response_model=Characters)
def create_account(character_create: CharacterCreate, db: Session = Depends(get_session)):
    return character_controller.create_character(character_create, db)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controllers import character_controller
from src.models.charactersModel import CharacterCreate, Characters
from src.database import get_session

router = APIRouter()

@router.post("/create_character", response_model=Characters)
def create_character(character_create: CharacterCreate, db: Session = Depends(get_session)):
    return character_controller.create_character(character_create, db)

@router.get("/get_character/{character_id}", response_model=Characters)
def get_character(character_id: int, db: Session = Depends(get_session)):
    return character_controller.get_character(character_id, db)

@router.delete("/delete_character/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_session)):
    return character_controller.delete_character(character_id, db)

@router.put("/update_character_name/{character_id}")
def update_character_name(character_id: int, new_name: str, db: Session = Depends(get_session)):
    return character_controller.update_character_name(character_id, new_name, db)
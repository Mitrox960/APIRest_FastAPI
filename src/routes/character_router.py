from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controllers import character_controller
from src.models.charactersModel import Characters
from src.models.statsModel import Statistiques
from src.database import get_session

router = APIRouter()

@router.post("/create_character", response_model=Characters)
def create_character(character_create: Characters, stats: Statistiques, db: Session = Depends(get_session)):
    return character_controller.create_character(character_create, stats, db)


@router.get("/get_all_character")
def get_all_character(db: Session = Depends(get_session)):
    return character_controller.get_all_character(db)

@router.get("/get_character/{character_id}")
def get_character(character_id: int, db: Session = Depends(get_session)):
    return character_controller.get_character(character_id, db)

@router.delete("/delete_character/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_session)):
    return character_controller.delete_character(character_id, db)

@router.put("/update_character_name/{character_id}")
def update_character_name(character_id: int, new_name: str, db: Session = Depends(get_session)):
    return character_controller.update_character_name(character_id, new_name, db)
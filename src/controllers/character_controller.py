from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.services.character_service import CharactersService
from src.models.charactersModel import CharacterCreate, Characters

def create_character(character_create: CharacterCreate, db: Session):
    # Gestion des erreurs HTTP (200, 404, 500)
    return CharactersService.create_character(db, character_create.name, character_create.gender, character_create.ethnic)

def get_character(character_id: int, db: Session):
    character = CharactersService.get_character(db, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

def delete_character(character_id: int, db: Session):
    character = CharactersService.delete_character(db, character_id)
    if character:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "Character deleted successfully"}

def update_character_name(character_id: int, new_name: str, db: Session):
    character = CharactersService.update_character_name(db, character_id, new_name)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "Character name updated successfully"}
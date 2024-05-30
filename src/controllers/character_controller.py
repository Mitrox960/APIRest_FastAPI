from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.services.characterServices.character_service import CharactersService
from src.services.statsServices.stats_services import StatsServices
from src.models.charactersModel import Characters
from src.models.statsModel import Statistiques

def create_character(character_create: Characters, stats : Statistiques, db: Session):
    character = CharactersService.create_character(
        db, 
        users_id=character_create.users_id,
        name=character_create.name, 
        gender=character_create.gender, 
        ethnic=character_create.ethnic
    )
    
    StatsServices.create_stats(
        db, 
        character_id=character.id,  
        vitality=stats.vitality, 
        spirit=stats.spirit, 
        endurance=stats.endurance, 
        strenght=stats.strenght, 
        dextirity=stats.dextirity, 
        intelligence=stats.intelligence, 
        faith=stats.faith, 
        chance=stats.chance
    )

    return character

def get_character(character_id: int, db: Session):
    character = CharactersService.get_character(db, character_id)
    stats = StatsServices.get_stats(db, character.id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character, stats
    

def delete_character(character_id: int, db: Session):

    character = CharactersService.get_character(db, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    CharactersService.delete_characters_by_user_id(db, character_id)
    StatsServices.delete_stats(db, character.id)
    return {"message": "Character deleted successfully"}

def update_character_name(character_id: int, new_name: str, db: Session):
    character = CharactersService.update_character_name(db, character_id, new_name)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "Character name updated successfully"}

def get_all_character(db: Session):
    return CharactersService.get_all_character(db)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.services.userServices.user_service import UserService
from src.services.characterServices.character_service import CharactersService
from src.services.statsServices.stats_services import StatsServices
from src.models.charactersModel import Characters
from src.models.statsModel import Statistiques

from src.models.usersModel import UserCreate


def create_account(user_create: UserCreate, character_create: Characters, stats : Statistiques, db):
    user = UserService.create_account(db, 
        user_create.email, 
        user_create.password)
   
    character = CharactersService.create_character(
        db, 
        users_id=user.id,
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

    return 

def get_all_account(db):
    return UserService.get_all_account(db)

def delete_account(user_id: int, db: Session):
    user = UserService.delete_account(db, user_id)
    CharactersService.delete_characters_by_user_id(db, user_id)
    if user:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"message": "User deleted successfully"}    
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.services.character_service import CharactersService
from src.models.charactersModel import CharacterCreate


def create_character(character_create: CharacterCreate, db):
    # Gestion des erreurs HTTP (200, 404, 500)
    return CharactersService.create_character(db, character_create.name, character_create.gender, character_create.ethnic)

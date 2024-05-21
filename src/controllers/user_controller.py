from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.services.user_service import UserService
from src.models.usersModel import UserCreate


def create_account(user_create: UserCreate, db):
    # Gestion des erreurs HTTP (200, 404, 500)
    return UserService.create_account(db, user_create.email, user_create.password)

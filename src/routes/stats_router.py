from fastapi import APIRouter
from src.controllers import statistiques_controller
from src.models.statsModel import Statistiques
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session

router = APIRouter()

@router.post("/create_stats", response_model=Statistiques)
def create_stats(stats: Statistiques, db: Session = Depends(get_session)):
    return statistiques_controller.create_stats(stats, db)

@router.post("/update_stats", response_model=Statistiques)
def create_stats(stats: Statistiques, db: Session = Depends(get_session)):
    return statistiques_controller.update_stats(stats, db)

@router.delete("/delete_stats/{id}")
def delete_stats(id: int, db: Session = Depends(get_session)):
    return statistiques_controller.delete_stats(id, db)

@router.get("/get_stats")
def get_stats(db: Session = Depends(get_session)):
    return statistiques_controller.get_stats(db)

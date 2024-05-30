from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_session
from src.services.statsServices.stats_services import StatsServices
from src.models.statsModel import Statistiques

def create_stats(stats : Statistiques, db):
    return StatsServices.create_stats(db, stats.vitality, stats.spirit, stats.endurance, stats.strenght, stats.dextirity, stats.intelligence, stats.faith, stats.chance)

def update_stats(stats : Statistiques, db):
    return StatsServices.update_stats(db, stats.id, stats.vitality, stats.spirit, stats.endurance, stats.strenght, stats.dextirity, stats.intelligence, stats.faith, stats.chance)

def delete_stats(stat_id : int, db):
    return StatsServices.delete_stats(db, stat_id)

def get_stats(db):
    return StatsServices.get_stats(db)
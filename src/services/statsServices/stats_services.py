from src.models.statsModel import Statistiques
from sqlmodel import Session, select

class StatsServices:
    @staticmethod
    def create_stats(
        db: Session, 
        character_id: int,
        vitality: int,
        spirit: int,
        endurance: int,
        strenght: int,
        dextirity: int,
        intelligence: int,
        faith: int,
        chance: int
        ) -> Statistiques:
        account = Statistiques(
        character_id = character_id,
        vitality=vitality, 
        spirit=spirit,
        endurance=endurance,
        strenght=strenght,
        dextirity=dextirity,
        intelligence=intelligence,
        faith=faith,
        chance=chance)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account


    
    @staticmethod
    def update_stats(
        db: Session, 
        id: int,
        vitality: int,
        spirit: int,
        endurance: int, 
        strenght: int,
        dextirity: int,
        intelligence: int,
        faith: int,
        chance: int
        ) -> Statistiques:
        stats = db.exec(select(Statistiques).where(Statistiques.id == id)).first()
        if not stats:
            raise ValueError("Statistiques not found")

        stats.vitality = vitality
        stats.spirit = spirit
        stats.endurance = endurance
        stats.strenght = strenght
        stats.dextirity = dextirity
        stats.intelligence = intelligence
        stats.faith = faith
        stats.chance = chance

        db.add(stats)
        db.commit()
        db.refresh(stats)

        return stats

        
    @staticmethod
    def delete_stats(
        db: Session,
        characters: list
    ):
        characters = db.exec(select(Statistiques).where(Statistiques.character_id == characters)).all()
        for character in characters:
            db.delete(character)
        db.commit()
        

        

    @staticmethod
    def get_stats(
        db: Session
    ) -> Statistiques:
        result = db.exec(select(Statistiques))
        characters = result.all()
        return characters


    
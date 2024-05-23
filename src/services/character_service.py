from src.models.charactersModel import Characters
from sqlmodel import Session

class CharactersService:
    @staticmethod
    def create_character(db: Session, name: str, gender: str, ethnic: str) -> Characters:
        # Logique métier
            # Pas de @ dupliqué
            # Password avec x catactères min...
        character = Characters(name=name, gender=gender, ethnic=ethnic)
        db.add(character)
        db.commit()
        db.refresh(character)
        return character

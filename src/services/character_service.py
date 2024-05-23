from src.models.charactersModel import Characters
from sqlmodel import Session

class CharactersService:
    @staticmethod
    def create_character(db: Session, name: str, gender: str, ethnic: str) -> Characters:
        # Logique métier
        # Pas de @ dupliqué
        # Password avec x caractères min...
        character = Characters(name=name, gender=gender, ethnic=ethnic)
        db.add(character)
        db.commit()
        db.refresh(character)
        return character

    @staticmethod
    def get_character(db: Session, character_id: int) -> Characters:
        character = db.get(Characters, character_id)
        return character

    @staticmethod
    def delete_character(db: Session, character_id: int) -> Characters:
        character = db.get(Characters, character_id)
        if character:
            db.delete(character)
            db.commit()
            
    @staticmethod
    def update_character_name(db: Session, character_id: int, new_name: str) -> Characters:
        character = db.get(Characters, character_id)
        if character:
            character.name = new_name
            db.commit()
            db.refresh(character)
            return character

 
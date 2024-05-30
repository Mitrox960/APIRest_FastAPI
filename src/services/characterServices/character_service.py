from src.models.charactersModel import Characters
from sqlmodel import Session, select

class CharactersService:
    @staticmethod
    def create_character(db: Session, users_id : int, name: str, gender: str, ethnic: str) -> Characters:
        character = Characters(users_id=users_id, name=name, gender=gender, ethnic=ethnic)
        db.add(character)
        db.commit()
        db.refresh(character)
        return character

    @staticmethod
    def get_character(db: Session, user_id: int) -> Characters:
        character = db.exec(select(Characters).where(Characters.users_id == user_id)).first()
        return character

            
    @staticmethod
    def delete_characters_by_user_id(db: Session, user_id: int):
        characters = db.exec(select(Characters).where(Characters.users_id == user_id)).all()
        if not characters:
            raise ValueError("No characters found for this user")
        for character in characters:
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

    @staticmethod
    def get_all_character(db: Session) -> Characters:
        result = db.exec(select(Characters))
        characters = result.all()
        return characters

 
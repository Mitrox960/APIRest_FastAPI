from src.models.usersModel import User
from sqlmodel import Session

class UserService:
    @staticmethod
    def create_account(db: Session, email: str, password: str) -> User:
        # Logique métier
            # Pas de @ dupliqué
            # Password avec x catactères min...
        account = User(email=email, password=password)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

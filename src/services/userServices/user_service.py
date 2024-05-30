from src.models.usersModel import User
from sqlmodel import Session, select

class UserService:
    @staticmethod
    def create_account(db: Session, email: str, password: str) -> User:
        account = User(email=email, password=password)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account
    
    @staticmethod
    def get_all_account(db: Session) -> User:
        result = db.exec(select(User))
        user = result.all()
        return user

    @staticmethod
    def delete_account(db: Session, user_id: int) -> User:
        user = db.get(User, user_id)
        if user:
            db.delete(user)
            db.commit()
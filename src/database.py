from sqlmodel import SQLModel, create_engine, Session, SQLModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_database():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_database()
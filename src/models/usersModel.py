from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

class UserCreate(SQLModel):
    email: str
    password: str
from typing import Optional
from sqlmodel import SQLModel, Field

class Characters(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    gender: str
    ethnic: str

    users_id: Optional[int] = Field(default=None, foreign_key="users.id")


from typing import Optional
from sqlmodel import SQLModel, Field

class Characters(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    password: str
    ethnic: str


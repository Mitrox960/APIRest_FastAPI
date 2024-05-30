from typing import Optional
from sqlmodel import SQLModel, Field

class Statistiques(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vitality: int
    spirit: int
    endurance: int
    strenght: int
    dextirity: int
    intelligence: int
    faith: int
    chance: int

    character_id: Optional[int] = Field(default=None, foreign_key="characters.id")


from pydantic import BaseModel
from typing import List

# --- Player ---
class PlayerBase(BaseModel):
    name: str
    score: int = 0

class PlayerCreate(PlayerBase):
    pass

class PlayerRead(PlayerBase):
    id: int

    class Config:
        from_attributes = True


# --- Question ---
class QuestionBase(BaseModel):
    text: str
    options: List[str]
    correct_index: int
    category: str
    difficulty: float

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int

    class Config:
        from_attributes = True


# --- Game ---
class GameBase(BaseModel):
    current_turn: int = 0
    state: str = "waiting"

class GameCreate(GameBase):
    pass

class GameRead(GameBase):
    id: int
    players: List[PlayerRead] = []
    questions: List[QuestionRead] = []

    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import List

# --- Player ---
class Player(BaseModel):
    name: str
    score: int = 0

class PlayerCreate(Player):
    pass

class PlayerRead(Player):
    id: int

    class Config:
        from_attributes = True


# --- Question ---
class Question(BaseModel):
    text: str
    options: List[str]
    correct_index: int
    category: str
    difficulty: float

class QuestionCreate(Question):
    pass

class QuestionRead(Question):
    id: int

    class Config:
        from_attributes = True


# --- Game ---
class Game(BaseModel):
    current_turn: int = 0
    state: str = "waiting"

class GameCreate(Game):
    pass

class GameRead(Game):
    id: int
    players: List[PlayerRead] = []
    questions: List[QuestionRead] = []

    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import List, Optional

# --- Player ---
class PlayerBase(BaseModel):
    name: str
    score: int = 0

class PlayerCreate(PlayerBase):
    pass

class PlayerOut(PlayerBase):
    id: int

    class Config:
        orm_mode = True

# --- Question ---
class QuestionBase(BaseModel):
    text: str
    options: List[str]
    correct_index: int
    category: Optional[str] = None
    difficulty: Optional[float] = None

class QuestionCreate(QuestionBase):
    pass

class QuestionOut(QuestionBase):
    id: int

class Config:
    from_attributes = True

# --- Game ---
class GameCreate(BaseModel):
    current_turn: int = 0
    state: str = "waiting"

class GameOut(BaseModel):
    id: int
    players: List[PlayerOut] = []
    current_turn: int
    state: str
    questions: List[QuestionOut] = []

    class Config:
        orm_mode = True

class GameUpdate(BaseModel):
    player_ids: Optional[List[int]] = None
    question_ids: Optional[List[int]] = None
    current_turn: Optional[int] = None
    state: Optional[str] = None
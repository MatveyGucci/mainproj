from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Integer, default=0)

    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="players")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    category = Column(String)
    difficulty = Column(Integer)
    correct_index = Column(Integer)
    options = Column(String)  # можно хранить как JSON-строку

    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="questions")


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    current_turn = Column(Integer, default=0)
    state = Column(String, default="waiting")

    players = relationship("Player", back_populates="game")
    questions = relationship("Question", back_populates="game")

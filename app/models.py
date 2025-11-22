from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.dialects.sqlite import JSON

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Integer, default=0)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    options = Column(String, nullable=False)   # храним варианты как строку
    correct_index = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    difficulty = Column(Float, nullable=False)


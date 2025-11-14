from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()

class PlayerModel(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Integer, default=0)
    game_id = Column(Integer, ForeignKey("games.id"))

class QuestionModel(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    options = Column(Text)  # JSON-строка
    correct_index = Column(Integer)
    category = Column(String)
    difficulty = Column(Integer)
    game_id = Column(Integer, ForeignKey("games.id"))

class GameModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    current_turn = Column(Integer, default=0)
    state = Column(String, default="waiting")

    players = relationship("PlayerModel", backref="game")
    questions = relationship("QuestionModel", backref="game")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

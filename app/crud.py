import random
from sqlalchemy.orm import Session
from . import models

# --- Players ---
def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()

def create_player(db: Session, player: models.Player):
    db.add(player)
    db.commit()
    db.refresh(player)
    return player
def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def get_questions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Question).offset(skip).limit(limit).all()

def get_random_question_by_category(db: Session, category: str):
    questions = db.query(models.Question).filter(models.Question.category == category).all()
    if not questions:
        return None
    q = random.choice(questions)
    # преобразуем строку обратно в список
    q.options = q.options.split(",")
    return q
def create_question(db: Session, question: models.Question):
    db.add(question)
    db.commit()
    db.refresh(question)
    return question
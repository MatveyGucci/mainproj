from sqlalchemy.orm import Session
from app.models import PlayerModel, QuestionModel, GameModel
def create_player(db: Session, name: str, score: int = 0):
    player = Player(name=name, score=score)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Player).offset(skip).limit(limit).all()

def create_question(db: Session, text: str, options: str, correct_index: int, category: str, difficulty: int):
    question = Question(text=text, options=options, correct_index=correct_index, category=category, difficulty=difficulty)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

def get_questions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Question).offset(skip).limit(limit).all()

def create_game(db: Session, state: str = "waiting", current_turn: int = 0):
    game = Game(state=state, current_turn=current_turn)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

def get_game(db: Session, game_id: int):
    return db.query(Game).filter(Game.id == game_id).first()

def get_games(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Game).offset(skip).limit(limit).all()
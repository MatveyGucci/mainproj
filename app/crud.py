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

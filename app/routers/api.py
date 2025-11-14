from fastapi import APIRouter, HTTPException
from typing import List
from models import Player, Question, Game

router = APIRouter()

# Пример хранилища игр
games = {}

@router.post("/games/", response_model=Game)
def create_game(game: Game):
    if game.id in games:
        raise HTTPException(status_code=400, detail="Game already exists")
    games[game.id] = game
    return game

@router.get("/games/{game_id}", response_model=Game)
def read_game(game_id: int):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    return games[game_id]

@router.get("/games/", response_model=List[Game])
def list_games():
    return list(games.values())

@router.delete("/games/{game_id}", response_model=Game)
def delete_game(game_id: int):
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    return games.pop(game_id)
from app.database import SessionLocal, engine
from app.models import Player, Question, Game
import pytest

@pytest.fixture(scope="module")
def test_db():
    # Create a new database session for testing
    db = SessionLocal()
    yield db
    db.close()

def test_create_player(test_db):
    player = Player(id=1, name="Test Player")
    test_db.add(player)
    test_db.commit()
    assert player.id == 1
    assert player.name == "Test Player"

def test_create_question(test_db):
    question = Question(
        id=1,
        text="What is the capital of France?",
        options=["Berlin", "Madrid", "Paris", "Rome"],
        correct_index=2,
        category="Geography",
        difficulty=1.0
    )
    test_db.add(question)
    test_db.commit()
    assert question.id == 1
    assert question.text == "What is the capital of France?"

def test_create_game(test_db):
    player1 = Player(id=1, name="Player One")
    player2 = Player(id=2, name="Player Two")
    game = Game(id=1, players=[player1, player2])
    test_db.add(game)
    test_db.commit()
    assert game.id == 1
    assert len(game.players) == 2

def test_player_score_update(test_db):
    player = test_db.query(Player).filter(Player.id == 1).first()
    player.score += 10
    test_db.commit()
    assert player.score == 10
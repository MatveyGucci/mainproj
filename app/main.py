from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app import models, schemas, crud
from app.database import SessionLocal, init_db

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Players ---
@app.post("/players/", response_model=schemas.PlayerRead)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = models.Player(name=player.name, score=player.score)
    return crud.create_player(db, db_player)

@app.get("/players/{player_id}", response_model=schemas.PlayerRead)
async def read_player(player_id: int, db: Session = Depends(get_db)):
    return crud.get_player(db, player_id)

@app.get("/players/", response_model=list[schemas.PlayerRead])
async def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_players(db, skip=skip, limit=limit)

@app.post("/questions/", response_model=schemas.QuestionRead)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    db_question = models.Question(
        text=question.text,
        options=",".join(question.options),  # сохраняем список как строку
        correct_index=question.correct_index,
        category=question.category,
        difficulty=question.difficulty
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@app.get("/questions/{question_id}", response_model=schemas.QuestionRead)
async def read_question(question_id: int, db: Session = Depends(get_db)):
    return crud.get_question(db, question_id)

@app.get("/questions/", response_model=list[schemas.QuestionRead])
async def read_questions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_questions(db, skip=skip, limit=limit)

@app.get("/questions/random/{category}", response_model=schemas.QuestionRead)
async def get_random_question(category: str, db: Session = Depends(get_db)):
    question = crud.get_random_question_by_category(db, category)
    if question is None:
        raise HTTPException(status_code=404, detail="No questions found for this category")
    return question
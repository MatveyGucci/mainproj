from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import SessionLocal, init_db

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Инициализация базы
init_db()

# Dependency
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
@app.post("/players/", response_model=schemas.PlayerOut)
async def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = models.PlayerModel(name=player.name, score=0)
    return crud.create_player(db, db_player)

@app.get("/players/{player_id}", response_model=schemas.PlayerOut)
async def read_player(player_id: int, db: Session = Depends(get_db)):
    return crud.get_player(db, player_id)

@app.get("/players/", response_model=list[schemas.PlayerOut])
async def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_players(db, skip=skip, limit=limit)
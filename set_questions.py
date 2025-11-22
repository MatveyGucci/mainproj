import json
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app import models

def load_questions_from_file(filename: str):
    # создаём таблицы, если их ещё нет
    init_db()
    db: Session = SessionLocal()
    with open(filename, "r", encoding="utf-8") as f:
        questions = json.load(f)
        for q in questions:
            db_question = models.Question(
                text=q["text"],
                options=",".join(q["options"]),  # список превращаем в строку
                correct_index=q["correct_index"],
                category=q["category"],
                difficulty=q["difficulty"]
            )
            db.add(db_question)
        db.commit()
    db.close()

if __name__ == "__main__":
    load_questions_from_file("questions_dataset.json")
    db = SessionLocal()
    from sqlalchemy import func
    results = db.query(models.Question.category, func.count(models.Question.id)).group_by(models.Question.category).all()
    for category, cnt in results:
        print(f"{category}: {cnt} questions")
    db.close()

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.db import crud, models, schemas
from app.db.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/polls/", response_model=List[schemas.Poll])
def read_polls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_polls(db, skip=skip, limit=limit)


@app.get("/polls/{poll_id}", response_model=schemas.Poll)
def read_poll(poll_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_poll(db, poll_id=poll_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Poll not found')
    return db_user

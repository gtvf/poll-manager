from typing import List
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status

from app.db import crud, schemas, models
from app.db.db import SessionLocal

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


def fake_hash_password(password: str):
    return "fakehashed" + password


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


def fake_decode_token(token):
    return schemas.User(username=token + "fakedecoded", email="john@example.com")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = Depends(get_db)
    user_dict = db.query(models.User).filter(models.User.username == form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

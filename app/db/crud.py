from sqlalchemy.orm import Session

from app.db import models, schemas


def get_poll(db: Session, poll_id: int):
    return db.query(models.Poll).filter(models.Poll.id == poll_id).first()


def get_polls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Poll).offset(skip).limit(limit).all()


def get_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()


def create_poll(db: Session, poll: schemas.Poll):
    db_poll = models.Poll(title=poll.title, description=poll.description)
    db.add(db_poll)
    db.commit()
    db.refresh(db_poll)
    return db_poll

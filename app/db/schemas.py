from typing import Optional, List

from pydantic import BaseModel


class Vote(BaseModel):
    poll_id: int
    answer_id: int

    class Config:
        orm_mode = True


class Answer(BaseModel):
    id: int
    text: str
    poll_id: int
    votes_count: int

    class Config:
        orm_mode = True


class Poll(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    answers: List[Answer]
    user_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    email: str
    password: str
    username: str

    class Config:
        orm_mode = True

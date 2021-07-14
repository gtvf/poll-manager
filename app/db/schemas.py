from typing import Optional

from pydantic import BaseModel


class Poll(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    answers: list

    class Config:
        orm_mode = True


class Answer(BaseModel):
    id: int
    text: str
    poll_id: int

    class Config:
        orm_mode = True


class Vote(BaseModel):
    poll_id: int
    answer_id: int

    class Config:
        orm_mode = True

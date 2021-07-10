from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    answers = relationship('Answer', back_populates='poll')


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    poll_id = Column(Integer, ForeignKey('polls.id'))

    poll = relationship('Poll', back_populates='answers')


class Vote(Base):
    __tablename__ = 'votes'

    poll_id = Column(Integer, ForeignKey('polls.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))

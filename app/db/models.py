from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.db import Base


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    answers = relationship('Answer', back_populates='poll')
    user = relationship('User', back_populates='polls')


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    poll_id = Column(Integer, ForeignKey('polls.id'))

    poll = relationship('Poll', back_populates='answers')
    votes = relationship('Vote', back_populates='answer')

    @property
    def votes_count(self):
        return len(self.votes)


class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, index=True)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))

    answer = relationship('Answer', back_populates='votes')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    username = Column(String)

    polls = relationship('Poll', back_populates='user')

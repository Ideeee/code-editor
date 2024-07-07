import datetime as dt

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Enum, Text, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp


class Question(Timestamp, Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(Text)
    test_cases = Column(ARRAY(String))
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False)

    topic = relationship("Topic", primaryjoin="and_(Topic.id == foreign(Question.topic_id))", back_populates="questions")


class Topic(Timestamp, Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))

    questions = relationship("Question", primaryjoin="and_(Topic.id == foreign(Question.topic_id))") #, viewonly=True)

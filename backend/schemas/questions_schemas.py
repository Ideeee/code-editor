from pydantic import BaseModel
from typing import Optional
from datetime import datetime






class QuestionBase(BaseModel):
    title: str
    body: str
    topic_id = int


class QuestionCreate(QuestionBase):
    test_cases: Optional[list[str]]


class Question(QuestionBase):
    id: int
    test_cases: list[str]
    topic_id = int
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True

class TopicBase(BaseModel):
    title: str


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    id: int
    questions: list[Question]
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True
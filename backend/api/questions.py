from typing import Union
import fastapi
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from services import questions_services
from models import questions_models
from schemas import questions_schemas
from db.db_setup import SessionLocal, engine, get_db


router = fastapi.APIRouter(tags=["Questions"])

@router.post("/questions", response_model=questions_schemas.Question)
async def create_question(
    question: questions_schemas.QuestionCreate,
    topic_id: int, 
    db: Session = Depends(get_db)
    ):

    # existing_student = student_services.get_student_by_username(db, username=student.username)
    # if existing_student:
    #     raise HTTPException(status_code=400, detail="A user with this username already exists")
    
    try:
        new_question = questions_services.create_question(db=db, question=question, topic_id=topic_id)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="This question already exists")
    except:
        raise HTTPException(status_code=400, detail="Could not create student. Check parameters")

    return new_question


@router.get("/questions", response_model=list[questions_schemas.Question])
async def get_questions(
    title: Union[str, None] = None,
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    if title:
        question = questions_services.get_question_by_title(db, title=title)

        if question is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        return question
    
    questions = questions_services.get_questions(db, skip=skip, limit=limit)
    return questions


@router.get("/questions/{id}", response_model=questions_schemas.Question)
async def get_question_by_id(
    user_id: int, 
    db: Session = Depends(get_db)
):
    question = questions_services.get_questions(db, user_id=user_id)

    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return question


@router.post("/topics", response_model=questions_schemas.Topic)
async def create_topic(
    topic: questions_schemas.TopicCreate, 
    db: Session = Depends(get_db)
    ):

    existing_topic = questions_services.get_topic_by_title(db, title=topic.title)
    if existing_topic:
        raise HTTPException(status_code=400, detail="This topic already exists")
    
    try:
        new_topic = questions_services.create_question(db=db, topic=topic)
    except:
        raise HTTPException(status_code=400, detail="Could not create topic. Check parameters")

    return new_topic

    

from sqlalchemy.orm import Session

from schemas import questions_schemas
from models import questions_models


def get_question(db: Session, question_id: int):
    return db.query(questions_models.Question).filter(questions_models.Question.id == question_id).first()


def get_question_by_title(db: Session, matric_no: str):
    return db.query(questions_models.Question).filter(questions_models.Question.matric_no == matric_no).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(questions_models.Question).offset(skip).limit(limit).all()


def create_question(db: Session, question: questions_schemas.QuestionCreate, topic_id: int):
    
    new_question = questions_models.Question(
        title=question.title, 
        body=question.body,
        topic_id=topic_id,
        department=question.department,
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return questions_schemas.Question.from_orm(new_question)


def create_topic(db: Session, topic: questions_schemas.TopicCreate):
    
    new_topic = questions_models.Topic(
        title=topic.title, 
    )

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return questions_schemas.Topic.from_orm(new_topic)


def get_topic_by_title(db: Session, title: str):
    return db.query(questions_models.Topic).filter(questions_models.Topic.title == title).first()


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(admin_model.Item).offset(skip).limit(limit).all()


# def create_admin_item(db: Session, item: schemas.ItemCreate, admin_id: int):
#     db_item = admin_model.Item(**item.dict(), owner_id=admin_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item



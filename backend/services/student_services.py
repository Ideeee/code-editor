from sqlalchemy.orm import Session

from schemas import student_schemas
from models import student_models


def get_student(db: Session, student_id: int):
    return db.query(student_models.Student).filter(student_models.Student.id == student_id).first()


def get_student_by_matric_no(db: Session, matric_no: str):
    return db.query(student_models.Student).filter(student_models.Student.matric_no == matric_no).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(student_models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: student_schemas.StudentCreate):
    
    new_student = student_models.Student(
        first_name=student.first_name, 
        last_name=student.last_name,
        matric_no=student.matric_no,
        department=student.department,
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return student_schemas.Student.from_orm(new_student)


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(admin_model.Item).offset(skip).limit(limit).all()


# def create_admin_item(db: Session, item: schemas.ItemCreate, admin_id: int):
#     db_item = admin_model.Item(**item.dict(), owner_id=admin_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item



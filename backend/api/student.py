from typing import Union
import fastapi
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from services import student_services
from models import student_models
from schemas import student_schemas
from db.db_setup import SessionLocal, engine, get_db


router = fastapi.APIRouter(tags=["Students"])

@router.post("/students", response_model=student_schemas.Student)
def create_student(
    student: student_schemas.StudentCreate, 
    db: Session = Depends(get_db)
    ):

    # existing_student = student_services.get_student_by_username(db, username=student.username)
    # if existing_student:
    #     raise HTTPException(status_code=400, detail="A user with this username already exists")
    
    try:
        new_student = student_services.create_student(db=db, student=student)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="A student with this matric number already exists")
    except:
        raise HTTPException(status_code=400, detail="Could not create student. Check parameters")

    
    return new_student


@router.get("/students", response_model=list[student_schemas.Student])
def get_students(
    matric_no: Union[str, None] = None,
    skip: int = 0, 
    limit: int = 100,
    db: Session = Depends(get_db)
):
    if matric_no:
        student = student_services.get_student_by_matric_no(db, matric_no=matric_no)

        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        return student
    
    students = student_services.get_students(db, skip=skip, limit=limit)
    return students

@router.get("/students/{id}", response_model=student_schemas.Student)
def get_student_by_id(
    user_id: int, 
    db: Session = Depends(get_db)
):
    student = student_services.get_user(db, user_id=user_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student


@router.post("/student/login", status_code=200, response_model=student_schemas.Student)
async def login(
    student: student_schemas.StudentBase, 
    db: Session = Depends(get_db)
):
    verified_student = student_services.get_student_by_matric_no(db=db, matric_no=student.matric_no)

    if verified_student is None:
        raise fastapi.HTTPException(status_code=403, detail="Invalid Credentials")
    
    verified = verified_student.last_name.lower() == student.last_name.lower()

    if not verified:
        raise fastapi.HTTPException(status_code=403, detail="Invalid Credentials")
    
    return verified_student

    

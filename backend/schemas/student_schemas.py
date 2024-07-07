from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GradesBase(BaseModel):
    score: int
    

class GradesCreate(GradesBase):
    student_id: int
    exam_id: int


class Grades(GradesCreate):
    id: int
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True
        

class StudentBase(BaseModel):
    matric_no: str
    last_name: str


class StudentCreate(StudentBase):
    first_name: str
    department: str


class Student(StudentBase):
    id: int
    # is_active: bool
    grades = list[Grades]
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True
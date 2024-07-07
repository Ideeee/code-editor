import datetime as dt
import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Enum, Text, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp



class Student(Timestamp, Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    matric_no = Column(String(50))
    department = Column(String(100))
    
    grades = relationship("Grades", primaryjoin="and_(Student.id == foreign(Grades.student_id))")


class Grades(Timestamp, Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"), index=True)
    score = Column(Integer)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)

    student = relationship("Student", primaryjoin="and_(Student.id == foreign(Grades.student_id))", back_populates="grades")
    exam = relationship("Exam", primaryjoin="and_(Exam.id == foreign(Grades.exam_id))", back_populates="grades")
    
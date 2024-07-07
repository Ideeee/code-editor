import datetime as dt
import enum
import bcrypt

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Enum, Text, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp
from .student_models import Grades


class Role(enum.Enum):
    BaseAdmin = "Admin"
    User = "User"

class Admin(Timestamp, Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(Text(), nullable=False)
    role = Column(Enum(Role), nullable=False)

    def make_password_hash(password):
        hash = bcrypt.hashpw(password=password.encode('utf-8'), salt=bcrypt.gensalt())
        return hash.decode('utf-8')
    
    def check_password(self, password: str):
        result = bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
        return result
    
    
    exams = relationship("Exam", primaryjoin="and_(Admin.id == foreign(Exam.admin_id))", back_populates="created_by")



# class Profile(Timestamp, Base):
#     __tablename__ = "profiles"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     is_active = Column(Boolean, default=False)
#     # questions = Column(String(50))

class Exam(Timestamp, Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    admin_id = Column(Integer, ForeignKey("admin.id"), nullable=False)

    created_by = relationship("Admin", primaryjoin="and_(Admin.id == foreign(Exam.admin_id))", back_populates="exams")
    grades = relationship("Grades", primaryjoin="and_(Exam.id == foreign(Grades.exam_id))")
    # questions = relationship("Question", primaryjoin="and_(Topic.id == foreign(Question.topic_id))", viewonly=True) 

    
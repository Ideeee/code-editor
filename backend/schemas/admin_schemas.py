from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from models.admin_model import Role




class AdminBase(BaseModel):
    username: str


class AdminLogin(AdminBase):
    password: str


class AdminCreate(AdminBase):
    first_name: Optional[str]
    last_name: Optional[str]
    password: str
    role: Role


class Admin(AdminBase):
    id: int
    # is_active: bool
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True

class ExamBase(BaseModel):
    title: str


class ExamCreate(ExamBase):
    pass


class Exam(ExamBase):
    id: int
    admin_id: int
    created_at: datetime
    updated_at: datetime 

    class Config:
        orm_mode = True 
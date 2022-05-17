from sqlalchemy import Column, String, DateTime, \
    VARCHAR

from common.model import BaseModel
from sqlalchemy import Column, String, DateTime, \
    VARCHAR

from common.model import BaseModel


# from flask import app as apps
# from app import db as db
# from common.model import BaseModel


class Student(BaseModel):
    __tablename__ = 'student'
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(20))
    hashed_password = Column(VARCHAR(20))
    gender = Column(String(10))
    dob = Column(DateTime())

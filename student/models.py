from datetime import datetime, timedelta

import jwt
from decouple import config
from sqlalchemy import Column, String, DateTime, Text

from common.model import BaseModel


class Student(BaseModel):
    __tablename__ = 'student'
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(20), unique=True, nullable=False)
    hashed_password = Column(Text())
    gender = Column(String(10))
    dob = Column(DateTime())

    def generate_access_token(self, std_obj, source=None, login_history_id=None):
        return jwt.encode({
            '_id': str(std_obj._id),
            'email': std_obj.email,
            'login_id': str(login_history_id),
            'is_guest': False,
            'source': source,
            'ts': (datetime.now() + timedelta(minutes=int(config('access_token_time_in_min')))).strftime(
                '%Y-%m-%d %H:%M:%S'),

        }, config('jwt_secret'), algorithm="HS256")

    def generate_refresh_token(self, std_obj, source=None, login_history_id=None):
        return jwt.encode({
            '_id': str(std_obj._id),
            'login_id': str(login_history_id),
            'is_guest': False,
            'source': source,
            'refresh_ts': (datetime.now() + timedelta(minutes=int(config('refresh_token_time_in_min')))).strftime(
                '%Y-%m-%d %H:%M:%S'),

        }, config('jwt_secret'), algorithm="HS256")

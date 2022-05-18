from datetime import datetime, timedelta

import jwt
from decouple import config
from sqlalchemy import Column, String, DateTime

from common.model import BaseModel


class Student(BaseModel):
    __tablename__ = 'student'
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(20))
    hashed_password = Column(String(255))
    gender = Column(String(10))
    dob = Column(DateTime())

    def generate_access_token(self, source=None,login_history_id=None):
        return jwt.encode({
            '_id': str(self._id),
            'email': self.email,
            'login_id': str(login_history_id),
            'is_guest': False,
            'source': source,
            'ts': (datetime.now() + timedelta(minutes=int(config('access_token_time_in_min')))).strftime(
                '%Y-%m-%d %H:%M:%S'),

        },config('secret'), algorithm="HS256")

    def generate_refresh_token(self,source=None,login_history_id=None):
        return jwt.encode({
            '_id': str(self._id),
            'login_id': str(login_history_id),
            'is_guest': False,
            'source': source,
            'refresh_ts': (datetime.now() + timedelta(minutes=int(config('refresh_token_time_in_min')))).strftime(
                '%Y-%m-%d %H:%M:%S'),

        },config('secret'), algorithm="HS256")

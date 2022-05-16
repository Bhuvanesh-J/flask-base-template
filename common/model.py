import uuid

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    _id = db.Column(db.String(40), default=str(uuid.uuid4()), primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, blank=True, nullable=True)
    # client_id

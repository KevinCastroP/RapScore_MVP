#!/usr/bin/python3
"""
Creating table User
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, PrimaryKeyConstraint
from sqlalchemy import Integer, DateTime, Float


class User(BaseModel, Base):
    """Representation of user"""
    username = Column(String(50), primary_key=True,
                      nullable=False, autoincrement=False)
    email = Column(String(100), nullable=False)
    psswd = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

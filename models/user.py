#!/usr/bin/python3
"""
Creating table User
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy import Integer, DateTime, Float
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Representation of user"""
    __tablename__ = 'user'
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    psswd = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

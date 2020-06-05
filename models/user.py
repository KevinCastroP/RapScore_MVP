#!/usr/bin/python3
"""
Creating table User
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Representation of user"""
    if models.storage_t == "db":
        __tablename__= 'user'
        username = Column(String(50), primary_key=True, nullable=False, autoincrement=False)
        email = Column(String(100), nullable=False)
        psswd = Column(String(50), nullable=False)
        status = Column(String(50), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        username = ""


    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

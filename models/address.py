#!/usr/bin/python3
"""
Creating table address
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime
from sqlalchemy.orm import relationship

class Address(BaseModel, Base):
    """Representation of Address"""
    if models.storage_t == "db":
        __tablename__= 'address'
        id = Column(Integer(3), primary_key=True, nullable=False, autoincrement=False)
        person = Column(Integer(11), primary_key=True, nullable=False, autoincrement=False)
        address = Column(String(100), nullable=True)
        observations = Column(String(100), nullable=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        id = ""
        person = ""


    def __init__(self, *args, **kwargs):
        """Initializes address"""
        super().__init__(*args, **kwargs)

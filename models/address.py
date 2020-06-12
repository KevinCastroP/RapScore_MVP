#!/usr/bin/python3
"""
Creating table address
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime
from models.person import Person
from models.base_model import BaseModel, Base


class Address(BaseModel, Base):
    """Representation of Address"""
    __tablename__ = 'address'
    # id = Column(Integer, primary_key=True,
    #             nullable=False, autoincrement=True)
    person = Column(String(60), ForeignKey("person.id"), nullable=False, autoincrement=False)
    address = Column(String(100), nullable=True)
    observations = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes address"""
        super().__init__(*args, **kwargs)

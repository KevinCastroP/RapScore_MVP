#!/usr/bin/python3
"""
Creating table address
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import PrimaryKeyConstraint, Integer, DateTime
from models import person


class Address(BaseModel, Base):
    """Representation of Address"""
    id = Column(Integer(3), primary_key=True,
                nullable=False, autoincrement=True)
    person = Column(Integer(11), nullable=False, autoincrement=False,
                    ForeignKey('person.id'))
    address = Column(String(100), nullable=True)
    observations = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes address"""
        super().__init__(*args, **kwargs)

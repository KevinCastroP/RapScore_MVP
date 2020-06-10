#!/usr/bin/python3
"""
Creating table Worker
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime, Float
from models.person import Person
from models.base_model import Base


class Worker(Base):
    """Representation of worker"""
    __tablename__ = 'worker'
    worker = Column(Integer(11), primary_key=True,
                    nullable=False, autoincrement=False,
                    ForeignKey('person.id'))
    score = Column(Float, nullable=False)
    type_vehicle = Column(String(50), nullable=True)
    date_incorporation = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes worker"""
        super().__init__(*args, **kwargs)

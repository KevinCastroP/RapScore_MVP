#!/usr/bin/python3
"""
Creating table Worker
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Worker(BaseModel, Base):
    """Representation of worker"""
    if models.storage_t == "db":
        __tablename__= 'worker'
        worker = Column(Integer(11), primary_key=True, nullable=False, autoincrement=False)
        score = Column(Float, nullable=False)
        type_vehicle = Column(String(50), nullable=True)
        date_incorporation = Column(DateTime, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        worker = ""


    def __init__(self, *args, **kwargs):
        """Initializes worker"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""
Creating table Request
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Request(BaseModel, Base):
    """Representation of Request"""
    if models.storage_t == "db":
        __tablename__= 'request'
        id = Column(Integer(11), primary_key=True, nullable=False, autoincrement=True)
        worker = Column(Integer(11), nullable=False, autoincrement=False)
        amount_request = Column(Float, nullable=False)
        status = Column(String(20), nullable=False)
        type_loan = Column(Integer(11), nullable=False)
        observations = Column(String(100), nullable=False)
        request_date = Column(DateTime, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        id = ""
        worker = ""


    def __init__(self, *args, **kwargs):
        """Initializes Request"""
        super().__init__(*args, **kwargs)

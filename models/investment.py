#!/usr/bin/python3
"""
Creating table investment
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Investment(BaseModel, Base):
    """Representation of Investment"""
    if models.storage_t == "db":
        __tablename__= 'investment'
        id = Column(Integer(11), primary_key=True, nullable=False, autoincrement=True)
        investor = Column(Integer(11), nullable=False, autoincrement=False)
        term_in_months = Column(Integer(5), nullable=False)
        rentability = Column(Float, nullable=False)
        status = Column(String(15), nullable=False)
        investment_date = Column(DateTime, nullable=False)
        return_date = Column(DateTime, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        id = ""
        investor = ""


    def __init__(self, *args, **kwargs):
        """Initializes investment"""
        super().__init__(*args, **kwargs)

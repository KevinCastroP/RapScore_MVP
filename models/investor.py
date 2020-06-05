#!/usr/bin/python3
"""
Creating table Investor
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Investor(BaseModel, Base):
    """Representation of investor"""
    if models.storage_t == "db":
        __tablename__= 'investor'
        investor = Column(Integer(11), primary_key=True, nullable=False, autoincrement=False)
        bank_name = Column(String(100), nullable=False)
        type_account = Column(String(50), nullable=False)
        number_account = Column(String(100), nullable=False)
        date_incorporation = Column(DateTime, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        investor = ""


    def __init__(self, *args, **kwargs):
        """Initializes investor"""
        super().__init__(*args, **kwargs)

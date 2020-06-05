#!/usr/bin/python3
"""
Creating table Loan
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime, Float
from sqlalchemy.orm import relationship

class Loan(BaseModel, Base):
    """Representation of loan"""
    if models.storage_t == "db":
        __tablename__= 'loan'
        id = Column(Integer(11), primary_key=True, nullable=False, autoincrement=True)
        number_request = Column(Integer(11), nullable=False)
        amount_outlay = Column(Float, nullable=False)
        term_in_months = Column(Integer(5), nullable=False)
        interest_rate = Column(Float, nullable=False)
        outlay_date = Column(DateTime, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        id = ""
        number_request = ""


    def __init__(self, *args, **kwargs):
        """Initializes loan"""
        super().__init__(*args, **kwargs)

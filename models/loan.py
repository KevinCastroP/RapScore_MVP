#!/usr/bin/python3
"""
Creating table Loan
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import PrimaryKeyConstraint, Integer, DateTime, Float
from models import request


class Loan(BaseModel, Base):
    """Representation of loan"""
    id = Column(Integer(11), primary_key=True,
                nullable=False, autoincrement=True)
    number_request = Column(Integer(11), nullable=False,
                            ForeignKey('request.id'))
    amount_outlay = Column(Float, nullable=False)
    term_in_months = Column(Integer(5), nullable=False)
    interest_rate = Column(Float, nullable=False)
    outlay_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes loan"""
        super().__init__(*args, **kwargs)

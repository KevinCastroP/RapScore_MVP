#!/usr/bin/python3
"""
Creating table Type loan
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, PrimaryKeyConstraint
from sqlalchemy import Integer, DateTime, Float


class Type_loan(BaseModel, Base):
    """Representation of type loan"""
    id = Column(Integer(11), primary_key=True,
                nullable=False, autoincrement=True)
    description = Column(String(100), nullable=False)
    amount_min = Column(Float, nullable=False)
    amount_max = Column(Float, nullable=False)
    score_min = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    term_min = Column(Integer(5), nullable=False)
    term_max = Column(Integer(5), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes type loan"""
        super().__init__(*args, **kwargs)

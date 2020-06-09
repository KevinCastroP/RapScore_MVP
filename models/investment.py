#!/usr/bin/python3
"""
Creating table investment
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import PrimaryKeyConstraint, Integer, DateTime, Float
from models import investor


class Investment(BaseModel, Base):
    """Representation of Investment"""
    id = Column(Integer(11), primary_key=True,
                nullable=False, autoincrement=True)
    investor = Column(Integer(11), nullable=False, autoincrement=False,
                      ForeignKey('investor.investor'))
    term_in_months = Column(Integer(5), nullable=False)
    rentability = Column(Float, nullable=False)
    status = Column(String(15), nullable=False)
    investment_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes investment"""
        super().__init__(*args, **kwargs)

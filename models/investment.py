#!/usr/bin/python3
"""
Creating table investment
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime, Float
from models import investor
from models.base_model import BaseModel, Base


class Investment(BaseModel, Base):
    """Representation of Investment"""
    __tablename__ = 'investment'
    # id = Column(Integer, primary_key=True,
    #             nullable=False, autoincrement=True)
    investor = Column(String(60), ForeignKey('investor.id'), nullable=False, autoincrement=False)
    amount = Column(Float, nullable=False)
    term_in_months = Column(Integer, nullable=False)
    rentability = Column(Float, nullable=False)
    status = Column(String(15), nullable=False)
    investment_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes investment"""
        super().__init__(*args, **kwargs)

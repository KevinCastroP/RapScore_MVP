#!/usr/bin/python3
"""
Creating table Investor
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime, Float
from models.person import Person
from models.base_model import Base


class Investor(Base):
    """Representation of investor"""
    __tablename__ = 'investor'
    investor = Column(Integer(11), primary_key=True,
                      nullable=False, autoincrement=False,
                      ForeignKey('person.id'))
    bank_name = Column(String(100), nullable=False)
    type_account = Column(String(50), nullable=False)
    number_account = Column(String(100), nullable=False)
    date_incorporation = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes investor"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""
Creating table person
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime
from models.user import User
from models.base_model import BaseModel, Base


class Person(BaseModel, Base):
    """Representation of Person"""
    __tablename__ = 'person'
    # id = Column(Integer, primary_key=True,
    #             nullable=False, autoincrement=True)
    user = Column(String(50), ForeignKey('user.username'), nullable=False)
    type_id = Column(String(5), nullable=False)
    number_identification = Column(String(30), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    name_company = Column(String(100), nullable=True)
    business_name = Column(String(100), nullable=True)
    tradename = Column(String(100), nullable=True)
    legal_status = Column(String(20), nullable=True)
    legal_repre_type_id = Column(String(5), nullable=True)
    legal_repre_number_id = Column(String(20), nullable=True)
    legal_repre_full_name = Column(String(100), nullable=True)
    born_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes person"""
        super().__init__(*args, **kwargs)

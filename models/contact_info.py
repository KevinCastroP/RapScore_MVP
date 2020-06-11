#!/usr/bin/python3
"""
Creating table Contact info
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime
from models.person import Person
from models.base_model import BaseModel, Base


class Contact_info(BaseModel, Base):
    """Representation of Contact info"""
    __tablename__ = 'contact_info'
    person = Column(Integer, ForeignKey('person.id'), primary_key=True,
                    nullable=False, autoincrement=False)
    type_contact = Column(String(5), primary_key=True,
                          nullable=False, autoincrement=False)
    data_contact = Column(String(50), nullable=False)
    description = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes Contact info"""
        super().__init__(*args, **kwargs)

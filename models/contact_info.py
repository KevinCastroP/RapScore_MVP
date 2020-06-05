#!/usr/bin/python3
"""
Creating table Contact info
"""
import models
from models.base_model import BaseModel, Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Integer, DateTime
from sqlalchemy.orm import relationship

class Contact_info(BaseModel, Base):
    """Representation of Contact info"""
    if models.storage_t == "db":
        __tablename__= 'contact_info'
        person = Column(Integer(11), primary_key=True, nullable=False, autoincrement=False)
        type_contact = Column(String(5), primary_key=True, nullable=False, autoincrement=False)
        data_contact = Column(String(50), nullable=False)
        description = Column(String(100), nullable=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        person = ""
        type_contact = ""


    def __init__(self, *args, **kwargs):
        """Initializes Contact info"""
        super().__init__(*args, **kwargs)

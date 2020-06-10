#!/usr/bin/python3
"""
Creating table Request
"""
import models
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer, DateTime, Float
from models.worker import Worker
from models.type_loan import Type_loan
from models.base_model import Base


class Request(Base):
    """Representation of Request"""
    __tablename__ = 'request'
    id = Column(Integer(11), primary_key=True,
                nullable=False, autoincrement=True)
    worker = Column(Integer(11), nullable=False, autoincrement=False,
                    ForeignKey('worker.worker'))
    type_loan = Column(Integer(11), nullable=False, ForeignKey('type_loan.id'))
    amount_request = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    observations = Column(String(100), nullable=False)
    request_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes Request"""
        super().__init__(*args, **kwargs)

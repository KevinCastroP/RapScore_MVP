#!/usr/bin/python3
"""
Contains class BaseModel
"""

import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid


Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)


    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = uuid.uuid4()

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()


    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)


    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        time = "%d-%b-%Y (%H:%M:%S.%f)"
        if "born_date" in new_dict:
            new_dict["born_date"] = new_dict["born_date"].strftime(time)
        if "investment_date" in new_dict:
            new_dict["investment_date"] = new_dict["investment_date"].strftime(time)
        if "return_date" in new_dict:
            new_dict["return_date"] = new_dict["return_date"].strftime(time)
        if "date_incorporation" in new_dict:
            new_dict["date_incorporation"] = new_dict["date_incorporation"].strftime(time)
        if "outlay_date" in new_dict:
            new_dict["outlay_date"] = new_dict["outlay_date"].strftime(time)
        if "request_date" in new_dict:
            new_dict["request_date"] = new_dict["request_date"].strftime(time)
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        del new_dict["_sa_instance_state"]
        return new_dict
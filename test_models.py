#!/usr/bin/python3
"""
Listing all objects from State table
"""


if __name__ == '__main__':
    from sys import argv
    from models.base_model import BaseModel, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from datetime import datetime
    import sqlalchemy
    from sqlalchemy import Column, String
    from sqlalchemy import Integer, DateTime, Float
    from models.address import Address
    from models.contact_info import Contact_info
    from models.investment import Investment
    from models.investor import Investor
    from models.loan import Loan
    from models.person import Person
    from models.request import Request
    from models.type_loan import Type_loan
    from models.user import User
    from models.worker import Worker


    Base = declarative_base()
 
    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(
            argv[1], argv[2], argv[3], argv[4]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = User()
    obj.username = "crazyD"
    obj.email = "hanibal@pepito.com"
    obj.psswd = "123bitch"
    obj.status = "active"
    session.add(obj)
    session.commit()
    session.close()
    # test for user table
    # for count in session.query(User).order_by(User.username).all():
    #     print("{} {} {} {} {} {}".format(count.username, count.email, count.psswd, count.status,
    #                                      count.created_at, count.updated_at))
    # session.close()

    #test for person table
    # for count in session.query(Person).order_by(Person.id).all():
    #     print("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(count.id, count.username, count.type_id, count.number_identification,
    #                                                                    count.first_name, count.last_name, count.name_company,
    #                                                                    count.business_name, count.tradename, count.legal_status,
    #                                                                    count.legal_repre_type_id, count.legal_repre_number_id, count.legal_repre_full_name,
    #                                                                    count.born_date, count.created_at, count.updated_at))
    # session.close()

#!/usr/bin/python3
"""
Listing all objects from State table
"""


if __name__ == '__main__':
    from sys import argv
    from models.base_model import Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from datetime import datetime
    import sqlalchemy
    from sqlalchemy import Column, String
    from sqlalchemy import Integer, DateTime, Float

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'user'
        username = Column(String(50), primary_key=True,
                          nullable=False, autoincrement=False)
        email = Column(String(100), nullable=False)
        psswd = Column(String(50), nullable=False)
        status = Column(String(50), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(
            argv[1], argv[2], argv[3], argv[4]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(User).order_by(User.username).all():
        print("{} {} {} {} {} {}".format(state.username, state.email, state.psswd, state.status,
                                         state.created_at, state.updated_at))
    session.close()

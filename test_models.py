#!/usr/bin/python3
"""
Listing all objects from State table
"""


if __name__ == '__main__':
    import json
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
    session.close()
    # creating a new user
    # obj = User()
    # obj.username = "crazyD"
    # obj.email = "hanibal@pepito.com"
    # obj.psswd = "123bitch"
    # obj.status = "active"
    # session.add(obj)
    # session.commit()
    # session.close()
    
    # test user table (delete, show, quit, create)
    # while True:
    #     for user in session.query(User).all():
    #         print("{} {}".format(user.id, user.username))
    #     option = input("select an option\n c: create, s: show, d: delete, q: quit\n-> ")
    #
    #     if option == "c":
    #         obj = User()
    #         obj.username = "crazyD"
    #         obj.email = "hanibal@pepito.com"
    #         obj.psswd = "123bitch"
    #         obj.status = "active"
    #         session.add(obj)
    #         session.commit()
    #     elif option == "s":
    #         uId = input("type the id: ")
    #         users = session.query(User).filter_by(id = uId).all()
    #         print(json.dumps(users[0].to_dict(), indent=2))
    #     elif option == "d":
    #         uId = input("type the id: ")
    #         users = session.query(User).filter_by(id = uId).all()
    #         session.delete(users[0])
    #         session.commit()
    #     elif option == "q":
    #         break
    # session.close()

    # test person table (delete, show, quit, create)
    # while True:
    #     print("Users")
    #     print([us.id for us in session.query(User).all()])
    #     print("=================================================")
    #     print("Persons")
    #     print([(pe.id, pe.first_name, pe.last_name) for pe in session.query(Person).all()])
    #     option = input("select an option\n c: create, s: show, d: delete, q: quit\n-> ")
       
    #     if option == "c":
    #         obj = Person()
    #         user = input("type the user Id: ")
    #         obj.user = user
    #         obj.type_id = "cc"
    #         obj.number_identification = "1106893268"
    #         obj.first_name = "Kevin"
    #         obj.last_name = "Castro"
    #         obj.born_date = "1991-09-12"
    #         session.add(obj)
    #         session.commit()
    #     elif option == "s":
    #         uId = input("type the id: ")
    #         users = session.query(Person).filter_by(id = uId).all()
    #         print(json.dumps(users[0].to_dict(), indent=2))
    #     elif option == "d":
    #         uId = input("type the id: ")
    #         users = session.query(Person).filter_by(id = uId).all()
    #         session.delete(users[0])
    #         session.commit()
    #     elif option == "q":
    #         break
    # session.close()

    # test investor table (delete, show, quit, create)
    # while True:
    #     print("Users")
    #     print([us.id for us in session.query(User).all()])
    #     print("=================================================")
    #     print("Persons")
    #     print([(pe.id, pe.first_name, pe.last_name) for pe in session.query(Person).all()])
    #     print("=================================================")
    #     print("Investor")
    #     print([(inv.id, inv.investor, inv.bank_name) for inv in session.query(Investor).all()])
    #     option = input("select an option\n c: create, s: show, d: delete, q: quit\n-> ")
       
    #     if option == "c":
    #         obj = Investor()
    #         per = input("type the person Id: ")
    #         obj.investor = per
    #         obj.bank_name = "Bancolombia"
    #         obj.type_account = "ahorros"
    #         obj.number_account = "55555555555"
    #         obj.date_incorporation = "2020-06-12"
    #         session.add(obj)
    #         session.commit()
    #     elif option == "s":
    #         uId = input("type the id: ")
    #         users = session.query(Investor).filter_by(id = uId).all()
    #         print(json.dumps(users[0].to_dict(), indent=2))
    #     elif option == "d":
    #         uId = input("type the id: ")
    #         users = session.query(Investor).filter_by(id = uId).all()
    #         session.delete(users[0])
    #         session.commit()
    #     elif option == "q":
    #         break
    # session.close()

    # test investment table (delete, show, quit, create)
    # while True:
    #     print("Investor")
    #     print([(inv.id, inv.investor, inv.bank_name) for inv in session.query(Investor).all()])
    #     print("=================================================")
    #     print("Investment")
    #     print([(inve.id, inve.investor, inve.amount) for inve in session.query(Investment).all()])
    #     option = input("select an option\n c: create, s: show, d: delete, q: quit\n-> ")

    #     if option == "c":
    #         obj = Investment()
    #         inv = input("type the investor Id: ")
    #         obj.investor = inv
    #         obj.amount = 5000
    #         obj.term_in_months = 8
    #         obj.rentability = 2.05
    #         obj.status = "vigente"
    #         obj.investment_date = "2020-06-13"
    #         obj.return_date = "2020-12-12"
    #         session.add(obj)
    #         session.commit()
    #     elif option == "s":
    #         uId = input("type the id: ")
    #         users = session.query(Investment).filter_by(id = uId).all()
    #         print(json.dumps(users[0].to_dict(), indent=2))
    #     elif option == "d":
    #         uId = input("type the id: ")
    #         users = session.query(Investment).filter_by(id = uId).all()
    #         session.delete(users[0])
    #         session.commit()
    #     elif option == "q":
    #         break
    # session.close()

    # test for show user table
    # for count in session.query(User).order_by(User.username).all():
    #     print("{} {} {} {} {} {}".format(count.username, count.email, count.psswd, count.status,
    #                                      count.created_at, count.updated_at))
    #     session.delete(count)
    # session.commit()
    # session.close()

    #test for show person table
    # for count in session.query(Person).order_by(Person.id).all():
    #     print("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(count.id, count.username, count.type_id, count.number_identification,
    #                                                                    count.first_name, count.last_name, count.name_company,
    #                                                                    count.business_name, count.tradename, count.legal_status,
    #                                                                    count.legal_repre_type_id, count.legal_repre_number_id, count.legal_repre_full_name,
    #                                                                    count.born_date, count.created_at, count.updated_at))
    # session.close()

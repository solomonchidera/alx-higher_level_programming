#!/usr/bin/python3
"""This script prints the first State object from
the database hbtn_0e_6_usa by using SQLAlchemy
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    mysql_engine = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(mysql_engine.format(USER, PASS, DB))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

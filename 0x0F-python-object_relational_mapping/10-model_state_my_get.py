#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa by
using SQLAlchemy
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    USR = argv[1]
    PASS = argv[2]
    DB = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USR, PASS, DB))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == state_name)
    if states.count() != 0:
        for state in states:
            print(state.id)
    else:
        print("Not found")

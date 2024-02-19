#!/usr/bin/python3
"""script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USER, PASS, DB))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%"))
    for state in states:
        print("{}: {}".format(state.id, state.name))

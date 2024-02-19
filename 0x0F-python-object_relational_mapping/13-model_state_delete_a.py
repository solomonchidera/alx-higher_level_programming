#!/usr/bin/python3
"""This script deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa by using sqlalchemy
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    USR = argv[1]
    PASS = argv[2]
    DB = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%"))
    if states.count():
        for state in states:
            session.delete(state)
        session.commit()
    session.close()

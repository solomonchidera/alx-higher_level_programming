#!/usr/bin/python3
"""script that changes the name of a State object
from the database hbtn_0e_6_usa by using sqlalchemy
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
                           .format(USR, PASS, DB))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).one()
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()

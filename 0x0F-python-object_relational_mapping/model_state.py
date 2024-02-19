#!/usr/bin/python3
"""Module that contains the class definition of a
State and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """A State class links to states table:
    Attributes:
        id: state identifier
        name: state name
    """
    __tablename__ = "states"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)

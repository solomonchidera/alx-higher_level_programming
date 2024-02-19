#!/usr/bin/python3
"""Module that contains the class definition of a
City
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """A City class links to cities table:
    Attributes:
        id: city identifier
        name: city name
        state_id : state identifier (FK)
    """
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

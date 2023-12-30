#!/usr/bin/python3
""" This module contains City Class """

from relationship_state import Base, State
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """ City class """
    __tablename__ = 'cities'

    id = Column('id', Integer, unique=True, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)

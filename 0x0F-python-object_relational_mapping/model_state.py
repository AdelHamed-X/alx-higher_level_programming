#!/usr/bin/python3
""" This module has the State class """

from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('MySQL://root:root@localhost', port=3306)


class State(Base):
    """ State Class """
    __tablename__ = 'states'

    id = Column('id', Integer, unique=True, auto_increment=True,
            nullable=False)
    name = Column('name', String(128), nullable=False)

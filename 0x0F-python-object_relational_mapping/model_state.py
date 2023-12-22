#!/usr/bin/python3
""" This module has the State class """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ State Class """
    __tablename__ = 'states'

    id = Column('id', Integer, unique=True, auto_increment=True,
            nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    

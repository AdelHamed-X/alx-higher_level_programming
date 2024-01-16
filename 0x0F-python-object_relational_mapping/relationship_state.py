#!/usr/bin/python3
""" This module has the State class """

from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from typing import List

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ State Class """
    __tablename__ = 'states'

    id = Column('id', Integer, unique=True,
                nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    cities: Mapped[List['City']] = relationship(backref='state')

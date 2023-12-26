#!/usr/bin/python3
""" A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")

    Session = sessionmaker()
    session = Session(bind=engine)

    with session.begin():
        state_to_update = session.query(State).filter_by(id=2).first()
        state_to_update.name = "New Mexico"

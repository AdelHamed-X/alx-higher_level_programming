#!/usr/bin/python3
""" script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_city import City
from relationship_state import Base, State


if __name__ == '__main__':

    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    session = Session(bind=engine)

    with session.begin():
        California = State(name="California")
        San_Francisco = City(name="San Francisco")
        California.cities.append(San_Francisco)
        session.add_all([California, San_Francisco])
    session.commit()

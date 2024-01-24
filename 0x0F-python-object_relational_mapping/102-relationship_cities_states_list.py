#!/usr/bin/python3
""" A script that lists all City objects from the database hbtn_0e_101_usa """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    usr, pwd, db = argv[1:]

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@localhost/{db}")
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    session = Session(bind=engine)

    for instance in session.query(State):
        for city_instance in instance.cities:
            print(f"{city_instance.id}: {city_instance.name} "
                  f"-> {instance.name}")

#!/usr/bin/python3
""" A script that lists all State objects from the database hbtn_0e_6_usa """

from sqlalchemy import create_engine, text()

if __name__ == '__main__':
    from model_state import Base, State

    engine = create_engine()
    with engine.connection() as conn:
        result = conn.execute(text("SELECT states.id, states.name FROM states\
                                   ORDER BY states.id;"))

    for state in result:
        print(f"{state[0]}: {state[1]}")

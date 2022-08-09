#!/usr/bin/python3
"""Module to add object to states table"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    user = argv[1]
    password = argv[2]
    db = argv[3]

    # Create engine and local_session
    connect_string = f"mysql+mysqldb://{user}:{password}@localhost/{db}"
    engine = create_engine(connect_string, pool_pre_ping=True)
    Session = sessionmaker()
    local_session = Session(bind=engine)

    # Find object to update and update
    state_to_update = local_session.query(State).filter(State.id == 2).first()
    state_to_update.name = 'New Mexico'

    # Add to database
    local_session.commit()

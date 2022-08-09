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

    # Find states to delete
    states_to_delete = local_session.query(State).\
        filter(State.name.contains('a')).all()

    # Delete states from database
    for state in states_to_delete:
        local_session.delete(state)

    local_session.commit()

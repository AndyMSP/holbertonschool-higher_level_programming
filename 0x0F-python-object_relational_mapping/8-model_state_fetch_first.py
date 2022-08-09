#!/usr/bin/python3
"""Lists all state objects from the database given"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    # Create engine and local_session
    connect_string = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(connect_string, pool_pre_ping=True)
    Session = sessionmaker()
    local_session = Session(bind=engine)

    # Perform query
    results = local_session.query(State).first()

    # Print results
    if results == None:
        print("Nothing")
    else:
        print(f"{results.id}: {results.name}")

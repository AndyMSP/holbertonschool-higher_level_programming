#!/usr/bin/python3
"""Lists all state objects from the database given"""


if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    user = argv[1]
    password = argv[2]
    db = argv[3]
    match = argv[4]

    # Create engine and local_session
    connect_string = f"mysql+mysqldb://{user}:{password}@localhost/{db}"
    engine = create_engine(connect_string, pool_pre_ping=True)
    Session = sessionmaker()
    local_session = Session(bind=engine)

    # Perform query
    results = local_session.query(State).filter(State.name == match).all()

    # Print results
    if len(results) == 0:
        print("Not found")
    else:
        for item in results:
            print(item.id)

#!/usr/bin/python3

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

    # Create new state object
    new_state = State(name='Louisiana')

    # Add to database
    local_session.add(new_state)
    local_session.commit()

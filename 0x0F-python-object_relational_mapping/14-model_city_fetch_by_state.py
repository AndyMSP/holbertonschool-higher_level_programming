#!/usr/bin/python3
"""Prints city, city_id and state"""


if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
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

    # Perform query
    l_cities = local_session.query(City.name, City.id, State.name).join(State).order_by(City.id).all()

    for item in l_cities:
        print(f"{item[2]}: ({item[1]}) {item[0]}")
    
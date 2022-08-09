#!/usr/bin/python3

from main import User, Session, engine

local_session = Session(bind=engine)

# return all objects
users = local_session.query(User).all()
print(users)

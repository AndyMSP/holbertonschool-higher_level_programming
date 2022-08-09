#!/usr/bin/python3

from main import Session, engine, User

local_session = Session(bind = engine)

#ascending
users = local_session.query(User).order_by(User.username).all()

for user in users:
    print(f"{user.username}")

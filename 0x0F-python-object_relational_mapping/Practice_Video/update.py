#!/usr/bin/python3

from main import Session, engine, User

local_session = Session(bind = engine)

user_to_update = local_session.query(User).filter(User.username == 'Andy').first()

user_to_update.username = 'Andy2'

local_session.commit()
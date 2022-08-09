#!/usr/bin/python3

from main import User, engine, Base

Base.metadata.create_all(engine)
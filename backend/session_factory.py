'''Create session and engine for connections'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session_engine():
    '''Create a session and an engine, return both'''
    engine = create_engine(os.environ['DB_STRING'])
    session = sessionmaker(bind=engine)

    return session(), engine

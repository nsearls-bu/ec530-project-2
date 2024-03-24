'''Create session and engine for connections'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ['DB_STRING'])

def get_my_session():
    '''Create a session and an engine, return both'''
    session = sessionmaker(bind=engine)

    return session()

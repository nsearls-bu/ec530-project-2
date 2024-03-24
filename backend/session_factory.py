'''Create session and engine for connections'''
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session_engine():
    engine = create_engine(os.environ['DB_STRING'])
    Session = sessionmaker(bind=engine)

    return Session(), engine
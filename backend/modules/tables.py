from sqlalchemy import Column, DateTime, String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    '''Defines base class for setting up other tables'''
    pass


class Account(Base):
    '''For storing accounts and sessions - will be used for OAuth'''


    __tablename__ = 'ACCOUNT'
    account_id = Column('account_id', String, primary_key=True)
    access_token = Column('access_token', String)
    expires_at = Column('expires_at', DateTime)


class Users(Base):
    '''Stores user profiles and account details'''
    __tablename__ = 'USERS'

    user_id = Column("user_id", String, primary_key=True)
    username = Column("username", String)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    cell = Column("cell", String)
    email = Column("email", String)
    age = Column("age", Integer)


class Documents(Base):
    '''Stores a list of documents with the full text'''
    __tablename__ = 'DOCUMENTS'

    document_id = Column("document_id", String, primary_key=True)
    user_id = Column("user_id", String, ForeignKey("USERS.user_id"))
    uploaded_on = Column("uploaded_on", DateTime)
    fulltext = Column("fulltext", String)


class Paragraphs(Base):
    '''Stores a paragraph in each row for quick access'''

    __tablename__ = 'PARAGRAPHS'
    document_id = Column("document_id", String, ForeignKey("DOCUMENTS.document_id"))
    paragraph_id = Column("paragraph_id", String, primary_key=True)
    text = Column("text", String)


class Connections(Base):
    '''List of connections to various LLMs or text analysers'''

    __tablename__ = 'CONNECTIONS'

    connection_name = Column("connection_name", String)
    connection_type = Column("connection_type", String)
    connection_url = Column("connection_url", String)
    connection_id = Column("connection_id", String, primary_key=True)
    user_id = Column("user_id", String, ForeignKey("USERS.user_id"))


class NLP_Response(Base):
    '''Stores the outputted response from the text analyser'''

    __tablename__ = 'RESPONSE'

    response_id = Column("response_id", String, primary_key=True)
    user_id = Column("user_id", String, ForeignKey("USERS.user_id"))
    document_id = Column("document_id", String)
    title_summary = Column("title_summary", String)
    sentiment_score = Column("sentiment_score", String)
    keywords = Column("keywords", String)
    similar_articles = Column("similar_articles", String)

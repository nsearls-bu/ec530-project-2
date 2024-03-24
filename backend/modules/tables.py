from sqlalchemy import Column, DateTime, String, ForeignKey, Integer, UUID
from sqlalchemy.orm import DeclarativeBase
import uuid

class Base(DeclarativeBase):
    '''Defines base class for setting up other tables'''
    pass


class Account(Base):
    '''For storing accounts and sessions - will be used for OAuth'''


    __tablename__ = 'ACCOUNT'
    account_id = Column('account_id', UUID, primary_key=True, default=uuid.uuid4)
    access_token = Column('access_token', String)
    expires_at = Column('expires_at', DateTime)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Users(Base):
    '''Stores user profiles and account details'''
    __tablename__ = 'USERS'

    user_id = Column("user_id", UUID, primary_key=True, default=uuid.uuid4)
    username = Column("username", String)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    cell = Column("cell", String)
    email = Column("email", String)
    age = Column("age", Integer)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Documents(Base):
    '''Stores a list of documents with the full text'''
    __tablename__ = 'DOCUMENTS'

    document_id = Column("document_id", UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column("user_id", UUID, ForeignKey("USERS.user_id"))
    uploaded_on = Column("uploaded_on", DateTime)
    document_name = Column("document_name", String)
    filetype = Column("filetype", String)
    fulltext = Column("fulltext", String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Paragraphs(Base):
    '''Stores a paragraph in each row for quick access'''

    __tablename__ = 'PARAGRAPHS'
    document_id = Column("document_id", UUID, ForeignKey("DOCUMENTS.document_id"))
    paragraph_id = Column("paragraph_id", UUID, primary_key=True, default=uuid.uuid4)
    text = Column("text", String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Connections(Base):
    '''List of connections to various LLMs or text analysers'''

    __tablename__ = 'CONNECTIONS'

    connection_name = Column("connection_name", String)
    connection_type = Column("connection_type", String)
    connection_url = Column("connection_url", String)
    connection_id = Column("connection_id", UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column("user_id", UUID, ForeignKey("USERS.user_id"))
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class NLP_Response(Base):
    '''Stores the outputted response from the text analyser'''

    __tablename__ = 'RESPONSE'

    response_id = Column("response_id", UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column("user_id", UUID, ForeignKey("USERS.user_id"))
    document_id = Column("document_id", String)
    title_summary = Column("title_summary", String)
    sentiment_score = Column("sentiment_score", String)
    keywords = Column("keywords", String)
    similar_articles = Column("similar_articles", String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

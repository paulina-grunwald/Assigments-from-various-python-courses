#import path module to be able to work between platforms
import os import path

#will be used to describe database
from sqlalchemy import(create_engine,
                       Column,
                       String,
                       Integer,
                       Boolean,
                       Table,
                       ForeignKey)

from sqlalchemy.orm import sessionmaker, relationships
from sqlalchemy.ext.declarative import declarative_base

database_filename = 'twitter.sqlite3'

diretory = path.abspath(path.dirname(__file__))
database_filepath = path.join(diretory, database_filename)

#create engine using file path
engine_url = 'sqlite:///{}'.format(database_filepath)

engine = create_engine(engine_url)

#the database class objects are going to inherit from
#this class
Base = declarative_base(bind=engine)

#create a configured "Session" class
Session = sessionmaker(bind=engine, autoflush=False)

#create a session
session = Session()
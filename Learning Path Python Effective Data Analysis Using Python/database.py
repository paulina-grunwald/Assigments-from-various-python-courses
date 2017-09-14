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

hashtag_tweet = Table('hashtag_tweet', Base.methadata,
                      Column('hashtag_id', Integer, ForeignKey('hashtag.id'), nullable = False),
                      Column('tweet_id', Integer, ForeignKey('tweets.id'), nullable=False))

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    tid = Column(String(100, nullable=False))
    tweet = Column(String(300), nullable=False)
    user_id =
    coordinates =
    user =
    created_at =
    favourite_count =
    in_reply_to_screen_name = Column(String)
    in_reply_to_status_id = Column(Integer)
    in_reply_to_user_id = Column(Integer)
    lang = Column(String)
    quoted_status_id = Column(Integer)
    retweet_count = Column(Integer)



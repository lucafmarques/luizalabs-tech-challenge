import os
import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config

db_url = config.URL()
db = databases.Database(db_url)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(db_url)
metadata.create_all(engine)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

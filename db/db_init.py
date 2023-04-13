import os

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = os.environ['DB_SIGNEDIN_URI']

db = create_engine(db_string)
base = declarative_base()

from models.user import User

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)



